#a e b)
ligar1 = False
tipo_amostra1 = "tecido"
resolucao_espacial1 = 50 #micrômetros
comprimento_onda1 = 400 #nanômetros
tipo_contraste1 = "fluorescência"
objetiva1 = 40 #x
poder_resolucao_lateral1 = 30 #micrômetros
poder_resolucao_axial1 = 30 #micrômetros
tamanho_pinhole1 = 3 #micrômetros
taxa_varredura1 = 10 #Hz
tempo_varredura1 = 5 #segundos

#c)
print("Este programa tem como objetivo integrar imagens em alta resolução em microscopia")

#d) e e)
tipo_amostra2 = input("Digite o tipo da amostra: 'célula biológica', 'tecido' ou 'material semicondutor'")
print("Houve alteração na variável inserida?", tipo_amostra1!=tipo_amostra2)
resolucao_espacial2 = float(input("Qual a resolução espacial, em micrômetros?"))
print("Houve alteração na variável inserida?", resolucao_espacial1!=resolucao_espacial2)
comprimento_onda2 = int(input("Qual o comprimento de onda, em nanômetros?"))
print("Houve alteração na variável inserida?", comprimento_onda1!=comprimento_onda2)
tipo_contraste2 = input("Qual o tipo de contraste? 'fluorescência', 'contraste de fase' ou 'DIC (Differential Interference Contrast)'")
print("Houve alteração na variável inserida?", tipo_contraste1!=tipo_contraste2)
objetiva2 = int(input("Qual a objetiva? 2.5x, 5x, 10x, 25x, 40x ou 65x? Digite apenas o número"))
print("Houve alteração na variável inserida?", objetiva1!=objetiva2)
poder_resolucao_lateral2 = float(input("Qual o poder de resolução lateral, em micrômetros?"))
print("Houve alteração na variável inserida?", poder_resolucao_lateral1!=poder_resolucao_lateral2)
poder_resolucao_axial2 = float(input("Qual o poder de resolução axial, em micrômetros?"))
print("Houve alteração na variável inserida?", poder_resolucao_axial1!=poder_resolucao_axial2)
tamanho_pinhole2 = float(input("Qual o tamanho do pinhole, em micrômetros?"))
print("Houve alteração na variável inserida?", tamanho_pinhole1!=tamanho_pinhole2)
taxa_varredura2 = int(input("Qual será a taxa de varredura? (Em Hz)"))
print("Houve alteração na variável inserida?", taxa_varredura1!=taxa_varredura2)
tempo_varredura2 = int(input("Qual será o tempo de varredura? (Em segundos)"))
print("Houve alteração na variável inserida?", tempo_varredura1!=tempo_varredura2)

#f)
print("As informações de configuração setadas pelo usuário são:")
print("Tipo da amostra:", tipo_amostra2)
print("Resolução espacial:", resolucao_espacial2)
print("Comprimento de onda:", comprimento_onda2)
print("Tipo de contraste:", tipo_contraste2)
print("Objetiva:", objetiva2)
print("Poder de resolução lateral:", poder_resolucao_lateral2)
print("Poder de resolução axial:", poder_resolucao_axial2)
print("Tamanho pinhole:", tamanho_pinhole2)
print("Taxa de varredura:", taxa_varredura2)
print("Tempo de varredura:", tempo_varredura2)

#g) e h)
calib_horiz = input("Para calibrar o equipamento no sentido horizontal, tecle a letra 'i' 10x  e a letra 'd' 10x ")
print("A informação foi corretamente digitada:", calib_horiz=='iiiiiiiiiidddddddddd', calib_horiz)

#i) e j)
calib_vert = input("Para calibrar o equipamento no sentido vertical, tecle a letra 'n' 10x  e a letra 'i' 10x ")
print("A informação foi corretamente digitada:", calib_vert=='nnnnnnnnnniiiiiiiiii', calib_vert)

#k)
print("Fim da calibração do sistema.")