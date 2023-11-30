dado = [89127, 1298, 902, 3097]

soma = dado[0] + dado[1] + dado[2] + dado[3] # essa soma # (elemento neutro é o 0, sempre começar com o elemento neutro) range (é uma faixa) range é o indice
print (soma)
soma = 0
for contador in range(4) : #(o range é uma forma de variar o numero)
    soma += dado [contador] # o que esta abaixo do "for" vai se repetir 
print(soma)