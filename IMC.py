# Calculando o IMC

peso = float(input("Digite o seu peso em Kg"))
altura = float(input("Digite a sua altura em cm"))

IMC = peso/altura**2

if IMC < 18.5:
  print("Você está abaixo do peso ideal")
elif IMC >= 18.5 and IMC < 24.9:
  print("Você está com o peso ideal")
elif IMC >= 24.9 and IMC < 29.9:
  print("Você está acima do peso ideal")
else:
  print("Você está muito acima do peso ideal")
