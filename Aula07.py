#Coleta e processamento
#Atividade de funcoesEclasses

# dados (entrada e saída)
# tempo?
#tempo_experimento = 1 # s
#frequencia_experimento = 10 #Hz
def coletar_dados(tempo_experimento, frequencia_sensor):
    """
    Essa função foi realizada para coletar dados de um sensor
    """
    qtdDados = tempo_experimento * frequencia_sensor
    #coleta
    dado = []
    for contador in range(qtdDados):
        dado.append(float(input()))
    return dado #Memória do def ao dado

def integrar(dado, frequencia_sensor):
    soma = 0
    for data in dado:
        soma = soma(1/ frequencia_sensor) * data
    return soma #Memória ao def integrar

#dado = coletar_dados (1, 10)
#Processamento: a execução começa aqui. Executado o que está dentro da sequẽncia

tempo = 1
freq = 1
dadosEx1 = coletar_dados(1, 1)
# dadosEx1 = coletar_dados (tempo, freq)
# integral = integrar(dadosEx1, freq) # o processamento está acontecendo
integral = integrar(dado = coletar_dados(tempo,freq))
                # frequencia_sensor = freq
processar = {"int": integrar}

