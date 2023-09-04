'''
Turma: 2023.2
Professor: Andre Dantas
Aluno: Gustavo Maciel

Atividade: 2
Aula: 3

Inclua no exercício de IMC uma atualização:
Requisito:
    Fazer o calculo do IMC
    Classificar a partir do resultado
    Receber o IMC utilizando a função input
'''

peso = input("Qual o seu peso?")
altura = input("Qual a sua altura?")

imc = (float(peso)/(float(altura) ** 2))


print("Seu IMC é ", imc) 
if( imc <17.0):
    print(" você está muito abaixo do peso")
elif(imc >= 17.0 and imc< 18.5):
    print(" você está abaixo do peso")
elif(imc >= 18.0 and imc < 25.0):    
    print(" você está dentro do peso normal")
elif(imc >= 25.0 and imc < 30.0):
    print(" você está acima do peso")
else:
    print("você está muito acima do peso, CUIDADO!!!")
