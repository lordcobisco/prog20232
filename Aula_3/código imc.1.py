#calcular imc

peso = 84
altura = 1.65

imc = peso/(altura**2)

# calculo de forma sequenciada
print("Estou muito abaixo do peso? ", imc < 17)
print("Estou abaixo do peso? ", imc >= 17 and imc < 18.5)
print("Estou dentro do peso? ", 18.5 <= imc <= 25)
print("Estou acima do peso? ", imc > 25 and imc <= 30)
print("Estou muito acima do peso? ", imc > 30)
