# PROCEDIMENTO DE ANESTESIA:

# utilizar uma diversidade de fármacos para anestesia os animais, dentre eles Ketamina e xilazina utilizados em conjunto, halotano (gasoso). Verificar a dosagem correta de acordo com o peso dos animais.
farmacos = { "ketamina" : ["70 kg/mg"], "xilazina" : ["80 kg/mg"], "alotano" : ["90 kg/mg"]}

# ETAPA 1 

print("na etapa 1: o roedor será anestesiado")
sedativo = input(" Para essa etapa, qual o sedativo será utilizado?")
farmacos1 = input(farmacos)

# ETAPA 2

print(" etapa 2: posicionamento do roedor no estereotáxico")
print("As barras que suportam o peso do animal devem ser posicionadas no ouvido externo do animal.")
print("Normalmente o animal dá uma pequena piscada, devido ao estímulo da musculatura responsável por este movimento.")

pisc = input("o roedor deu uma piscada quando a musculatura foi estimulada?")

if pisc == "sim":
    print("o roedor piscou, agora vamos fazer a analise da angulação da cabeça")
    Bregma = input("qual é o angulo do Bregma?")
    lamb = input("qual o angulo do lambda?")
    if Bregma == lamb:
        print("superficie plana.")
    else:
        print("posição incorreta.")

# ETAPA 3

print("etapa 3: limpeza do campo de trabalho")
print("Retirada da pelagem que recobre a parte superior da calota craniana")
print(" Retirada dos tecidos moles (epiderme, derme e tecido conjuntivo) até alcançar a parte óssea da caixa craniana.")

Calota_craniana = input(" a calota craniana foi limpa corretamente?")

if Calota_craniana == "sim":
    print("Otimo, passe para a próxima etapa")
else:
    print("limpe a calota craniana de qualquer resto de “pele” que esteja sobrando utilizando H2O2 10 volumes, para passar para próxima etapa.")

# ETAPA 4

Calota_craniana = "sim"

while Calota_craniana:
    craniano = input("Uma camada de poliacrilato foi colocada no perímetro externo para evitar sangramentos?")
    if craniano == "sim":
        print("sangramento evitado.")
        break
    else:
        print("coloque uma camada de poliacrilato para estancar o sangramento")

# ETAPA 5

print(" etapa 5 : Localização do ponto para fixar os parafusos")

AnteroPosterior_AP= float(input("Digite os valores encontrados nas réguas a partir do posicionamento da agulha (AP): "))
LateroLateral_LL = float(input("Digite os valores encontrados nas réguas a partir do posicionamento da agulha (LL): "))
LateroLateral_LL_bilat = float(input("Digite os valores encontrados nas réguas a partir do posicionamento da agulha (LL): "))
DorsoVentral_DV = float(input("Digite os valores encontrados nas réguas a partir do posicionamento da agulha (DV): "))

AP = 0.42 
LL = 0.30
LL_bilat = 0.30
DV = 0.20

posições = [AnteroPosterior_AP - AP, LateroLateral_LL + LL, LateroLateral_LL_bilat - LL_bilat, DorsoVentral_DV - DV]
print("os valores fora:", posições)

# ETAPA 6

hemisferio = input("Em qual dos hemisférios você colocará a primeira cânula?")
print("Você deverá localizar os pontos de inserção conforme a indicação a seguir: ")
print("AnteroPosterior_AP", posições[0])
print("LateroLateral_LL", posições[1], " ", posições[2])
print("DorsoVentral_DV", posições[3])

# ETAPA 7

print("etapa 7 : apoie a mão que segura a broca contra o assoalho ou ao estereotáxico e perfure o crânio a +- 45 graus de angulação.")

angulacao = float(input("Qual inclinação da sua mão?"))

if(angulacao > 0 and angulacao < 40):
     print("A angulacão não está ideal")
elif(angulacao >= 40 and angulacao <= 50):
     print(" continue as perfurações")
else:
     print("A angulacão está acima do ideal")

# ETAPA 8 

print("Agora que a perfuração foi feita, insira a  cânula-guia até ", posições[3])

# ETAPA 9 

sangramento = input("Está sangrando ou saindo liquido cefalorraquidiano?")
if(sangramento):
    print("Utilize rolos de papel para limpar")

# ETAPA 10

print("etapa 10: elaboração do capacete rigido")

textura = "sim"

while textura:
    tex = input("A mistura do acrílico polimerizante com o solvente está com a textura espessa?")
    if tex == "sim":
        print("aplique a mistura na região com cuidado para que não escorra. Abarque o crânio, a cânula-guia e o parafuso.")
        
        break
    else:
        print("leva-lo ate sua caixa-moradia.")


# ETAPA 11

print(" ETAPA 11: Fixação de uma outra cânula. posicionar a agulha sobre o outro ponto de inserção da cânula-guia. Introduzir a cânula-guia até o valor:", posições[3])


# ETAPA 12

sangramento = int(input("Está sangrando ou saindo liquido cefalorraquidiano?"))

if(sangramento):
    print("Utilize rolos de papel para limpar")
    print("Agora que já inseriu a cânula, é hora de espalhar um pouco mais do cimento criado do produto entre o solvente e acrilato")

textura = input("A mistura do acrílico polimerizante com o solvente está com a textura espessa?")

while(textura != 1):
    print("Continue misturando")
    textura = input("textura no ponto?")
    print("Agora aplique a mistura na região com cuidado para que não escorra. Abarque o crânio, a cânula-guia e o parafuso.")

# Etapa 13

print("Levante o roedor cuidadosamente e coloque-o em uma caixa aquecida")

outros_roedores = "sim"

while outros_roedores:
    roedores = input("Os outros roedores estão dormindo?")
    if roedores == "sim":
        print("leva-lo ate sua caixa-moradia.")
        break
    else:
        print("esperar os outros roedores se acalmarem")

