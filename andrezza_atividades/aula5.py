lista=["ai meu deus", 13, 145,"cupom",149]
print(lista) #print lista completa
print(lista[2]) #print um elemento especíico da lista

# pergunta de prova: quando não consegue printar, é pq não tem dados na memória :: não reconheceu a linha por ex.

lista[2] = 51 # modificando o valor de um elemento da lista
print(lista) # print da lista modificada

print(lista[0:len(lista):2]) #print da lista de 0 ao element 2 / len() - retorna length da lista

#perguntando se o elemento ta na lista; retorna true or false
print('13' in lista)




