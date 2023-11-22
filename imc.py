#comentario em python começa com ########## e não com ////
print("Este programa calculo o IMC")
peso = float(input("digite o peso (kg): "))
altura = float(input("digite a altura (m): "))

imc = (peso/(altura**2))

print("olá Matheus, seu IMC é ", imc) 
if( imc <17.0):
    print("você está muito abaixo do peso")
elif(imc >= 17.0 and imc< 18.5):
    print("você está abaixo do peso")
elif(18.0 <= imc < 25.0):    
    print(" você está dentro do peso normal")
elif( 25.0 <= imc < 30.0):
    print(" você está acima do peso")
else:
    print("você está muito acima do peso, CUIDADO!!!")