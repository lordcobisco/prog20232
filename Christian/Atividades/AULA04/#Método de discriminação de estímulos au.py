#Método de discriminação de estímulos auditivos para primatas atráves do condicionamento operante

#Habituação
print("Bem vindo ao programa de Habituação!")
Legenda= print("SIM digite 1 NÃO digite 2")
habituacao=int(input("O animal está habituado?: "))
if habituacao == 1:
    print("Animal habituado")
#Aproximação
aproximação=float(input("Distancia animal: "))
if aproximação < 30:
    agua=0,5
    print("Agua liberada 0,5ml")
toque_barra=int(input("Toques na barra: "))
if toque_barra == 20:
    print("Experimento passou para próxima etapa")
else:
    print("Faltam toques",20-toque_barra,"para a próxima etapa")
som1=input(("Som 1 foi emitido: SIM digite 1 NÃO digite 2: "))
som2=input("Som 2 foi emitido: SIM digite 1 NÃO digite 2: ")
if som1 and som2 != 1:
    print("Agua liberada 0,5 ml")
numero_experimento=int(input("Quantas vezes o experimento foi realizado: "))
tempo=int(input("Em quanto tempo? Digite em minutos: "))

if numero_experimento > 49 and tempo > 29:
    print("Experimento passou para próxima fase")