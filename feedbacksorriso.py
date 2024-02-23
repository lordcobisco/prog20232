import paho.mqtt.client as mqtt
import cv2
import numpy as np

host_mqtt = "0.tcp.sa.ngrok.io"
porta_mqtt = 14277

def on_connect(client, userdata, flags, rc):
    print("Connect with result code " + str(rc))
    client.subscribe("newdev")
    client.subscribe("dev9840ss")

smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

def detect_smiles(image, client):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    smiles = smile_cascade.detectMultiScale(gray, scaleFactor=1.8, minNeighbors=20)
    for (x, y, w, h) in smiles:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    if len(smiles) > 0 and client is not None:
        print("Continue sorrindo para receber a eletroestimulação!")
        client.publish('cmd2dev3632',
            '{"op":2,"m":0,0,1,0",' +
            '{"op":2,"m":0,0,0,0",' +
            '"t":200,"p":20000}')
    elif client is not None:
        print("Sorriso não detectado!")
        client.publish('cmd2dev3632',
            '{"op":2,"m":0,0,0,0",' +
            '"t":200,"p":20000}')

def detect_smiles_realtime(client):
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()

        detect_smiles(frame, client)

        cv2.imshow('Smile Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.on_connect = on_connect
client.connect(host_mqtt, porta_mqtt, 60)

client.loop_start()

detect_smiles_realtime(client)
