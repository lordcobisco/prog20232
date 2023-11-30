# aprendendo a usar listas

lista = ["Giovanna", 24, 1.59, ["psicóloga", "mestranda"]] # cria a lista e define seus valores

# print(lista[1]) # mostra o valor na posição 1

# lista[3] = 51 # altera valores da lista

print(lista[0:2]) # os dois pontos servem para selecionar uma faixa, "a partir do 0 (primeiro número), acesse até antes do 2 (segundo número)"

print(lista[0 : len(lista) : 2]) # até o tamanho da lista, de 2 em 2 - vai pular um 

# verificando a existência de itens em uma lista
print ("Giovanna" in lista) # retorna true
print ("peixe" in lista) # retorna false
