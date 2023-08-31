compras = ['chocolate', 'pizza', 'refri']
lista = ['liohana', 1, 6.9, compras]

print(lista)

i=0
while (i < 4):          #comando de repetição p/ ver todos os elementos da lista
    print(lista[i])
    i = i+1

print(lista[3][1]) #vizualizar lista dentro da lista

lista[3][1] = 'lasanha'  #substituir elementos em uma lista

print(lista[2:4])  #definir janelas em uma lista

print(lista[0:len(lista):2])  #ler toda a lista do zero até o fim de 2 em 2
