tempoExperimento = 1 #S
frequenciaSensor = 10 #Hz
quantidadedeDados = tempoExperimento*frequenciaSensor
# coleta
dado = []
for contador in range(quantidadedeDados) :
    dado.append(float(input()))

print(dado)