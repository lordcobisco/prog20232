distanciap = [30] #cm padrao
distancia = []
recompensa = [0.5] #volume em ml da recompensa
toquebarra = [int()] #sensor para contabilizar toques na barra pelo animal
tempo = 30 #cronometro que contabiliza automaticamente a duração dos testes (em min)
numtrial = [] #número da trial que está sendo realizada máx 50

habituacao = str((input("O animal está habituado? (True ou False)")))

if habituacao == "True":
  print("Iniciar treinamento.")
  numtrial = int(input("Qual o número da trial que está sendo realizada? (Máx. 50)"))
  distancia = [float(input("Qual a distância do animal da região de interesse?"))]
  toquebarra = int(input("Quantas vezes o animal tocou na barra? (somente número)"))
else:
  print("ATENÇÃO: animal não habituado!")

if distancia < distanciap and toquebarra >= 20:
  print("O animal passou para a próxima etapa!")
  print("Verifque o som reproduzido e a direção tomada pelo animal.")
  ladotoque = str(input("Em que barra o animal tocou, direita ou esquerda?"))  #lado em que o animal tocou na barra (direita ou esquerda)
  som = str(input("Qual o som reproduzido, som1 ou som2?"))
elif distancia < distanciap:
  print(f"O animal receberá uma recompensa de {recompensa} mL")
else:
  print("Reinicie o experimento.")

if som == "som1" and ladotoque == "esquerda":
  print(f"O animal receberá uma recompensa de {recompensa} mL")
elif som == 'som2' and ladotoque == "direita":
  print(f"O animal receberá uma recompensa de {recompensa} mL")
else:
  print("Repetir experimento.")

print("Resultado:")

if numtrial == 50 and tempo == 30:
  print("O animal passou para a próxima fase!")
else:
   print("Rever experimento.")
