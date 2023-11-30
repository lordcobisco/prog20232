# Crie as variáveis necessárias para que o programa funcione corretamente.

Caminho_da_luz = "claro"
Laser = 512
Intensidade_da_luz = 30
Abertura = 1.0
Lentes_convergentes = 10
Aumento_lente = 50
Resolucao_da_imagem = "alta"
Quantidade_celulas_por_area = 600
Tipo_celula = "Hemacias"
Zoon = 2

# Frase inicial do programa

print("Esse programa tem como objetivo receber dados para configuração de um microscopio confocal")

# Para cada informação digitada, apresente na tela a seguinte mensagem: “Houve alteração na variável inserida? ”. Após a mensagem, apresentar verdadeiro ou falso com base no que foi digitado pelo usuário e o que estava armazenado na variável. Obs.: Não deve ser utilizado if aqui.

Luz_microscopio = input("O caminho da luz é claro ou esuro?" )
print ("Houve alteração na variável inserida?", Caminho_da_luz != Luz_microscopio )
Laser_microscopio = int(input("qual o valor da intensidade do laser?"))
print ("Houve alteração na variável inserida?", Laser != Laser_microscopio)
Intensidade_da_luz_microscopio = int(input("Qual foi a intensidade da luz?"))
print ("Houve alteração na variável inserida?", Intensidade_da_luz != Intensidade_da_luz_microscopio )
Abertura_microscopio = float(input("qual o tamanho da abertura circular?" ))
print ("Houve alteração na variável inserida?", Abertura != Abertura_microscopio)
Lentes_convergentes_microscopio = int(input("Qual o tamanho da convergência das lentes?"))
print ("Houve alteração na variável inserida?", Lentes_convergentes != Lentes_convergentes_microscopio)
Aumento_lente_microscopio = int(input("De quanto foi o aumento da lente?"))
print ("Houve alteração na variável inserida?", Aumento_lente != Aumento_lente_microscopio)
Resolucao_da_imagem_microscopio = input("A resolução foi alta ou baixa?")
print ("Houve alteração na variável inserida?", Resolucao_da_imagem != Resolucao_da_imagem_microscopio)
Quantidade_celulas_por_area_microscopio = int(input("De quanto foi a quantidade de céluas por área?"))
print ("Houve alteração na variável inserida?", Quantidade_celulas_por_area != Quantidade_celulas_por_area_microscopio)
Tipo_celula_microscopio = input("Qual foi o tipo de célula utilizada?")
print ("Houve alteração na variável inserida?", Tipo_celula!= Tipo_celula_microscopio)
Zoon_microscopio = int(input("De quanto foi o Zoon do microscópio?"))
print ("Houve alteração na variável inserida?", Zoon != Zoon_microscopio)

#Retorne ao usuário de forma organizada as informações que foram digitadas. Ex.: “As informações de configurações setadas pelo usuário são: ...”

print ("As informações de configurações setadas pelo usuário são:")

print ("caminho da luz:", Luz_microscopio )
print ("Valor da intensidade do laser:", Laser_microscopio)
print ("Valor da intensidade da luz:", Intensidade_da_luz_microscopio)
print ("Tamanho da abertura circular:", Abertura_microscopio)
print ("Tamanho da convergência das lentes", Lentes_convergentes_microscopio)
print ("Aumento das lentes:", Aumento_lente_microscopio)
print ("Resolução alta ou baixa:", Resolucao_da_imagem_microscopio)
print ("Quantidade de células por área:", Quantidade_celulas_por_area_microscopio)
print ("Tipo de célula utilizada:", Tipo_celula_microscopio)
print ("Zoon do microscópio:", Zoon_microscopio)

# Após setada as configurações iniciais o usuário deve utilizar dois caracteres para a calibração do equipamento no sentido horizontal. Para isso, ele deve apertar a tecla correspondente à primeira letra do seu nome 10x e à última letra do seu nome 10x.
# Imediatamente após apertar a tecla o programa deve apresentar na tela que a informação foi corretamente digitada e mostrar o caractere pressionado.

print ("##CALIBRAÇÃO HORIZONTAL##")

# 1 - vez
Primeira = input(" Digite a primeira letra do seu nome para calibrar:")
Ultima = input ("Digite a ultima letra do seu nome para calibrar:")
print (" A primeira letra do seu nome é?", Primeira)
print ("A ultima letra do seu nome é?:", Ultima)

# 2 - vez
Primeira_calibração = input ("Digite a primeira letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Primeira == Primeira_calibração, "a letra digitada foi:", Primeira_calibração)
Ultima_calibração = input ("Digite a ultima letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Ultima == Ultima_calibração, "a letra digitada foi", Ultima_calibração)

# 3 - vez
Primeira_calibração = input ("Digite a primeira letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Primeira == Primeira_calibração, "a letra digitada foi:", Primeira_calibração)
Ultima_calibração = input ("Digite a ultima letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Ultima == Ultima_calibração, "a letra digitada foi", Ultima_calibração)

# 4 - vez
Primeira_calibração = input ("Digite a primeira letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Primeira == Primeira_calibração, "a letra digitada foi:", Primeira_calibração)
Ultima_calibração = input ("Digite a ultima letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Ultima == Ultima_calibração, "a letra digitada foi", Ultima_calibração)

# 5 - vez
Primeira_calibração = input ("Digite a primeira letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Primeira == Primeira_calibração, "a letra digitada foi:", Primeira_calibração)
Ultima_calibração = input ("Digite a ultima letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Ultima == Ultima_calibração, "a letra digitada foi", Ultima_calibração)

# 6 - vez
Primeira_calibração = input ("Digite a primeira letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Primeira == Primeira_calibração, "a letra digitada foi:", Primeira_calibração)
Ultima_calibração = input ("Digite a ultima letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Ultima == Ultima_calibração, "a letra digitada foi", Ultima_calibração)

# 7 - vez
Primeira_calibração = input ("Digite a primeira letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Primeira == Primeira_calibração, "a letra digitada foi:", Primeira_calibração)
Ultima_calibração = input ("Digite a ultima letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Ultima == Ultima_calibração, "a letra digitada foi", Ultima_calibração)

# 8 - vez
Primeira_calibração = input ("Digite a primeira letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Primeira == Primeira_calibração, "a letra digitada foi:", Primeira_calibração)
Ultima_calibração = input ("Digite a ultima letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Ultima == Ultima_calibração, "a letra digitada foi", Ultima_calibração)

# 9 - vez
Primeira_calibração = input ("Digite a primeira letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Primeira == Primeira_calibração, "a letra digitada foi:", Primeira_calibração)
Ultima_calibração = input ("Digite a ultima letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Ultima == Ultima_calibração, "a letra digitada foi", Ultima_calibração)

# 10 - vez
Primeira_calibração = input ("Digite a primeira letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Primeira == Primeira_calibração, "a letra digitada foi:", Primeira_calibração)
Ultima_calibração = input ("Digite a ultima letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Ultima == Ultima_calibração, "a letra digitada foi", Ultima_calibração)
print ("CALIBRAÇÃO NO SENTIDO HORIZONTAL CONCLUÍDA")

# Na sequência o usuário deve utilizar dois caracteres para a calibração do equipamento no sentido vertical. Para isso, ele deve apertar a tecla correspondente à segunda letra do seu nome 10x e à penúltima letra do seu nome 10x.
# Imediatamente após apertar a tecla o programa deve apresentar na tela que a informação foi corretamente digitada e mostrar o caractere pressionado.

print ("##CALIBRAÇÃO VERTICAL##")

# 1 - VEZ
Segunda = input(" Digite a Segunda letra do seu nome para calibrar:")
Penultima = input ("Digite a penúltima letra do seu nome para calibrar:")
print (" A Segunda letra do seu nome é?", Segunda)
print ("A Penúltima letra do seu nome é:", Penultima)

# 2 - vez
Segunda_calibração = input ("Digite a segunda letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Segunda == Segunda_calibração, "a letra digitada foi:", Segunda_calibração)
Penultima_calibração = input ("Digite a Penúltima letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Penultima == Penultima_calibração, "a letra digitada foi", Penultima_calibração)

# 3 - vez
Segunda_calibração = input ("Digite a segunda letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Segunda == Segunda_calibração, "a letra digitada foi:", Segunda_calibração)
Penultima_calibração = input ("Digite a Penúltima letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Penultima == Penultima_calibração, "a letra digitada foi", Penultima_calibração)

# 4 - vez
Segunda_calibração = input ("Digite a segunda letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Segunda == Segunda_calibração, "a letra digitada foi:", Segunda_calibração)
Penultima_calibração = input ("Digite a Penúltima letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Penultima == Penultima_calibração, "a letra digitada foi", Penultima_calibração)

# 5 - vez
Segunda_calibração = input ("Digite a segunda letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Segunda == Segunda_calibração, "a letra digitada foi:", Segunda_calibração)
Penultima_calibração = input ("Digite a Penúltima letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Penultima == Penultima_calibração, "a letra digitada foi", Penultima_calibração)

# 6 - vez
Segunda_calibração = input ("Digite a segunda letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Segunda == Segunda_calibração, "a letra digitada foi:", Segunda_calibração)
Penultima_calibração = input ("Digite a Penúltima letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Penultima == Penultima_calibração, "a letra digitada foi", Penultima_calibração)

# 7 - vez
Segunda_calibração = input ("Digite a segunda letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Segunda == Segunda_calibração, "a letra digitada foi:", Segunda_calibração)
Penultima_calibração = input ("Digite a Penúltima letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Penultima == Penultima_calibração, "a letra digitada foi", Penultima_calibração)

# 8 - vez
# Segunda_calibração = input ("Digite a segunda letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Segunda == Segunda_calibração, "a letra digitada foi:", Segunda_calibração)
Penultima_calibração = input ("Digite a Penúltima letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Penultima == Penultima_calibração, "a letra digitada foi", Penultima_calibração)

# 9 - vez
Segunda_calibração = input ("Digite a segunda letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Segunda == Segunda_calibração, "a letra digitada foi:", Segunda_calibração)
Penultima_calibração = input ("Digite a Penúltima letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Penultima == Penultima_calibração, "a letra digitada foi", Penultima_calibração)

# 10 - vez
Segunda_calibração = input ("Digite a segunda letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Segunda == Segunda_calibração, "a letra digitada foi:", Segunda_calibração)
Penultima_calibração = input ("Digite a Penúltima letra do seu nome para calibrar:")
print ("A letra foi digitada corretamente:", Penultima == Penultima_calibração, "a letra digitada foi", Penultima_calibração)
print ("CALIBRAÇÃO NO SENTIDO VERTICAL CONCLUÍDA")

#Finalmente, o programa deverá apresentar na tela que houve o término da calibração do sistema.

print ("# A calibração foi concluída com sucesso #")

