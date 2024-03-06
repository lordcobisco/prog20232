import paho.mqtt.client as mqtt
from pylsl import StreamInlet, resolve_stream
import time
import numpy as np
import pandas as pd

# Definindo os parâmetros MQTT
host_mqtt = "10.1.0.18"
porta_mqtt = 1885

# Initialize lists to store data
all_times = []
all_channels = []

# Funções MQTT para controle de estimulação
def ativar_estimulacao():
    client.publish('cmd2dev1772',
                   '{"op":2,"m":"0,0,1,0",' +
                   '"t":200,"p":20000}')

def desativar_estimulacao():
    client.publish('cmd2dev1772',
                   '{"op":2,"m":"0,0,0,0",' +
                   '"t":200,"p":20000}')

# Callbacks MQTT
def on_connect(client, userdata, flags, rc):
    print("Connect with result code " + str(rc))
    client.subscribe("newdev")
    client.subscribe("dev9840ss")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

    posicao_pri = str(msg.payload).find(',')
    posicao_pro = str(msg.payload).find(',', posicao_pri + 1)
    valor_eeg = float(str(msg.payload)[posicao_pri+1:posicao_pro])

    print(f"Valor no EEG: {valor_eeg}")

    if valor_eeg > 0.93:
        print("Ativou")
        ativar_estimulacao()
        time.sleep(2)
        desativar_estimulacao()
    else:
        print("N Ativou")
        desativar_estimulacao()
    
    if msg.topic == "dev9840ss":
        client.publish("seu_topico_de_saida", msg.payload)

# Inicialização do cliente MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.on_connect = on_connect
client.on_message = on_message
client.connect(host_mqtt, porta_mqtt, 60)

# Inicialização do stream LSL
streams = resolve_stream('name', 'EEG')
inlet = StreamInlet(streams[0])

# Definindo o tempo inicial
start_time = time.time()

# Duração da coleta de dados (em segundos)
collection_duration = 30  # Ajuste conforme necessário

cont = 0

while time.time() - start_time < collection_duration:
    cont += 1
    sample, timestamp = inlet.pull_sample()

    value_at_index_5 = sample[5]

    print(cont)

    if value_at_index_5 > 0.50:
        print("Estimula")
        ativar_estimulacao()
    else:
        print("Não Estimula")
        desativar_estimulacao()

    print(f"Valor no índice 5: {value_at_index_5}")
    print(sample)

    all_times.append(timestamp - start_time)
    all_channels.append(sample)

    time.sleep(3)

# Salvando os dados em um arquivo CSV
columns = [f'c{i}' for i in range(1, len(sample) + 1)]
data = np.column_stack([all_times, np.array(all_channels)])
df = pd.DataFrame(data, columns=['time'] + columns)
df.to_csv("dados_aquisition_1.csv", sep=";", index=False)

client.loop_stop()
client.disconnect()
