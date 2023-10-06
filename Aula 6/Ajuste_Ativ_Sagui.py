#Atividade Habituação
#Ajuste da atividade Método de discriminação de estímulos auditivos para primatas através do condicionamento operante
#Adaptação do problema para utilizar funções, principalmente os trechos de código dentro das estruturas de repetição.
#Variaveis

posicao = [30] #cm padrao
posicao = []
recompensa = [0.5] #volume em ml da recompensa
toquebarra = [int()] #sensor para contabilizar toques na barra pelo animal
tempo = 30 #cronometro que contabiliza automaticamente a duração dos testes (em min)
numtrial = [] #número da trial que está sendo realizada máx 50

def habituacao ():
 habituacao = ((input("O animal está habituado? (True ou False)")))
if habituacao == "True":
  print("Habituacao satisfatoria!. Iniciar treinamento.")
  return True
else:
  print("O animal precisa se habituar ao ambiente.")
  habituacao == "False"
  return False

#Regime de aproximações sucessivas
def aproximacoes_sucessivas():
if habituacao == True
    print ("Com relação a aproximação, o animal deve se aproximar a uma distância igual ou maior que 30cm")
if posicao < posicao and toquebarra >= 20:
  print("O animal passou para a próxima etapa!")
if aproximacao < 30:
  print (print("O animal receberá uma recompensa de 0,5 mL"))
  aproximacao == True
  return True

def toquebarra = int(input("Quantas vezes o animal tocou na barra? (somente número)"))
if toques >= 20:
    return input ("O animal está habituado para a proxima etapa.")
else:
  print("ATENÇÃO: animal não habituado, não passa para próxima etapa!")

  numtrial = int(input("Qual o número da trial que está sendo realizada? (Máx. 50)"))

  
def Som1 = input("O som1 foi ativado?")

def Som1 = True
if som1 == 
  Som1Emitido = input("Qual som foi emitido? Digite som 1 ou som 2.")
     if Som1Emitido == "som 1":
          print("O som 1 foi emitido.")
    print("Liberar 0,5 ml de rec.")
else:
    print("Não liberar nada.")

def BarraEsquerda = input("O animal tocou na barra esquerda?")
 BarraEsquerda = True
  if BarraTocada == input("O animal tocou em qual barra? Digite esquerda ou direita: ")
  if BarraTocada == "esquerda":
    print("Liberar 0,5ml de recompensa")

def Som2 = True
if som1=2 == 
  Som2Emitido = input("Qual som foi emitido? Digite som 1 ou som 2.")
     if Som2Emitido == "som 2":
          print("O som 2 foi emitido.")
    print("Liberar 0,5 ml de rec.")
else:
    print("Não liberar nada.")

def BarraDireita = input("O animal tocou na barra esquerda?")
 BarraDireita = True
  if BarraTocada == input("O animal tocou em qual barra? Digite esquerda ou direita: ")
  if BarraTocada == "direita":
    print("Liberar 0,5ml de recompensa")
  else: print ("Não libere a recompensa.")

# Chama as funções 
if realizar_habituacao():
    if aproximacoes_sucessivas():
        if tocar_barra():
            emitir_som("O som 1 foi emitido ao toque do animal na barra esquerda?")
            emitir_som("O som 2 foi emitido ao toque do animal na barra direita?")

# Se o experimento foi realizado 50x em 30min, apresentar que o experimento seguirá para a próxima fase.
TempoDeExperimento=True
if TempoDeExperimento: igual a 30min
if numtrial: 50x 
if numtrial == 50 and tempo == 30: True
  print("O animal passou para a próxima fase!")
else:
   print("Rever experimento e continuar na etapa de aproximações sucessivas.")
