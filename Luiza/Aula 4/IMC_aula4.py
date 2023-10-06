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

#ATUALIZAÇÃO - FUNÇÕES
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 17:
        return "Estou muito abaixo do peso"
    elif 17 <= imc < 18.5:
        return "Estou abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Estou dentro do peso normal"
    elif 25 <= imc < 30:
        return "Estou acima do peso normal"
    else:
        return "Estou muito acima do peso normal"
def main():
    peso = float(input('Digite o seu peso (kg): '))
    altura = float(input('Digite a sua altura (m): '))
    imc = calcular_imc(peso, altura)
    print("Seu IMC é:", imc)
    classificacao = classificar_imc(imc)
    print(classificacao)

if __name__ == "__main__":
    main()
