#("HABITUAÇÃO")

Habituacao_animal = input("O animal está habituado? (sim ou não)")
if Habituacao_animal == "sim":
    print("Animal habituado, começar treinamento.")
    Habituacao_animal = True
else:
    print("realize a etapa de habituação")
    Habituacao_animal = False

# Regime de aproximações sucessivas 
# aproximação 30cm

if Habituacao_animal == True:
    print("APROXIMAÇÕES SUCESSIVAS")
    aproximação = 30
    aproximação = float(input("quantos cm o animal se aproximou? "))
    if aproximação < 30:
        print ("liberar 0,5 mL de recompensa")
        sagui_aproximado = True
    else:
        print ("So liberar quando a aproximação ficar menor que 30cm")
        sagui_aproximado = False

# Se animal tocou na barra 20x, retornar que o experimento passou para a próxima etapa

if sagui_aproximado == True:
    tocar_barra = input("O sagui tocou 20x na barra? (sim ou não)")
    if tocar_barra == "sim":
        print("O experimento passou para próxima etapa")
tocar = True

# Se o som1 foi emitido e o animal tocou na barra esquerda, liberar 0,5ml de rec

if tocar == True:
    som_1 = input("O som 1 foi emitido ao toque do animal na barra esquerda? (sim ou não)")
    if som_1 == "sim":
        print("liberar 0,5 mL de recompensa")   
    else:
        print("Não liberar recompensa")
      

# Se o som2 foi emitido e o animal tocou na barra direita, liberar 0,5ml de rec

    som_2 = input( "O som 2 foi emitido ao toque do animal na barra direita? (sim ou não)")
    if som_2 == "sim":
        print("liberar 0,5 mL de recompensa")
    else :
        print("não liberar recompensa")

# Se o experimento foi realizado 50x em 30min, apresentar que o experimento seguirá para a próxima fase.

Tempo =float(input("Quanto tempo durou o experimento?"))
Repetições = float(input("Quantas repetições foram realizadas?"))
if Tempo <30 and Repetições >= 50:
        print("Experimento seguirá para a próxima fase")
else:
        print("O experimento não seguirá para a próxima fase")

        




    



    





