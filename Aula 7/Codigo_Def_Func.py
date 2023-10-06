# Problema experimento com
# coleta e processamento

# dados (entrada e saída)
# tempo?
tempoExperimento = 1  #s
frequenciaSensor = 10 #Hz

'''
Esta função foi feita para coletar dados baseados na frequencia do sensor
'''
def coletarDados():

    dadosEx1 = coletarDados (1, 1)
    dadosEx2 = coletarDados (1, 2)
    dadosEx3 = coletarDados (1, 10)

dado = [89127, 1298, 902, 3097, 356]
soma = dado [0] + dado [1] + dado [2] + dado [3]
soma = 0
for contador in range (len (dado)):
    soma = soma + (1 / frequenciaSensor) * dado [contador]
print (soma)

def coletarDados(tempoExperimento, frequenciaSensor):
    qtDados = tempoExperimento*frequenciaSensor 
    # coleta
    dado = []
    for contador in range (qtDados):
        dado.append(float(input()))
    return dado

def integrar (dado,frequenciaSensor):
    soma = 0
    for data in dado:
        soma = soma + (1/ frequenciaSensor)
    return soma

tempo = 1
freq = 1
dadosEx1 = coletarDados(1,10)
integral = integrar (dado= coletarDados(tempo,freq),
                    frequenciaSensor=freq)


processar = {int (integrar)}
processar (coletarDados (tempo, freq), freq)
