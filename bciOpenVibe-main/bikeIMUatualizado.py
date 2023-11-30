import paho.mqtt.client as mqtt
import json, math, threading, os

class saveIMUMQTTData(mqtt.Client):
    def requestIMUStream(self):
        msg2send = {'op':1}
        msg2send['simulationTime'] = str(self.simulationTime)
        msg2send['frequence'] = self.frequence
        msg2send['sensorType'] = self.sensorType
        print('requestIMUStream: ', self.cmdTopicSensor)
        self.publish(self.cmdTopicSensor,json.dumps(msg2send))

    def stopIMUStream(self):
        msg2send = {'op':22}
        self.publish(self.cmdTopicSensor,json.dumps(msg2send))
    
    def streamReceivedData(self,msg):
        data = msg.payload.decode('utf8').replace(';\n','').split(',')
        acc = [float(data[0]), float(data[1]), float(data[2])]
        return 180 * math.atan2 (acc[0],acc[2])/math.pi

    def connectSensor(self,sensorNumber,actuatorNumber,simulationTime=6000,frequence=20,sensorType = 2):

        self.connect('10.1.0.44', 1883, 600)
        self.ssTopic = 'dev'+sensorNumber+'ss'
        self.cmdTopicSensor = 'cmd2dev'+sensorNumber
        self.cmdTopic = 'cmd2dev'+actuatorNumber
        self.simulationTime = simulationTime
        self.frequence = frequence
        self.sensorType = sensorType
        self.angle = 0
        self.counter = 0
        self.angleMin1 = -179   #FESBIKE ' Perna esquerda esticada
        self.angleMin2 = -150   #FESBIKE ' Perna esquerda esticada
        self.flagAngleMin = False
        self.angleMax1 = 150   #FESBIKE ' Perna direita esticada
        self.angleMax2 = 175   #FESBIKE ' Perna direita esticada
        self.flagAngleMax = True
        self.deviceStim = json.loads("{\"op\":2,\"m\":\"Channel String Vector\",\"t\":200,\"p\":20000}\n")
        self.p1 = "0,0,0,0"
        self.p2 = "0,0,0,0"
        # self.file = open(self.cmdTopic + '.dev','w')
        # self.requestIMUStream()
        rc = 0
        while rc == 0:
            rc = self.loop()
        return rc
    def startExperiment(self,msg):
        if '1' in msg.payload.decode('utf8'):
            print('Request Start')
            self.requestIMUStream()

    def stopExperiment(self,msg):
        if '0' in msg.payload.decode('utf8'):
            print('Request Stop')
            self.stopIMUStream()
            self.deviceStim['m'] = "0,0,0,0"
            self.publish(self.cmdTopic,json.dumps(self.deviceStim))

    def on_connect(self, mqttc, obj, flags, rc):
        print("Connected with result code "+str(rc))
        self.subscribe(self.ssTopic)
        self.subscribe('webCommand')
        self.subscribe('start')
    
    def on_connect_fail(self, mqttc, obj):
        print("Connect failed")
        self.connect('10.1.1.169', 1883, 600)

    def on_message(self, mqttc, obj, msg):
        if msg.topic == 'webCommand':
            msgDict = json.loads(msg.payload)
            self.p1 = msgDict['p1']
            self.p2 = msgDict['p2']
            self.angleMin1 = float(msgDict['a1'].split(',')[0])
            self.angleMin2 = float(msgDict['a1'].split(',')[1])
            self.angleMax1 = float(msgDict['a2'].split(',')[0])   #FESBIKE ' Perna direita esticada
            self.angleMax2 = float(msgDict['a2'].split(',')[1])   #FESBIKE ' Perna direita esticada
            self.deviceStim = json.loads("{\"op\":2,\"m\":\"Channel String Vector\",\"t\":"+str(msgDict['ton'])+",\"p\":"+str(msgDict['period'])+"}\n")
        elif 'start' in msg.topic: 
            self.startExperiment(msg)
            self.stopExperiment(msg)
        else:
            self.angle = self.streamReceivedData(msg)
            self.counter += 1
            """ self.deviceStim['m'] = '0,10,10,0'
            self.publish(self.cmdTopic,json.dumps(self.deviceStim)) """
            if self.angle > self.angleMin1 and self.angle < self.angleMin2  and not self.flagAngleMin:
                self.flagAngleMin = True
                self.flagAngleMax = False
                self.deviceStim['m'] = self.p1
                self.publish(self.cmdTopic,json.dumps(self.deviceStim))
                print('Direita: ',self.angle)
                
            elif self.angle > self.angleMax1 and self.angle < self.angleMax2 and not self.flagAngleMax:
                self.flagAngleMin = False
                self.flagAngleMax = True
                self.deviceStim['m'] = self.p2
                self.publish(self.cmdTopic,json.dumps(self.deviceStim))
                print('Esquerda', self.angle)

            if self.counter > 100: 
                print(self.angle)
                self.counter = 0

imusave = saveIMUMQTTData()

imusave.connectSensor(sensorNumber="6200",actuatorNumber='4360')
# 7288