#itens A e B
resolucao, emitdo, n_imagens = 10, 512, 1
celula, reagente, nome = "a", "a", "aaaa"
primeira_letra, segunda_letra, ultima_letra, penultima_letra = "a", 'a', 'a', 'a'
mudou_0, mudou_1, mudou_2, mudou_3, mudou_4 = False, False, False, False, False

#item c
print('Esse programa tem como objetivo receber dados para ')

#itens D e E
print("Por favor, insira as seguintes informações:")
resolucao = int(input("Resolução da imagem, em DPI: "))
mudou_0 = input("Houve alteração na variável inserida? Insira 1 para verdadeiro: ")=='1'
print(f"É {mudou_0} que o conteúdo da variável inserida é: {resolucao}")
celula = input("Tipo de célula a ser analisada: ")
mudou_1 = input("Houve alteração na variável inserida? Insira 1 para verdadeiro: ")=='1'
print(f"É {mudou_1} que o conteúdo da variável inserida é: {celula}")
emitido = int(input("Comprimento de onda da luz emitida: "))
mudou_2 = input("Houve alteração na variável inserida? Insira 1 para verdadeiro: ")=='1'
print(f"É {mudou_2} que o conteúdo da variável inserida é: {emitdo}")
reagente = input("Insira o reagente da solução: ")
mudou_3 = input("Houve alteração na variável inserida? Insira 1 para verdadeiro: ")=='1'
print(f"É {mudou_3} que o conteúdo da variável inserida é: {reagente}")
n_imagens = int(input("Insira quantas imagens você quer que tenha: "))
mudou_4 = input("Houve alteração na variável inserida? Insira 1 para verdadeiro: ")=='1'
print(f"É {mudou_3} que o conteúdo da variável inserida é: {n_imagens}")

#item f
print("As informações de calibração foram a seguintes:")
print(f"Resolução: {resolucao} DPI. Mudanças: {mudou_0}")
print(f"Tipo de celula: {celula}. Mudanças: {mudou_1}")
print(f"Comprimento de onda emitido: {emitido} nm. Mudanças: {mudou_2}")
print(f"Reagente: {reagente}. Mudanças: {mudou_3}")
print(f"Nº de imagens: {n_imagens}. Mudança: {mudou_4}")

#item g
nome = input('Por favor, insira o seu nome (caso o nome tenha menos de 4 letras\
             então insira o sobrenome): ')
print("Calibração horizontal")
primeira_letra = input("Insira 10x a primeira letra do seu nome:\n")
ultima_letra = input("Insira 10x a ultima letra do seu nome:\n")

#item h
print(f"Sua entrada {primeira_letra} corresponte a {nome[0]*10}:\n {primeira_letra==(nome[0]*10)}\n")
print(f"Sua entrada {ultima_letra} corresponte a {nome[-1]*10}:\n {ultima_letra==(nome[-1]*10)}")

#item i
print("Calibração vertical")
segunda_letra = input("Insira 10x a segunda letra do seu nome:\n")
penultima_letra = input("Insira 10x a penultima letra do seu nome:\n")

#item j
print(f"Sua entrada {segunda_letra} corresponte a {nome[1]*10}:\n {segunda_letra==(nome[1]*10)}\n")
print(f"Sua entrada {penultima_letra} corresponte a {nome[-2]*10}:\n {penultima_letra==(nome[-2]*10)}")

#item k
print("----------------------------------")
print("Calibração concluída")
print("----------------------------------")
