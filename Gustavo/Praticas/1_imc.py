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
