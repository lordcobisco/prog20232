#Este programa simula a entrada de parâmetros de configuração de um microscópio confocal de varredura laser, como a simulação de entrada de dados.

#@author: Ana Paula

tipo_celula = 'sanguinea'
zoom = 2
abertura = 1.0
rotacao = 0
laser = 488
resolucao = "alta"
filtro = 15
campo = "claro"


print("Esse programa tem como objetivo configurar o microscopio confocal de varredura a laser")

celula_desejada = int(input("Informe a celula desejada:"))
print("Houve alteração na variável desejada?",tipo_celula!=celula_desejada)
zoom_desejado = int(input("Informe o zoom desejado:"))
print("Houve alteração na variável desejada?",zoom!=zoom_desejado)
abertura_desejado = input("Informe a abertura desejada")
print("Houve alteração na variável desejada?",abertura!=abertura_desejado)
rotacao_desejado = input("Informe a rotacao desejado")
print("Houve alteração na variável desejada?",rotacao!=rotacao_desejado)
laser_desejada = input("Informe o laser desejada")
print("Houve alteração na variável desejada?",laser!=laser_desejada)
resolucao_desejado = int(input("Informe a resolucao desejado"))
print("Houve alteração na variável desejada?",resolucao!=resolucao_desejado)
filtro_desejada = input("Informe o filtro desejado")
print("Houve alteração na variável desejada?",filtro!=filtro_desejada)
campo_desejado = input("informe qual campo deseja utilizar")
print("Houve alteração na variável desejada?",campo!=campo_desejado)

print("“As informações de configurações setadas pelo usuário são:")
print("Célula",celula_desejada)
print("Zoom",zoom_desejado)
print("Abertura",abertura_desejado)
print("Rotação",rotacao_desejado)
print("Laser",laser_desejada)
print("Resolução",resolucao_desejado)
print("Filtro",filtro_desejada)
print("Campo",campo_desejado)

inicial_do_usuario = input("Digite a primeira letra do seu nome para a calibração na horizontal")
print("Caracter digitado é:",inicial_do_usuario)
ultima_letra = input("Digite a última letra do seu nome para a calibração na horizontal")
print("Caracter digitado é:",ultima_letra)

segunda_letra = input("Digite a segunda letra do seu nome para a calibração na vertical")
print("Caracter digitado é:",segunda_letra)
penultima_letra = input("Digite a penultima letra do seu nome para a calibração na vertical")
print("Caracter digitado é:",penultima_letra)

Inicial_horizontal = inicial_do_usuario
Ultima_horizontal = ultima_letra

segunda_vertical = segunda_letra
penultima_vertical = penultima_letra

print("Houve alguma alteração?",Inicial_horizontal)
print("Houve alguma alteração",Ultima_horizontal)
print("Houve alguma alteração",segunda_vertical)
print("Houve alguma alteração",penultima_vertical)


print("A calibração do sistema foi finalizada com sucesso")