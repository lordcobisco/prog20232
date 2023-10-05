#AtividadeContextualizada4

#a)
habituado = False
tempo_habituacao = 60 #s

tempo_habituacao = int(input("Qual tempo o animal passou dentro da caixa na última habituação? (em segundos)"))
if tempo_habituacao >= 60:
  habituado = True
else:
  habituado = False

#b)
aproximacao = 30 #cm
aproximacao = int(input("Qual a distância do animal até a barra?"))
if aproximacao <= 30:
  print("Liberado 0,5ml de recompensa")
else:
  pass

pressao_barra = 1
pressao_barra = int(input("Quantas vezes o animal pressionou a barra?"))
if pressao_barra >= 20:
  print("Experimento passou para a próxima etapa.")
else:
  pass

som1 = 1
som2 = 2
tocou_barra_direita = "direita"
tocou_barra_esquerda = "esquerda"

som = int(input("Qual som tocou? 1 ou 2?"))
qual_barra = input("Qual barra o animal tocou? direita ou esquerda?")
if som==som1 and qual_barra==tocou_barra_esquerda:
  print("Liberado 0,5ml de recompensa")
else:
  pass

som = int(input("Qual som tocou? 1 ou 2?"))
qual_barra = input("Qual barra o animal tocou? direita ou esquerda?")
if som==som2 and qual_barra==tocou_barra_direita:
  print("Liberado 0,5ml de recompensa")
else:
  pass


quant_vezes = 2
tempo_exp = 5 #min
quant_vezes = int(input("Quantas vezes o experimento foi realizado?"))
tempo_exp = int(input("Há quanto tempo o experimento está sendo realizado? (em minutos)"))
if quant_vezes == 50 and tempo_exp <= 30:
                  print("O experimento seguirá para a próxima fase.")
else:
  print("Continue o treino")