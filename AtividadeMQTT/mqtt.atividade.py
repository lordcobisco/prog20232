import paho.mqtt.client as mqtt
import json
import signal

dados_IMU = "9840"
host = "0.tcp.sa.ngrok.io"
porta = "10618"
arq_salvo = "DadosdoIMU.txt"

def dadosIMU():
    client.publish('cmd2dev9840', '{"op":1,"simulationTime":3,"frequence":20,"sensorType":2}')

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("newdev")
    client.subscribe("dev9840ss")
    dadosIMU()

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload.decode("utf8")))
    # msg = json.loads(msg.payload)
    if msg.topic == ("dev" + dados_IMU + "ss"):
        with open(arq_salvo,'a') as arquivo:
            arquivo.write(msg.payload.decode("utf8") +"\n")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("0.tcp.sa.ngrok.io", 10618, 60)
client.loop_forever()