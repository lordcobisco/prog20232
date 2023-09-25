# informacaoDOteclado = int(input()) #conversão explicita do input em int
# print(informacaoDOteclado*3)

#calcular IMC
peso=float(input("Digite seu peso:"))
altura=float(input("Digite sua altura:"))
imc=peso/(altura*altura)
print("Seu IMC é:" , imc)

if imc < 17:
    print("Muito abaixo do peso")
elif 17<imc<18.5:
    print("Abaixo do peso normal")
elif 18.5<imc<25.0:
    print("Peso dentro do normal")
elif 25.0<imc<30.0:
    print("Acima do peso normal")
else: print("Muito acima do peso")
