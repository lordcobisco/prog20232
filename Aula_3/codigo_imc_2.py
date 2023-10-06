peso = float(input('digite o seu peso (kg)'))
altura = float(input('digite a sua altura (m)'))
imc=peso/altura**2

if (imc < 17):
    print ("estou muito abaixo do peso")
if (imc >= 17 and imc < 18.5):
    print ("Abaixo do peso")
if (imc >= 18.5 and imc < 25.0):
    print ("EStou com o peso dentro do normal")
if(imc >= 25.0 and imc <30.0):
    print ("Acima do peso normal")
if (imc > 30.0):
    print("MUito acima do peso")
    
