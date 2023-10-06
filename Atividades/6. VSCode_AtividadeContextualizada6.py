print("Vamos iniciar o programa de cirurgia extereotáxica animal")

peso_animal = int(input("Digite o peso do animal em kg"))

dose_ketamina = peso_animal * 60 #mg
dose_xilasina = peso_animal * 10 #mg

doses_medicamentos = {
    "Ketamina": dose_ketamina,
    "Xilasina": dose_xilasina
                      }

print("Animal anestesiado")
print("Animal sendo posicionado no aparelho extereotáxico")

piscada_de_olho = "não"
while piscada_de_olho != "sim": 
  piscada_de_olho = input("O animal piscou o olho?")
  print("Posicionando novamente")

angulação = 1
while angulação != 0:
  print("Verificando angulação da cabeça")
  angulação = int(input("Qual a angulação da cabeça?"))
  
print("Animal posicionado corretamente")

print("Retirando pelagem que recobre a calota craniana")

alcancou_osso = "não"
while alcancou_osso != "sim":
  alcancou_osso = input("Alcançou o osso?")
  print("Retirando os tecidos moles (epiderme, derme e tecido conjuntivo)")

print("Limpando calota craniana com H2O2")

print("Colocando camada de poliacrilato")

ponto_parafuso = input("Qual o ponto de fixação do parafuso?")


voltas_parafuso = 0
while voltas_parafuso < 3:
  voltas_parafuso = int(input("Quantas voltas deu o parafuso?"))
  print("Fixando parafuso no ponto", ponto_parafuso)

if voltas_parafuso >= 3:
  print("Parar!")
else:
  pass

AP = int(input("Qual o valor do AnteroPosterior? (mm)"))
LL = int(input("Qual o valor do LateroLateral? (mm)"))
DV = int(input("Qual o valor do DorsoVentral? (mm)"))

AP = AP - 0.42 
LL_direita = LL - 0.3 
LL_esquerda = LL + 0.3
DV = DV - 0.2 

coordenadas = (AP, LL_direita, LL_esquerda, DV)

hemisferio = input("Em qual hemisfério vai iniciar?")
print("Iniciando inserção das cânula-guia no hemisfério", hemisferio)
if hemisferio == "esquerdo":
  print("Fazer inserção LL:", LL_esquerda)
elif hemisferio == "direito":
  print("Fazer inserção LL:", LL_direita) 
else:
  print("Comando inválido")

print("Perfurando a 45º")

print("Introduzindo cânula-guia, DV:", DV)
print("Utilizando rolos de papel absorvente para drenar o sangue")

print("Misturando acrílico com solvente")
textura = []
while "espessa" and "maleável" not in textura: 
  print("Continue misturando.")
  textura = input("Qual a textura da mistura?")

if hemisferio == "direito":
  print("Introduzindo cânula no hemisfério esquerdo, DV:", DV)
elif hemisfério == "esquerdo":
  print("Introduzindo cânula no hemisfério direito, DV:", DV)
else:
  pass

print("Utilizando rolos de papel absorvente para drenar o sangue")

print("Misturando acrílico com solvente")
textura = []
while "espessa" and "maleável" not in textura: 
  print("Continue misturando.")
  textura = input("Qual a textura da mistura?")

print("Levantando animal devagar e acomodando na caixa")
animal_despertou = "não"
while animal_despertou != "sim":
  animal_despertou = input("O animal despertou?")
print("Colocando animal na caixa-moradia")
  
