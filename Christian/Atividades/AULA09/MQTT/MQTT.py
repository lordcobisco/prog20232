import paho.mqtt.client as mqtt
import json
import csv

dados= "dadossensor.txt"
with open(dados,'w') as arquivo:
    arquivo.write("teste,\n")

Dispositivo = "9840"

mqtt_host = "0.tcp.sa.ngrok.io"
mqtt_port = 10618

def send_imu_init():
    msg2send = {'op':1}
    msg2send['simulationTime'] = 3
    msg2send['frequence'] = 20
    print('requestIMUStream:', "cmd2dev"+Dispositivo)
    client.publish("cmd2dev"+Dispositivo,json.dumps(msg2send))
   
    if msg2send['simulationTime'] == 0:
        send_imu_stop()
        
 
# O callback para quando o cliente recebe uma resposta CONNACK do servidor.
def on_connect(client, userdata, flags, rc):
    print("Conectado com o código de resultado " + str(rc))

    client.subscribe("newdev")
    client.subscribe("dev"+Dispositivo+"ss")
    client.subscribe("dev"+Dispositivo+"status")
    
    send_imu_init()
    

# O callback para quando uma mensagem PUBLISH é recebida do servidor.
def on_message(client, userdata, msg):
    print(msg.topic,": ",msg.payload.decode('utf8'))
    if msg.topic == "dev9840ss":
        with open(dados,'a') as arquivo:
            arquivo.write(msg.payload.decode('utf8')+"\n")


 

def on_connect_fail(client, userdata, msg):
     print("Connect failed")
     client.connect("0.tcp.sa.ngrok.io",10618, 600)


def send_imu_stop():
    imu_stop_operation = {"op": 22}
    client.publish("cmd2dev"+Dispositivo, json.dumps(imu_stop_operation))
    print("Stop")
 

# Configuração do cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Conectar ao servidor MQTT
client.connect(mqtt_host, mqtt_port, 60)
# Iniciar o loop para continuar recebendo mensagens

client.loop_forever()