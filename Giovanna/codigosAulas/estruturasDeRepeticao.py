# aqui vc encontra: range, repetição com for e listas

for i in range(5):
    print(i) # retorna de 0 a 4

for item in range(10, 110, +10): # parâmetros de range: start (onde começa), stop (onde para), step (intervalo)
    print(item)

for caractere in "Giovanna":
    print(caractere)

lista = ['Giovanna', 'Vítor', 'José']

for item in lista: 
    print(item)

# duas formas de fazer a mesma coisa - retornar todos os itens da lista: 

linguagens = ['Pyhton', 'PHP', 'C#', 'PowerBuilder', 'Cobol']
tamanho = len(linguagens) # retorna quantos itens tem a lista
indices = range(tamanho)

for i in indices:
    print(linguagens[i]) 

for linguagem in linguagens:
    print(linguagem)

for key, value in enumerate(['p', 'y', 't', 'h', 'o', 'n']):
    print(key, value)

for i, valor in enumerate(linguagens):
    print('Linguagem: ' + valor)
    print('Índice: ' + str(i))