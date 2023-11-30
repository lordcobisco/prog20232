peso = float (input('Digite o seu peso (kg): '))
altura = float (input('Digite a sua altura (m): '))
imc = peso/(altura**2)
print ("Seu IMC é: ", imc)

if imc < 17:
    print ('Estou muito abaixo do peso!')
elif imc >= 17 and imc < 18.5:
    print ('Estou abaixo do peso normal!')
elif 18.5 <= imc < 25:
    print (' Estou com o peso dentro do normal!')
elif 25 <= imc < 30:
    print ('Estou acima do peso normal!')
else:
    print ('Estou muito acima do peso normal!')