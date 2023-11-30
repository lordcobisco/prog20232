tempoExperimento = 1 #s
frequenciaSensor = 10 #Hz 
qtdDados = tempoExperimento * frequenciaSensor

# coleta 
dados = []
for contador in range(qtdDados):
    dados.append(float(input()))

soma = 0 
# linguagem de baixo nível
# for contador in range(len(dado)):
#     soma = soma + (1 / frequenciaSensor) * dado[contador]
# print(soma)

# forma mais fácil de fazer 
for dado in dados: 
    soma = soma + (1 / frequenciaSensor) * dado
print(soma)

