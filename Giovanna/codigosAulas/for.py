dado = [89127, 1298, 902, 3097, 356]

soma = dado[0]+dado[1]+dado[2]+dado[3] # trabalho de corno 
print(soma)

soma = 0
for contador in range(len(dado)):
    soma += dado[contador]
print(soma)

soma = 0 
for d in dado: 
    soma += d
print(soma)