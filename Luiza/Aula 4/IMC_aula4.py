peso = float(input('Digite o seu peso (kg):'))
altura = float(input('Digite a sua altura (m):'))
IMC = peso/(altura**2)
print(IMC)
print("Seu IMC é", IMC )
if IMC<17:
      print("Estou muito abaixo do peso?")
elif IMC >= 17 and IMC <18.5:
      print("Estou abaixo do peso?")
elif IMC < 18.5:
    print("Estou abaixo do peso?" )
else:
     print("imc normal")

# print("Estou muito abaixo do peso?" , IMC<17 )
# print("Estou abaixo do peso?" , IMC>=17 and IMC < 18.5)   #ou podemos escrever assim
# print("Estou muito abaixo do peso?" , 17 <= IMC < 18.5)
# print("Estou dentro do peso normal?" , IMC>=18.5 and IMC < 25)
# print("Estou acima do peso normal?" , IMC>=25 and IMC <30)
# print("Estou muito acima do peso normal?" , IMC < 30)
