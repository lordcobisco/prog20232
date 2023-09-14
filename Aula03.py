#

# Função para calcular o IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Função para interpretar o IMC
def interpretar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Sobrepeso"
    elif imc < 34.9:
        return "Obesidade Grau I"
    elif imc < 39.9:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"

# Solicitar ao usuário que insira o peso e a altura
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))

# Calcular o IMC
imc = calcular_imc(peso, altura)

# Interpretar o IMC
classificacao = interpretar_imc(imc)

# Exibir o resultado
print(f"Seu IMC é {imc:.2f}, o que significa que você está na categoria de '{classificacao}'.")