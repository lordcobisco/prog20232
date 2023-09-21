# Problema?
# Experimento com?
# Coleta e processamento

#Experimento qualquer:

#dados (entrada e saída)
#tempo?

# Definindo uma função (memória)
def ColetarDados(tempExperimento, frequencia):
    """
    Esta função foi feita para coletar dados
    """
    nDados = tempExperimento*frequencia
    #coleta
    dados = []
    for contador in range(nDados):
        dados.append(float(input()))
    return dados

#Processamento
def integrar(dado, frequencia):
    """
    Esta função foi feita para processar os dados coletados
    """
    soma = 0
    for data in dado:
        soma = soma + (1/frequencia)*data
    return soma

#Coletar os dados e processá-los

tempo = 1
freq = 10
#dados = ColetarDados(tempo, freq)
#processamento = integrar(ColetarDados(tempo, freq), freq)

print(integrar(ColetarDados(tempo, freq), freq))
