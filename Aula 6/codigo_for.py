# tempoExperimento = 1  # s
# frequenciaSensor = 10  # Hz
# qtdDados = tempoExperimento * frequenciaSensor
# # coleta
# dado = []
# for contador in range(qtdDados):
#     dado.append(float(input()))

# # dado = [89127, 1298, 902, 3097, 356]
# soma = 0
# # for contador in range(len(dado)):
# #     soma = soma + (1 / frequenciaSensor) * dado[contador]
# for data in dado:
#     soma = soma + (1 / frequenciaSensor) * data
# print(soma)

dicionario = {"Brasil": [1, 2, 2, 1, 4, 5, 3], "EUA": [3, 4, 56, 3, 6, 4, 2]}
for pais in dicionario:
    print(pais)
    print(dicionario[pais])
