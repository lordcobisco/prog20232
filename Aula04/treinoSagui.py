#DUAS ESCOLHAS aleatoria com  REPETIÇÃO
import random

# Defina os sons e suas respostas 
sons = {"phee": "e", "trill": "d"}

def reproduzir_som():
    # Simula a reprodução de um som, escolhendo aleatoriamente entre "phee" e "trill"
    som = "trill"
  
    return som

def treinamento():
   
    while escolha != d:

        som = reproduzir_som()
        resposta_correta = som
       
        #Macaco escolhe a alavanca e - esuqerda ou d - direita
        escolha = input(f"Som reproduzido: {som}. Escolha esquerda (e) ou direita (d): ")

        if escolha == resposta_correta:
            print("Escolha correta! Recebe 0.5 de rec.")
            break
        else:
            print("Escolha incorreta. A luz da caixa é apagada por 5 segundos.")
            som = reproduzir_som()
            #chama novamente a funcao treinamento, até acertar
            treinamento()

##################################################################

#DUAS ESCOLHAS aleatoria sem  REPETIÇÃO
import random

# Defina os sons e suas respostas 
sons = {"phee": "e", "trill": "d"}

def reproduzir_som():
    # Simula a reprodução de um som, escolhendo aleatoriamente entre "phee" e "trill"
    som =  random.choice(["phee", "trill"])
    somfixo = random.choice(["phee", "trill"])
    return som

def treinamento():
   
    while tentativas < 60:
        acertos = 0
        erros =0
        tentativas = 0
        som = reproduzir_som()
        resposta_correta = som
       
        #Macaco escolhe a alavanca e - esuqerda ou d - direita
        escolha = input(f"Som reproduzido: {som}. Escolha esquerda (e) ou direita (d): ")
        tentativas = tentativas + 1
        if escolha == resposta_correta:
            print("Escolha correta! Recebe 0.5 de rec.")
            acertos = acertos + 1
            break
        else:
            print("Escolha incorreta. A luz da caixa é apagada por 5 segundos.")
             erros = erros + 1
            #chama novamente a funcao treinamento, até acertar
            treinamento()




