#Objetos/variáveis#

#import microscope #fingindo um dataset pra fazer acontecer
luz = [True] #sensor 
laser = [0] #nm (comprimento de onda em nanometro)
objetiva = [0] #objetiva/magnificação 10x 40x 100x...
lamina_posicionada = [True] 
macro = [] #atrelado a um sensor no equipamento
micro = [] #atrelado a um sensor no equipamento
resolucao = [0.2, 0.5] #um (micrometros)
celltype = [0]
fitc = [490] #nm
alexa = [488] #nm
filtro = [0]
calhori1 = []
calhori2 = []
calverti = []


print("Esse programa objetiva receber dados para obtenção de imagens por microscopia confocal.")
print("Selecione as configurações iniciais.")

objetiva = [int(input("Objetiva(10, 40, 100):"))]
print("Houve alteração na variável inserida?", objetiva != [0] )

laser = [int(input("Comprimento de onda do laser (nm):"))]
print("Houve alteração na variável inserida?", laser != [0] )

celltype = [str(input("Tipo celular:"))]
print("Houve alteração na variável inserida?", celltype != [0] )

filtro = [float(input("Filtro (fitc-490, alexa-488):"))]
print("Houve alteração na variável inserida?", filtro != [0] )

print(f"As informações definidas foram = objetiva:{objetiva}, laser:{laser}, tipo celular:{celltype}, filtro:{filtro}.")

print("Agora será realizada a calibração...")

print("Para calibração horizontal pressione a primeira letra do seu nome 10x.")
calhori1 = [str(input())]
calhori1.append(str(input()))
calhori1.append(str(input()))
calhori1.append(str(input()))
calhori1.append(str(input()))
calhori1.append(str(input()))
calhori1.append(str(input()))
calhori1.append(str(input()))
calhori1.append(str(input()))
calhori1.append(str(input()))
if (len(calhori1) == 10):
  print(f"Calibração horizontal 1 finalizada, caracteres digitados:{calhori1}")
else:
  print("Atenção: Preencha novamente!")

print("Para calibração horizontal pressione a última letra do seu nome 10x.")
calhori2 = [str(input())]
calhori2.append(str(input()))
calhori2.append(str(input()))
calhori2.append(str(input()))
calhori2.append(str(input()))
calhori2.append(str(input()))
calhori2.append(str(input()))
calhori2.append(str(input()))
calhori2.append(str(input()))
calhori2.append(str(input()))
if (len(calhori2) == 10):
  print(f"Calibração horizontal 2 finalizada, caracteres digitados:{calhori2}")
else:
  print("Atenção: Preencha novamente!")

print("Para calibração vertical pressione a segunda letra do seu nome 10x.")
calverti1 = [str(input())]
calverti1.append(str(input()))
calverti1.append(str(input()))
calverti1.append(str(input()))
calverti1.append(str(input()))
calverti1.append(str(input()))
calverti1.append(str(input()))
calverti1.append(str(input()))
calverti1.append(str(input()))
calverti1.append(str(input()))
if (len(calverti1) == 10):
  print(f"Calibração vertical 1 finalizada, caracteres digitados:{calverti1}")
else:
  print("Atenção: Preencha novamente!")

print("Para calibração vertical pressione a penúltima letra do seu nome 10x.")
calverti2 = [str(input())]
calverti2.append(str(input()))
calverti2.append(str(input()))
calverti2.append(str(input()))
calverti2.append(str(input()))
calverti2.append(str(input()))
calverti2.append(str(input()))
calverti2.append(str(input()))
calverti2.append(str(input()))
calverti2.append(str(input()))
if (len(calverti2) == 10):
  print(f"Calibração vertical 2 finalizada, caracteres digitados:{calverti2}")
else:
  print("Atenção: Preencha novamente!")

if (calhori1, calhori2, calverti1, calverti2 == 10, 10, 10, 10):
  print("Calibração conclúida com sucesso!")
