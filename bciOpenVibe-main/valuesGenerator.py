import numpy
import paho.mqtt.client as mqtt
import sys,threading
import time
import struct
import os,json
from random import randrange

#sensorBuffer1 = [0,1,2,3,3,0,1,2,3,3,0,1,2,3,3,0,1,2,3,3,0,1,2,3,3,0,1,2,3,3,0,1,2,3,3,0,1,2,3,3,0,1,2,3,3,0,1,2,3,3,0,1,2,3,3,0,1,2,3,3,0,1,2,3,3,0,1,2,3,3,0,1,2,3,3,0,1,2,3,3,0,1,2,3,3,0,1,2,3,3,0,1,2,3,3,0,1,2,3,3,0,1,2,3,3,0,1,2,3,3,0,1,2,3,3,0,1,2,3,3,0,1,2,3,3,0,1,2,3,3,0,1,2,3,4]
sensorBuffer1=[]
#sensorBuffer1 = [30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30]

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
      # settings are retrieved in the dictionary
      self.channelCount = int(self.setting['Channel count'])
      self.samplingFrequency = int(self.setting['Sampling frequency'])
      self.epochSampleCount = int(self.setting['Generated epoch sample count'])
      global sensorBuffer1
      temp = str(self.setting['RPM']).split(',')
      for item in temp:
          sensorBuffer1.append(float(item))

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
      for rowIndex, row in enumerate(self.signalBuffer):
          # if len(sensorBuffer1) > 0:
          self.signalBuffer[rowIndex,:] = sensorBuffer1[randrange(len(sensorBuffer1))]
          # else:
              # print("Sem dados MQTT")

    def sendSignalBufferToOpenvibe(self):
      start = self.timeBuffer[0]
      end = self.timeBuffer[-1] + 1./self.samplingFrequency
      bufferElements = self.signalBuffer.reshape(self.channelCount*self.epochSampleCount).tolist()
      self.output[0].append( OVSignalBuffer(start, end, bufferElements) )

   # the process is straightforward
    def process(self):
        # if len(sensorBuffer) > 0:
        #     self.output[0].append(sensorBuffer.pop())
        # else:
        #     print("Sem dados MQTT")
       
      #start = self.timeBuffer[0]
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