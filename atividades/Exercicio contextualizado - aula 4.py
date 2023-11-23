# Método de discriminação de estímulos auditivos para primatas.
 
print('Vamos iniciar o Treinamento')
animal = input('Digite o tipo de Animal que será testado: ')
print("Coloque o %s na Caixa de Habituação" %(animal))
grupo = input('Iniciaremos a Habituação, INFORME o grupo de Animal: ')
print("Esse animal pertence ao Grupo %s," %(grupo))

print('vamos começar')

barraEsquerda = int(input("O Animal apertou o batão 1?\n"))
barraDireita = int(input("O Animal apertou o batão 2?\n"))

som1 = input("musica baixa")
som1 = input("musica alta")

Primeira_etapa = input(int("20"))
for i in range(1,Primeira_etapa):
    Primeira_etapa - i
    
if (barraDireita and som1):
	print("Foram adicionados 0,5ml de água")
else: 
	print("Nada foi Acionado!")
 
if (barraEsquerda and som2):
	print("Foram adicionados 0,5ml de água")
else: 
	print("Nada foi Acionado!")

print("Fim da 1ª Habituação. O Animal realizou 20 Tentativas")

Segunda_etapa = input(int("50"))
for i in range(1,Segunda_etapa):
    Segunda_etapa - i
    
if (barraDireita and som1):
	print("Foram adicionados 0,5ml de água")
else: 
	print("Nada foi Acionado!")
 
if (barraEsquerda and som2):
	print("Foram adicionados 0,5ml de água")
else: 
	print("Nada foi Acionado!")

print("Fim da 2ª Habituação. O Animal realizou 50 Tentativas")

print("Fim do Experimento")