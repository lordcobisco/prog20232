listateste = [1,2,3]
lista = ["oi", 13, ["lista", 1], listateste, 11, 25]
print(lista[0])
lista[0] = "oioioi"
print(lista[0: len(lista) : 2]) #valor do 2 em 2 
#print(lista)
#lista[3] = "adicionar"
#print(lista[3])
tupla = (1,2,3)
print (tupla)
print (tupla[:1]) #fatiamento

dicionario = {
    'professores': ['andré'],
    'alunos': ['ap']
    }

dicionario["ap"] = 123
print (dicionario)
