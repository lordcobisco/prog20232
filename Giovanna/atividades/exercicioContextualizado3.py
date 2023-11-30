resolucaoImagem = 1
tipoCelula = 1
tipoSensor = 1

print("Esse programa tem como objetivo receber dados para configurar o uso de Microscópio confocal de varredura a laser. \n As seguir serão apresentadas as configurações padrões e você poderá fazer as alterações necesssárias. \n Todas as informações aqui inseridas são códigos que devem ser consultados no manual de instrução para as opções desejadas.")

print("Resolução da imagem: ", resolucaoImagem, "\n Houve alteração nessa variável? Digite a nova informação. Senão, digite a opção padrão acima.")
novaResolucaoImagem = int(input())
print(novaResolucaoImagem == resolucaoImagem)
resolucaoImagem = novaResolucaoImagem

print("Tipo de célula: ", tipoCelula, "\n Houve alteração nessa variável? Digite a nova informação. Senão, digite a opção padrão acima.")
novoTipoCelula = int(input())
print(novoTipoCelula == tipoCelula)
tipoCelula = novoTipoCelula

print("Tipo de sensor: ", tipoSensor, "\n Houve alteração nessa variável? Digite a nova informação. Senão, digite a opção padrão acima.")
novotipoSensor = int(input())
print(novotipoSensor == tipoSensor)
tipoSensor = novotipoSensor

print(
    "As informações de configuração escolhidas pelo usuário são:\n", 
    "Resolução da imagem: ", resolucaoImagem, "\n",
    "Tipo de célula: ", tipoCelula, "\n",
    "Tipo de sensor: ", tipoSensor, "\n"
)

print("Vamos iniciar a calibração do equipamento.")

print("Aperte 10x a tecla que corresponde à primeira letra do seu nome")
calibracao1 = input()
calibracao1 = input()
calibracao1 = input()
calibracao1 = input()
calibracao1 = input()
calibracao1 = input()
calibracao1 = input()
calibracao1 = input()
calibracao1 = input()
calibracao1 = input()
print("A informação foi corretamente digitada: ", calibracao1)

print("Aperte 10x a tecla que corresponde à última letra do seu nome")
calibracao2 = input()
calibracao2 = input()
calibracao2 = input()
calibracao2 = input()
calibracao2 = input()
calibracao2 = input()
calibracao2 = input()
calibracao2 = input()
calibracao2 = input()
calibracao2 = input()
print("A informação foi corretamente digitada: ", calibracao2)

print("Aperte 10x a tecla que corresponde à segunda letra do seu nome")
calibracao3 = input()
calibracao3 = input()
calibracao3 = input()
calibracao3 = input()
calibracao3 = input()
calibracao3 = input()
calibracao3 = input()
calibracao3 = input()
calibracao3 = input()
calibracao3 = input()
print("A informação foi corretamente digitada: ", calibracao3)

print("Aperte 10x a tecla que corresponde à penúltima letra do seu nome")
calibracao4 = input()
calibracao4 = input()
calibracao4 = input()
calibracao4 = input()
calibracao4 = input()
calibracao4 = input()
calibracao4 = input()
calibracao4 = input()
calibracao4 = input()
calibracao4 = input()
print("A informação foi corretamente digitada: ", calibracao4)

print("A calibração foi realizada com sucesso.")