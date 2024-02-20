# Importa a biblioteca 'os' para operações relacionadas ao sistema operacional
import os

# Importa a biblioteca 'paho.mqtt.client' para trabalhar com MQTT
import paho.mqtt.client as mqtt

# Define o número desejado de mensagens antes de parar
num_messages_to_receive = 10
received_messages_count = 0

# Specify the folder path
folder_path = 'C:/Users/ariog/OneDrive/Documentos/Python Scripts'

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Connected successfully")
        client.subscribe("newdev")
        client.subscribe("dev9840ss")
    else:
        print(f"Connection failed with code {reason_code}")

def on_message(client, userdata, msg):
    global received_messages_count
    received_messages_count += 1

    print(f"Received message from {msg.topic}: {msg.payload.decode('utf8')}")

    client.publish('cmd2dev9840', '{"op":1,"simulationTime":"2","frequence":"2","sensorType":2}')

    if msg.topic == "dev9840ss":
        file_path = os.path.join(folder_path, 'dados.txt')
        
        with open(file_path, 'a') as f:
            f.write(msg.payload.decode('utf-8'))

    if received_messages_count >= num_messages_to_receive:
        print(f"Received {num_messages_to_receive} messages. Stopping execution.")
        client.disconnect()  # Desconecta o cliente MQTT


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

broker_address = "10.1.0.18"
broker_port = 1883
client.connect(broker_address, broker_port, keepalive=60)

# Inicie o loop para manter a conexão e processar eventos
client.loop_forever()