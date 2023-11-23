import paho.mqtt.client as mqtt
import json


nome_arquivo = open('dadosSensor.txt', 'w') #isso cria o arquivo, para escrita 

# Função para adicionar dados ao arquivo
def adicionar_dados_ao_arquivo(payload):
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write(payload + '\n')

#arquivo.write('Dados do Sensor a frequencia x, ...') #Não é aqui. Tem que colocoar em outro local do código. -> pra salvar no código tenho que pegar o payload 

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("newdev")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    # msg = json.loads(msg.payload)

    # Adicionar dados ao arquivo quando uma mensagem é recebida
    adicionar_dados_ao_arquivo(msg.payload.decode('utf-8'))

    client.publish("cmd2dev1488", '{"op":2,"m":"0,0,1,0","t":"200","p":"20000","f":"0"}')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("10.1.0.18", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

#O que tem que fazer é ler informações do sensor inercial e salvar 
#COmo salvar informações? - manipulação de arquivos (aula 8) -> biblioteca pandas ou 
#Open o arquivo e dps write 