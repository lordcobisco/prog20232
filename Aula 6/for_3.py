tempoExperimento = 1 #s
frequenciaSensor = 10 #Hz
qtdDados = tempoExperimento*frequenciaSensor
#coleta
dado = []
for contador in range (qtdDados):
    dado.append(float(input()))
