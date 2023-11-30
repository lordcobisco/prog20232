profundidadeDeCampo = int # em nanômetros
resolucaoImagem = int # em pixels
tipoCelula = str # tipo de célula
faixaIluminacao = int # intensidade da luz
corImagem = str # cor-alvo da imagem

profundidadeDeCampo = 50
resolucaoImagem = 480
tipoCelula = "neuronio"
faixaIluminacao = 8
corImagem = "cinza"

print("Esse programa tem como objetivo receber dados para orientar o microscópio confocal de varredura à laser do IIN-ELS!")

novaProfundidadeDeCampo = input("Qual é a profundidade de campo desejada?: ")
if novaProfundidadeDeCampo == profundidadeDeCampo:
    print("Houve alteração na variável inserida aqui? Não")
else:
    print ("Houve alteração na variável inserida aqui? Sim")

novaResolucaoImagem = input("Qual é a resolução de imagem desejada?: ")
print("")

novoTipoCelula = input("Qual é o tipo de célula a ser registrado?: ")
print("")

novaFaixaIluminacao = input("Qual é a faixa de iluminação desejada?: ")
print("")

novaCorImagem = input("Qual é a cor-alvo?: ")
print("")



print("As informações de configurações setadas pelo usuário são:")
print(novaProfundidadeDeCampo)
print(novaResolucaoImagem) 
print(novoTipoCelula) 
print(novaFaixaIluminacao)
print(novaCorImagem)

calibracaoHorizontal = str(input("Digite a primeira e a última letra do seu nome, cada uma 10 vezes, para calibrar horizontalmente o microscópio: "))
print("A informação foi corretamente digitada com:")
print(calibracaoHorizontal)

calibracaoVertical = str(input("Digite a primeira e a última letra do seu nome, cada uma 10 vezes, para calibrar verticalmente o microscópio: "))
print("A informação foi corretamente digitada com:")
print(calibracaoVertical)


print("Parabéns! O sistema foi calibrado. Agora você pode usar o microscópio à vontade")