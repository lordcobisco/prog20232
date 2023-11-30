import numpy
import paho.mqtt.client as mqtt
import sys,threading
import time
import struct
import os,json

sensorTopic4 = ""
sensorBuffer4 = []
sizeBuffer4 = 0


def on_connect4(client, userdata, flags, rc):
	print('connected Mqtt Input')
	client4.subscribe('webCommand')
	client4.publish('requestStart','1')
	
def on_message4(client, userdata, msg):
  global sensorTopic4

  #print(sensorTopic4,msg.topic)
  if msg.topic == 'webCommand':
    msgDict = json.loads(msg.payload)
    sensorTopic4 = "cmd2dev"+str(msgDict['stim2'])
    client4.subscribe(sensorTopic4)
    #print("***webcommand, ",sensorTopic4)
  elif sensorTopic4 in msg.topic:
    data = json.loads(msg.payload)
    #print(data)
    data = data['m'].split(',')
    for i in range(len(data)):
          data[i] = float(data[i])
    if len(sensorBuffer4) > 1:
      #print('Teste3: ', len(sensorBuffer4))
      if data[0] != sensorBuffer4[-1][0]: 
        sensorBuffer4.append(data[0:sizeBuffer4])
        #print('Teste2: ', len(sensorBuffer4))
    else:
        sensorBuffer4.append(data[0:sizeBuffer4])
        #print('Teste1: ', len(sensorBuffer4))

client4 = mqtt.Client()    # Identificacao do Cliente
    # client.username_pw_set(username="minibike",password="minibike2021")     # Usuario e senha do broker
client4.on_connect = on_connect4
client4.on_message = on_message4
#   //client.subscribe(sensorTopic4)
client4.connect('10.1.0.44',1883)



class MyOVBox(OVBox):

    def __init__(self):
      OVBox.__init__(self)
      self.channelCount = 0
      self.samplingFrequency = 0
      self.epochSampleCount = 0
      self.startTime = 0.
      self.endTime = 0.
      self.dimensionSizes = list()
      self.dimensionLabels = list()
      self.timeBuffer = list()
      self.signalBuffer = None
      self.signalHeader = None

   # this time we also re-define the initialize method to directly prepare the header and the first data chunk
    def initialize(self):
      self.t1 = threading.Thread(target = client4.loop_forever)
      self.t1.start()
      print("Inicializou")
      # settings are retrieved in the dictionary
      self.channelCount = int(self.setting['Channel count'])
      self.samplingFrequency = int(self.setting['Sampling frequency'])
      self.epochSampleCount = int(self.setting['Generated epoch sample count'])
      global sizeBuffer4
      sizeBuffer4 = self.channelCount 
      #creation of the signal header
      for i in range(self.channelCount):
         self.dimensionLabels.append( 'Sinus'+str(i) )
      self.dimensionLabels += self.epochSampleCount*['']
      self.dimensionSizes = [self.channelCount, self.epochSampleCount]
      self.signalHeader = OVSignalHeader(0., 0., self.dimensionSizes, self.dimensionLabels, self.samplingFrequency)
      self.output[0].append(self.signalHeader)

      #creation of the first signal chunk
      self.endTime = 1.*self.epochSampleCount/self.samplingFrequency
      self.signalBuffer = numpy.zeros((self.channelCount, self.epochSampleCount))
      self.updateTimeBuffer()
      self.updateSignalBuffer()

    def updateStartTime(self):
      self.startTime += 1.*self.epochSampleCount/self.samplingFrequency

    def updateEndTime(self):
      self.endTime = float(self.startTime + 1.*self.epochSampleCount/self.samplingFrequency)

    def updateTimeBuffer(self):
      self.timeBuffer = numpy.arange(self.startTime, self.endTime, 1./self.samplingFrequency)

    def updateSignalBuffer(self):
      if len(sensorBuffer4) > 0: 
        temp = sensorBuffer4.pop()
      for rowIndex, row in enumerate(self.signalBuffer):
          if len(sensorBuffer4) > 0:
            self.signalBuffer[rowIndex,:] = temp[rowIndex]
          else:
              print("Sem dados MQTT")

    def sendSignalBufferToOpenvibe(self):
      start = self.timeBuffer[0]
      end = self.timeBuffer[-1] + 1./self.samplingFrequency
      bufferElements = self.signalBuffer.reshape(self.channelCount*self.epochSampleCount).tolist()
      self.output[0].append( OVSignalBuffer(start, end, bufferElements) )

   # the process is straightforward
    def process(self):
        # if len(sensorBuffer4) > 0:
        #     self.output[0].append(sensorBuffer4.pop())
        # else:
        #     print("Sem dados MQTT")
       
      start = self.timeBuffer[0]
      end = self.timeBuffer[-1]
      if self.getCurrentTime() >= end:
         self.sendSignalBufferToOpenvibe()
         self.updateStartTime()
         self.updateEndTime()
         self.updateTimeBuffer()
         self.updateSignalBuffer()

   # this time we also re-define the uninitialize method to output the end chunk.
    def uninitialize(self):
      end = self.timeBuffer[-1]
      self.output[0].append(OVSignalEnd(end, end))            

box = MyOVBox()