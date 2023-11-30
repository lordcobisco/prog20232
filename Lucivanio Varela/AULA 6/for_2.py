dado = [89127, 1298, 902, 3097,356]

soma = dado[0] + dado[1] + dado[2] + dado[3] 
soma = 0
for contador in range(len(dado)) : #não precisa mudar aqui com o "len" so precisa mudar o dado la em cima que foi acrescentar o 356
    soma += dado [contador] # o que esta abaixo do "for" vai se repetir 
print(soma)