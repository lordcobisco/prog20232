import paho.mqtt.client as mqtt
import json, math,time

class saveIMUMQTTData(mqtt.Client):
    def requestIMUStream(self):
        msg2send = {'op':1}
        msg2send['simulationTime'] = str(self.simulationTime)
        msg2send['frequence'] = self.frequence
        msg2send['sensorType'] = self.sensorType
        print('requestIMUStream: ', self.cmdTopic)
        self.publish(self.cmdTopic,json.dumps(msg2send))

    def stopIMUStream(self):
        msg2send = {'op':22}
        self.publish(self.cmdTopic,json.dumps(msg2send))
    
    def streamReceivedData(self,msg):
        # if topic == self.inputTopic:
        data = msg.payload.decode('utf8').replace(';\n','').split(',')
        acc = [float(data[0]), float(data[1]), float(data[2])]
         # return 180 * math.atan2 (acc[1],math.sqrt(acc[0]*acc[0]))/math.pi
         # return 180 * math.atan2 (acc[0],acc[2])/math.pi,data
        return 180 * math.atan2 (acc[0],acc[1])/math.pi,data

    def connectSensor(self,simulationTime=6000,frequence=20,sensorType = 2):
        devNumber="3912"
        self.stim1 = 'cmd2dev3632'
        self.stim2 = 'cmd2dev4360'

        self.connect('10.1.0.44', 1883, 600)
        self.ssTopic = 'dev'+devNumber+'ss'
        self.cmdTopic = 'cmd2dev'+devNumber
        self.simulationTime = simulationTime
        self.frequence = frequence
        self.sensorType = sensorType
        self.filterGiro = 0
        self.angle = 0
        self.gatePhase = 3
        self.counter = 0
        self.angleMin1 = 25
        self.angleMin2 = 30
        self.flagAngleMin = False
        self.angleMax1 = 60
        self.angleMax2 = 65
        self.flagAngleMax = True
        self.deviceStim = json.loads("{\"op\":2,\"m\":\"Channel String Vector\",\"t\":350,\"p\":20000}\n")
        self.deviceStim1 = json.loads("{\"op\":2,\"m\":\"Channel String Vector\",\"t\":350,\"p\":20000}\n")
        self.deviceStim2 = json.loads("{\"op\":2,\"m\":\"Channel String Vector\",\"t\":350,\"p\":20000}\n")
        #--------------------------------------------------------------------
        #--------------------------------------------------------------------
        #--------------------------------------------------------------------
        self.m1d = "0,0,0,0"
        self.m1e = "0,0,0,0"
        self.m2d = "0,0,0,0"
        self.m2e = "0,0,0,0"
        self.m3d = "0,0,0,0"
        self.m3e = "0,0,0,0"
        self.m4d = "0,0,0,0"
        self.m4e = "0,0,0,0"
        #--------------------------------------------------------------------
        #--------------------------------------------------------------------
        #--------------------------------------------------------------------

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
            self.deviceStim1['m'] = '0,0,0,0'
            self.publish(self.stim1,json.dumps(self.deviceStim1))
            self.deviceStim2['m'] = '0,0,0,0'
            self.publish(self.stim2,json.dumps(self.deviceStim2))   

    def on_connect(self, mqttc, obj, flags, rc):
        print("Connected with result code "+str(rc))
        self.subscribe(self.ssTopic)
        self.subscribe('webCommand')
        self.subscribe('start')
    
    def on_connect_fail(self, mqttc, obj):
        print("Connect failed")
        self.connect('10.1.0.44', 1883, 600)

    def on_message(self, mqttc, obj, msg):
        if msg.topic == 'webCommand':
            msgDict = json.loads(msg.payload)
            self.m1d = msgDict['m1'].split(';')[0]
            self.m1e = msgDict['m1'].split(';')[1]
            self.m2d = msgDict['m2'].split(';')[0]
            self.m2e = msgDict['m2'].split(';')[1]
            self.m3d = msgDict['m3'].split(';')[0]
            self.m3e = msgDict['m3'].split(';')[1]
            self.m4d = msgDict['m4'].split(';')[0]
            self.m4e = msgDict['m4'].split(';')[1]
            self.deviceStim = json.loads("{\"op\":2,\"m\":\"Channel String Vector\",\"t\":"+str(msgDict['ton'])+",\"p\":"+str(msgDict['period'])+"}\n")
            self.deviceStim1 = json.loads("{\"op\":2,\"m\":\"Channel String Vector\",\"t\":"+str(msgDict['ton'])+",\"p\":"+str(msgDict['period'])+"}\n")
            self.deviceStim2 = json.loads("{\"op\":2,\"m\":\"Channel String Vector\",\"t\":"+str(msgDict['ton'])+",\"p\":"+str(msgDict['period'])+"}\n")
        elif 'start' in msg.topic: 
            self.startExperiment(msg)
            self.stopExperiment(msg)
        else:
            try:
                self.angle = self.streamReceivedData(msg)
                self.counter += 1
                if str(msg.payload) == '0':
                    #PERNA DIREITA - CICLO 1
                    #self.deviceStim1['m'] = '8,0,10,0' #1
                    self.deviceStim1['m'] = self.m1d
                    self.publish(self.stim1,json.dumps(self.deviceStim1))
                    #PERNA ESQUERDA - CICLO 1
                    #self.deviceStim2['m'] = '15,0,0,15'#3
                    self.deviceStim2['m'] = self.m1e
                    self.publish(self.stim2,json.dumps(self.deviceStim2))   
                    print('Gate Phase',self.gatePhase)

                elif str(msg.payload) == '1':
                    #PERNA DIREITA - CICLO 2
                    #self.deviceStim1['m'] = '0,12,0,12'#2
                    self.deviceStim1['m'] = self.m2d
                    self.publish(self.stim1,json.dumps(self.deviceStim1))
                    #PERNA ESQUERDA - CICLO 2
                    #self.deviceStim2['m'] = '15,0,0,0'#4
                    self.deviceStim2['m'] = self.m2e          
                    self.publish(self.stim2,json.dumps(self.deviceStim2))   
                    print('Gate Phase',self.gatePhase)

                elif str(msg.payload) == '2':               
                    #PERNA DIREITA - CICLO 3
                    #self.deviceStim1['m'] = '12,0,0,12'#3
                    self.deviceStim1['m'] = self.m3d
                    self.publish(self.stim1,json.dumps(self.deviceStim1))
                    #PERNA ESQUERDA - CICLO 3
                    #self.deviceStim2['m'] = '11,0,13,0'#1
                    self.deviceStim2['m'] = self.m3e
                    self.publish(self.stim2,json.dumps(self.deviceStim2))             
                    print('Gate Phase',self.gatePhase)

                elif str(msg.payload) == '3':
                    #PERNA DIREITA - CICLO 4
                    #self.deviceStim1['m'] = '12,0,0,0'#4
                    self.deviceStim1['m'] = self.m4d
                    self.publish(self.stim1,json.dumps(self.deviceStim1))
                    #PERNA ESQUERDA - CICLO 4
                    #self.deviceStim2['m'] = '0,15,0,15'#2
                    self.deviceStim2['m'] = self.m4e
                    self.publish(self.stim2,json.dumps(self.deviceStim2))     
                    print('Gate Phase',self.gatePhase)

                if self.counter > 100:
                    print(self.angle)
                    self.counter = 0
            except:
                print('Erro no sensor!')
                self.deviceStim['m'] = '0,0,0,0'
                # self.publish(self.cmdTopic,json.dumps(self.deviceStim))
                self.deviceStim1['m'] = '0,0,0,0'
                # self.publish(self.stim1,json.dumps(self.deviceStim1))
                self.deviceStim2['m'] = '0,0,0,0'
                # self.publish(self.stim2,json.dumps(self.deviceStim2))            
imusave = saveIMUMQTTData()
imusave.connectSensor()
#imusave.connectSensor(devNumber="9696")
#imusave.connectSensor(devNumber="8792")
# 7288