#Automatização do Procedimento Cirúrgico no Exteriotáx

anestesia = {
    "Ketamina": ["10 mg/kg"],
    "Xilazina": ["100 mg/kg"],
    "KetaminaXilazina": ["50 mg/kg"],
    "HalotanoGasoso": ["200 mg/kg"]
}

#entradas:
#input("Informações da máquina: ")
#input("Posicionamento do rato: ")

#EtapaI
print("Na etapa I o animal deve ser devidamente cedado.")
farmaco1 = anestesia[input("Informe qual fármaco será administrado: ")]
print("Essa é a dosagem correta: ", farmaco1)

#EtapaII
print("Na etapa II o animal deve ser posicionado no estereotáxico.")
print("Posicione o animal, fazendo com que as barras que suportam o seu corpo estejam no ouvido externo do animal.")
piscar = (input("O animal deu uma leve piscada após o estímulo dessa musculatura?"))
if piscar == "sim":
    print("Ótimo. Agora vamos analisar a angulação da cabeça do animal.")
    bregma = input("Qual a angulação do bregma?")
    lambd = input("Qual a angulação do lambda?")
    if bregma == lambd:
        print("Temos uma superfície de cirurgia plana.")
    else:
        print("O animal não está corretamente posicionado.")
else:
    print("Posicione corretamente o animal.")

#EtapaIII
print("Na etapa III: Limpeza do campo de trabalho. Será necessário o cumprimento de algumas etapas:")
print("Inicialmente, retire a pelagem que recobre a parte superior da calota craniana.")
CalotaCraniana = input("A pelagem que recobre a parte superior da calota craniana foi retirada?")
if CalotaCraniana == "sim":
    print("Em seguida, retire os tecidos moles (epiderme, derme e tecido conjuntivo).")
    TecidosMoles = input("A parte óssea da caixa craniana foi alcançada?")
    if TecidosMoles == "sim":
        print("Após essas retiradas, limpe a calota craniana de qualquer resto de “pele” que esteja sobrando utilizando H2O2 - 10 volumes.")
        Limpeza = input("O área foi devidamente higienizada?")

#EtapaIV
if CalotaCraniana == "sim" and TecidosMoles == "sim" and  Limpeza == "sim":
    print("Com o animal em posição e com o campo cirúrgico devidamente limpo, utilize uma pequena camada de poliacrilato em todo o perímetro externo para evitar sangramentos.")

#EtapaV
print("Nessa etapa deve-se escolher um ponto para a fixação de parafusos.")
AnteroPosterior = input("Meça com a régua o posicionamento da águlha no AnteroPosterior e insira o valor na célula:")
LateroLateral = input("Meça com a régua o posicionamento da águlha no LateroLateral e insira o valor na célula:")
DorsoVentral = input("Meça com a régua o posicionamento da águlha no DorsoVentral e insira o valor na célula:")

AP = 0,42 #Estruturas do núcelo
LL = 0,3
DV = 0,2 

PosicaoAP = AnteroPosterior - AP
PosicaoLL = LateroLateral - LL
PosicaoDV = DorsoVentral - DV

posicao = (PosicaoAP, PosicaoLL, PosicaoDV)

print("Esses foram os valores encontrados: ", posicao)

#EtapaVI
