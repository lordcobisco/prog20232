
# Import the necessary libraries
import paho.mqtt.client as mqtt
import json

# Open the file 'data.txt' in write mode and write the header
file = open('data.txt', 'w')
file.write('IMU1,IMU2,IMU3,GYRO1,GYRO2,GYRO3,ACC1,ACC2,ACC3\n')
file.close()

# Define callback functions for MQTT events

# This function is called when the client successfully connects to the MQTT broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribe to the topics 'newdev' and 'dev9840ss'
    client.subscribe("newdev")
    client.subscribe("dev9840ss")
    # Publish a message to the topic 'cmd2dev9840' to start the data collection
    client.publish('cmd2dev9840',
                   '{"op":1,"simulationTime": 10,'+
                   '"frequence": 20,'+ 
                   '"sensorType": 0}')

# This function is called when a message is received from the MQTT broker
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    # If the message is received from the topic 'dev9840ss', append the payload to the file 'data.txt'
    if msg.topic == 'dev9840ss':
        with open('data.txt', 'a') as file:
            file.write(msg.payload.decode('utf-8')+'\n')

# This function is called when the client is disconnected from the MQTT broker
def on_disconnect(client, userdata, rc):
    print("Disconnected with result code " + str(rc))

# This function sends a command to stop data collection and disconnects the client from the MQTT broker
def stop_receiving(client):
    client.publish('cmd2dev9840',
                   '{"op":22}')
    client.disconnect()
    print("Encerrado")

# Create an MQTT client instance
client = mqtt.Client()

# Set the callback functions
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

# Set the MQTT broker address and port
broker_address = "0.tcp.sa.ngrok.io"
broker_port = 10618

# Connect to the MQTT broker
client.connect(broker_address, broker_port, 60)

# Start the MQTT network loop
client.loop_start()

# Infinite loop to keep the program running until 'a' is entered
while True:
    if input() == 'a':
        stop_receiving(client)
        break
    
