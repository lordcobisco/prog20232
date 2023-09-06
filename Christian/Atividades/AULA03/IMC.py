
p=float(input("Digite o peso:"))
a=float(input("Digite a altura:"))

IMC=p/(a*2)

if IMC <= 17:
    print("Muito abaixo do peso")

elif 17 < IMC < 18.5:
    print("Abaixo do peso")

elif  18.5 < IMC < 25: 
    print("Peso normal")

elif  25 > IMC < 30:
    print("Acima do normal")

else:
    print("Muito acima do peso")





