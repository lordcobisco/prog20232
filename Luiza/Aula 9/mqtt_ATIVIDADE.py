import paho.mqtt.client as mqtt
import json

import paho.mqtt.client as mqtt

caminho = 'dadosSensor.txt'
with open(caminho, 'w') as arquivo:
    arquivo.write('Simulation Time: 3, Frequence: 20, Dados do IMU\n')

def IMUdata():
    client.publish('cmd2dev9840',
                 '{"op":1,"simulationTime":3,'+
                 '"frequence":20,"sensorType":2}')
    
def stopIMUdata():
    client.publish('dev9840ss', '{"op":22}')

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("dev9840ss")
    client.subscribe("dev9840status")
    IMUdata()

def on_message(client, userdata, msg):
    print(msg.topic, ": ", msg.payload.decode('utf8'))
    if msg.topic == 'dev9840ss':
        with open(caminho, 'a') as arquivo:
            arquivo.write(msg.payload.decode('utf8') + '\n')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect('0.tcp.sa.ngrok.io', 10618, 60)
client.loop_forever()
