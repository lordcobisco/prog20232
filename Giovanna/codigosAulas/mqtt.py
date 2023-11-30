import paho.mqtt.client as mqtt
import json
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("newdev")
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload)) # msg.topic é o e-mail de origem e msg.payload é o conteúdo
    # msg = json.loads('{"DOIT Esp32 DevKit v1"}')
    client.publish('cmd2dev1488', '{"op":2,"m":"0,0,100,0","t":"200","p":"20000","f":"0"}')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("10.1.0.18", 1883, 60) # endereço do servidor 
client.loop_forever()