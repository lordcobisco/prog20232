import paho.mqtt.client as mqtt
import json
import csv

dispositivo_IMU = "9840"
host="0.tcp.sa.ngrok.io"
porta = 10618
arquivo_salvo = "exercicio_mqtt.txt"

def on_connect (client, userdata, flags, rc):
    print ("connected with result code" + str(rc))
    client.subscribe ("newdev")
    client.subscribe ("dev" + dispositivo_IMU + "ss")
    client.publish( "cmd2dev"+dispositivo_IMU,
                    '{"op":1,"simulationTime": 2,"frequence": 20,"sensorType":2}')
    
def on_message(client, userdate, msg):
    print (msg.topic + " "+ str (msg.payload.decode ("utf8")))

    if msg.topic == ("dev" + dispositivo_IMU + "ss"):
        with open (arquivo_salvo, 'a') as arquivo: 
            arquivo.write(msg.payload.decode ("utf8") + "\n")

# msg = json.liads ('{"device" : "DOIT Esp32 Devkit v1"})

      

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect ("0.tcp.sa.ngrok.io", 10618, 60)
client.loop_forever()




