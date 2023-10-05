peso = float(input('digite o seu peso (kg):'))
altura = float(input('digite a sua altura (m)'))
imc = peso/(altura**2)
print('seu imc é:', imc)
if imc < 17:
    print('muito abaixo do peso?', imc<17)
elif imc >= 17 :
    print('muito abaixo do peso normal?', imc>=17)
else:
    print('estou acima do peso!')
