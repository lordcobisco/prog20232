# Apresentar na tela apenas o IMC e a faixa na qual o operador se encaixa

peso = float(input("digite o seu peso (kg): "))
altura = float(input("digite a sua altura em  (m): "))
imc = peso/(altura**2)
print("seu IMC É", imc)

# Como forma de estrutura de decisão
if( imc < 17):
    print ("estou muito abaixo do peso!")
elif( imc>=17 and imc < 18.5):    
    print("estou abaixo do peso!")
elif(imc >18.5 and imc < 25):
    print("estou com o peso dentro do normal!")
elif(imc>25 and imc < 30):
    print("estou acima do peso!")
else:
    print("estou muito acima do peso!")
