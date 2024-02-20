import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    if reason_code == 0:
        print("Connected to broker")
        global Connected
        Connected = True
    else:
        print("Connection failed")

def on_message(client, userdata, msg):
    print("Message received: "  + str(msg.payload))

Connected = False

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

broker_address = "10.1.0.18"
broker_port = 1883
client.connect(broker_address, broker_port, keepalive=60)

# Inicie o loop para manter a conexão e processar eventos
client.loop_forever()
