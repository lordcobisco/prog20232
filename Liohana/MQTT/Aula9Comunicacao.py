#Aula 9 - Comunicação

#Objetivo: receber e enviar informações do estimulador

import paho.mqtt.client as mqtt
import json

data = "DadosSensorLiohana.txt"

with open(data, 'w') as file:
    file.write("DadosSensor, \n")

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("newdev")
    client.subscribe("dev9840ss")
    client.publish("reconect", ' ')
    client.publish('cmd2dev9840', '{"op":1,"simulationTime":3,"frequence":20,"sensorType":2}')
    
  
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    if msg.topic == "dev9840ss":
        with open(data, 'a') as file:
            file.write(msg.payload.decode('utf8') + "\n")

    


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#(servidor/endereço, porta, 60=tempo de time out)
client.connect("0.tcp.sa.ngrok.io", 10618, 60)

client.loop_forever()