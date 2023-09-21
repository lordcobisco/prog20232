#Problema experimento com 
#coleta e processamento

#Dados (entrada e saída)
#Tempo?

  #tempoExperimento=1 #s
  #frequenciaSensor=10 #Hz
def coletarDados (tempoExperimento,frequenciaSensor):
        """"
        Esta função foi feita para coletar dados de um sensor
        """
        qtdDados= tempoExperimento * frequenciaSensor 
#coleta
        dado =[]
        for contador in range (qtdDados):
            dado.append(float(input()))
        return dado
def integrar(dado,frequenciaSensor):
    soma=0
    for data in dado:   
         soma = soma + (1/frequenciaSensor)*data 
    print(soma)
    return soma

tempo=1
freq=1
integral=integrar(dado=coletarDados(tempo,freq), freq)

processar={"int":integrar}
processar["int"](coletarDados(tempo,freq), freq)
