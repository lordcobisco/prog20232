# Inclua no exercício de Método de discriminação de estímulos auditivos para primatas através do condicionamento operante uma atualização (com commit)

# Adaptação do problema utilizando estruturas de repetição -  utilizando o exercicio contextualizdo 4

#HABITUAÇÃO

Habituacao_animal = False

while not Habituacao_animal:
    Habituacao = input("O animal está habituado? (sim=1 ou não=0)")
    if Habituacao == "0":
        print("Realize a etapa de habituação.")
    elif Habituacao == "1":
        Habituacao_animal = True
        print("Animal habituado, começar treinamento.")
    else:
        print("Resposta inválida. Por favor, responda com '1' para sim ou '0' para não.")

# Regime de aproximações sucessivas 
# aproximação 30cm
        if Habituacao_animal == True:
            print("APROXIMAÇÕES SUCESSIVAS")

aproximação = False

while not aproximação:
    aproximação_animal = int(input("quantos cm o animal se aproximou? "))
    if aproximação_animal <= 30:
        print ("liberar 0,5 mL de recompensa")
        sagui_aproximado = True 
        break
    elif aproximação_animal > 30:
        print ("So liberar quando a aproximação ficar menor que 30cm")
        sagui_aproximado = False
    else:
        print("Resposta inválida")
        
# Se animal tocou na barra 20x, retornar que o experimento passou para a próxima etapa

sagui_aproximado = True 

tocar_barra = False

while not tocar_barra: 
    tocar_barra_1 = input("O sagui tocou 20x na barra? (sim ou não)")
    if tocar_barra_1 == "sim":
        print("O experimento passou para próxima etapa")
        break
tocar = True

# Se o som1 foi emitido e o animal tocou na barra esquerda, liberar 0,5ml de rec

tocar = True

som_1 = False

while not som_1:
    som_p1 = input("O som 1 foi emitido ao toque do animal na barra esquerda? (sim ou não)")
    if som_p1 == "sim":
        print("liberar 0,5 mL de recompensa")   
        sons_1 = True
        break
    else:
        print("Não liberar recompensa")

# Se o som2 foi emitido e o animal tocou na barra direita, liberar 0,5ml de rec

    sons_1 = True

som_2 = False

while not som_2:
    som_p2 = input( "O som 2 foi emitido ao toque do animal na barra direita? (sim ou não)")
    if som_p2 == "sim":
        print("liberar 0,5 mL de recompensa")
        sons_2 = True
        break
    else :
        print("não liberar recompensa")


# Se o experimento foi realizado 50x em 30min, apresentar que o experimento seguirá para a próxima fase.

sons_2 = True

Tempo = False
Repetições = False

while not Tempo:
    Tempo_T = int(input("Quanto tempo durou o experimento?"))
    Repetições_R = int(input("Quantas repetições foram realizadas?"))
    
    if Tempo_T <= 30:
        if Repetições_R >= 50:
            print("Experimento seguirá para a próxima fase")
        else:
            print("O experimento não seguirá para a próxima fase")
        break  
    else:
        print("O experimento não seguirá para a próxima fase")