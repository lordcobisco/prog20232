import paho.mqtt.client as mqtt
import json,threading

def on_connect(client, userdata, flags, rc):
	print('Connected')


client = mqtt.Client()    # Identificacao do Cliente
client.on_connect = on_connect
 

class MyOVBox(OVBox):
	def __init__(self):
		OVBox.__init__(self)


	def initialize(self):
		self.mqttHost = str(self.setting['MQTTHost'])
		self.mqttPort = int(self.setting['MQTTPort'])
		self.topic = str(self.setting['topic'])
		
		client.connect(self.mqttHost,self.mqttPort)
		self.t1 = threading.Thread(target = client.loop_forever)
		self.t1.start()
		print("Inicializou")
		return

	def process(self):
			#print(start)
		for chunkIdx in range( len(self.input[0]) ):
			chunk = self.input[0].pop()
			client.publish(self.topic,str(chunk).replace('[','').replace(']',''))
		return
		
	def uninitialize(self):
		# nop
		return

box = MyOVBox()
