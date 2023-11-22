import paho.mqtt.client as mqtt

dados = 'dadosSensor.txt'
with open(dados, 'w') as arquivo:
    # Escreve no arquivo
    arquivo.write('Simulation Time: 3, Frequence: 20, Dados do IMU\n')

def requestIMUStream():
    client.publish('cmd2dev9840','{"op":1,"simulationTime":"3",'+
                    '"frequence":20,"sensorType":2}')
def stopIMU():
    client.publish('dev9840ss',{'op':22})

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # client.subscribe("newdev")
    client.subscribe("dev9840ss")
    client.subscribe("dev9840status")
    requestIMUStream()

def on_message(client, userdata, msg):
    print(msg.topic,": ",msg.payload.decode('utf8'))
    if msg.topic == "dev9840ss":
        with open(dados, 'a') as arquivo:
            arquivo.write(msg.payload.decode('utf8')+'\n')

    # arquivo.write(dados)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect('10.1.0.18', 1883, 60)
client.loop_forever()