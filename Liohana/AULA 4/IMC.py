p = float(input('Qual o seu peso? (Kg)')) #entrada
h = float(input('Qual a sua altura? (m)')) #entrada

IMC = p/(h**2) #operador

print('Esse é o seu ICM: ', round(IMC,2)) #saida

# Utilizando Estruturas de Decisão:

if (IMC < 17):
print('Você está muito abaixo do peso')
if (IMC > 17 and IMC< 18.5):
print('Você está abaixo do peso normal')
if (IMC > 18.5 and IMC < 25):
print('Você está no peso dentro do normal')
if (IMC > 25 and IMC < 30):
print('Você está acima do peso normal')
if (IMC> 30):
print('Você está muito acima do peso normal')
