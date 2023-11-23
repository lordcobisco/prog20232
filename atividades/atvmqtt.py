import paho.mqtt.client as mqtt
import csv

arq = 'dadosACC.txt'

with open(arq, 'w') as arquivos:
    arquivos.write('Dados do IMU')

def dataImu(client):
    imu_data = {"op": 1, "simulationtime": 3, "frequence": "20", "sensortype": 2}
    client.publish('cm2dev1488', str(imu_data))

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("newdev")
    dataImu(client)

def on_message(client, userdata, msg):
    data = msg.payload.decode("utf-8")
    with open(arq, 'a') as arquivos:
        arquivos.write(data + "\n")
    save_to_csv(msg.payload)

def save_to_csv(data):
    with open(arq, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([data.decode('utf-8')])

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("10.1.0.18", 1883, 60)
client.loop_forever()
