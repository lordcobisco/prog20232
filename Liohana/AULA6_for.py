###Comando de repetição: for

n = [89127,1298, 902, 3097, 325, 8589, 123]

soma = 0
for contador in range(len(n)):
    soma += n[contador]
print(soma)

###Exemplo de Coleta de Dados

tempExperimento = 1 #s
freq = 10 #Hz
nDados = tempExperimento*freq

dado = []

for contador in range(nDados):
    dado.append(float(input()))

soma = 0
for data in dado:
     soma = soma + (1/freq) * data
print(soma)


###Dicionário

dicionario = {
            "BR": [1,2,2,1,4,5,3],
            "USA": [3,4,56,3,6,4,2]
             }

for pais in dicionario:
    print(pais)
    print(dicionario[pais])

