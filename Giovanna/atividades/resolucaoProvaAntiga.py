
finalizar_programa = False
# definindo as variáveis
sinal_estimulacao = []
# parâmetos de estimulação 
corrente = 0.5 
tensao = 10 
tempo = 1
frequencia = 10 
qtde_dados = tempo * frequencia

# variáveis dos sensores 
freq_aquisicao_eeg = 2
tempo_aquisicao_eeg = 1
qtde_dados_eeg = freq_aquisicao_eeg * tempo_aquisicao_eeg
banda_filtro_eeg = [20, 100]
dados_eeg = []

freq_aquisicao_ecg = 2 
tempo_aquisicao_ecg = 1
qtde_dados_ecg = freq_aquisicao_ecg * tempo_aquisicao_ecg
banda_filtro_ecg = [100, 200]
dados_ecg = []

while finalizar_programa == False: 

    print("Essa intervenção tem como objetivo aliviar os sintomas da depressão. Será feita uma estimulação transcraniana.")
    print("Escolha uma das três opções de intervenção:")
    tipo_intervencao = int(input("Digite o número referente ao tipo de intervenção:\n 1. Leve \n 2. Moderado \n 3. Grave"))
    if tipo_intervencao == 1: 
        print("Para casos leves, indicamos corrente = 1, tensão = 2, tempo = 3 e frequencia = 4")
    elif tipo_intervencao == 2: 
        print("Para casos moderados, indicamos corrente = 5, tensão = 6, tempo = 7 e frequencia = 8")
    elif tipo_intervencao == 3: 
        print("Para casos graves, indicamos corrente = 9, tensão = 10, tempo = 11 e frequencia = 12")

    # recebendo parâmetros
    corrente = float(input("Informe o valor de corrente desejado: "))
    tensao = float(input("Informe o valor de tensao desejado: "))
    tempo = float(input("Informe o tempo desejado: "))
    frequencia = int(input("Informe a frequencia desejada: "))

    print("Os parâmetros definidos foram: \n Corrente = ", corrente, "\n Tensão = ", tensao, "\n Tempo = ", tempo, "\n Frequência: ", frequencia)
    input("Digite qualquer coisa para iniciar a terapia")

    print("Iniciando a terapia...") # essa parte eu não entendi o que é pra enviar, então só simulei um valor qualquer
    for contador in range(qtde_dados):
        sinal_estimulacao.append(corrente*tensao*contador)
    print(sinal_estimulacao)

    print("Recebendo dados do EEG")
    for contador in range(qtde_dados_eeg):
        dados_eeg.append(float(input()))

    print("Recendo dados do ECG")
    for contador in range(qtde_dados_ecg):
        dados_ecg.append(float(input()))

    # Calculando índices 
    max_eeg = max(dados_eeg)
    min_eeg = min(dados_eeg)
    max_ecg = max(dados_ecg)
    min_ecg = min(dados_ecg)
    soma_eeg = sum(dados_eeg)
    soma_ecg = sum(dados_ecg)

    indices_coleta = (
        max_ecg, max_eeg, min_eeg, min_ecg, soma_eeg, soma_ecg
    )

    nome = input("Digite o nome do paciente: ")

    informacoes_paciente = {
        "Nome": nome,
        "Dados_Estimulo": sinal_estimulacao,
        "Dados_eeg": dados_eeg,
        "Dados_ecg": dados_ecg, 
        "Indices": indices_coleta
    }

    print(informacoes_paciente)

    finalizar_programa = input("Você deseja finalizar o programa? Escreva True para SIM e False para NÃO: ")
