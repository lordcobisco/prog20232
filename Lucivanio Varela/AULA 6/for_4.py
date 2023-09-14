tempoExperimento = 1 #S
frequenciaSensor = 10 #Hz
quantidadedeDados = tempoExperimento*frequenciaSensor
# coleta
dado = []
for contador in range(quantidadedeDados) :
    dado.append(float(input()))



#dado = [89127, 1298, 902, 3097,356]

soma = dado[0] + dado[1] + dado[2] + dado[3] 
soma = 0
for contador in range(len(dado)) : # (o "len" tamanho do vetor, é quantas vezes eu vou repetir ex: frequenciaSensor = 10 #Hz  )
    soma = soma + (1 / frequenciaSensor) * dado[contador] # esse "1 / frequenciaSensor" é a integral ( está somando todos os numeros)
print(soma)

print(len(dado))