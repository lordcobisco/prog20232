#funções e classes

#dados (entrada e saída)
tempoExperimento = 1 #s
frequenciaSensor = 10 #Hz

dado=[123,456,789]
soma=dado[0]+dado[1]+dado[2]
soma=0

for contador in range(len(dado)):
    soma=(1/frequenciaSensor)*dado[contador]
print(soma)

def coletarDados(tempoExperimento, frequenciaSensor):
    qtDados = tempoExperimento*frequenciaSensor
    #coleta
    dado=[]
    for contador in range(qtDados):
        dado.append(input())
    return dado

dadosEx1 = coletarDados(1,1)
dadosEx2 = coletarDados(1,2)
dadosEx3 = coletarDados(1,10)
print(dadosEx2)