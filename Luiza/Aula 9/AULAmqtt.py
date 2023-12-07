import paho.mqtt.client as mqtt
import json
arquivo = open('dadosSensor.txt','w')
arquivo.write('Dados do Sensor a frequencia x,...\n')
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("newdev")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    #msg = json.loads(msg.payload)
    client.publish('cmd2dev1488',
                   '{"op":2,"m":"0,0,1,0",'+
                    '"t":"200", "p":"20000",'+
                    '"f":0"}')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("10.1.0.18", 1883, 60)
client.loop_forever()
