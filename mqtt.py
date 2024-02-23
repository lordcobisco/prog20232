import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("newdev")
    client.subscribe("dev9840ss")

def on_message(client, userdata, msg):
    print(msg.topic+" "+(msg.payload.decode('utf8')))
    client.publish('cmd2dev9840',
                   '{"op":1,"simulationTime":"2","frequence":"2","sensorType":2}')
    if msg.topic == "dev9840ss":
        with open('mqttdados.txt', 'a') as f:
            f.write(msg.payload.decode('utf-8'))
        

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("0.tcp.sa.ngrok.io", 10618, 60)

client.loop_forever()