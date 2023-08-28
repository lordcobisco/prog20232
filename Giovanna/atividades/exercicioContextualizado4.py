
statusHabituacao = int(input("Seu animal está habituado? Digite 1 para SIM e 2 para NÃO ")) # É preciso saber se o animal foi habituado para iniciar o teste

if statusHabituacao == 1: 
    distanciaInicial = 30 # Define o quão próximo o animal está da barra, começando com 30cm 

    distanciaAtual = float(input("Qual a distância atual do animal até a barra em centímetros? ")) # saber se o animal se aproximou da barra

    if distanciaAtual < distanciaInicial: # se a distancia atual é menor que a distancia inicial (o animais se aproximou), a recompensa é liberada
        print("0,5ml de recompensa liberada! ")

        statusPrimeiraEtapa = int(input("O animal tocou 20x na barra? Digite 1 para SIM e 2 para NÃO ")) # o animal precisa tocar na barra 20x para seguir para a próxima etapa do experimento

        if statusPrimeiraEtapa == 1: # verifica se o animal atingiu o requisito para passar para próxima etapa
            print("O experimento passou para a próxima etapa.")
        else: 
            print("Oops! Não é possível ir para a próxima etapa :(")

        # para receber a recompensa, o animal precisa tocar na barra esquerda quando o som 1 tocar e na barra direita quando o som 2 tocar
        somEmitido = int(input("Informe qual som foi emitido, 1 ou 2: ")) # lê qual som foi emitido
        barraTocada = int(input("Informe qual barra o animal tocou. Digite 4 para esquerda e 5 para direita: ")) # lê qual barra o animal tocou

        # as condições a seguir verificam se o animal atendeu ao requisito para liberar a recompensa ou não
        if somEmitido == 1 and barraTocada == 4:
            print("0,5ml de recompensa liberada! ")
        elif somEmitido == 2 and barraTocada == 5: 
            print("0,5ml de recompensa liberada! ")
        else: 
            print("Nenhuma recompensa liberada.")
        
        statusSegundaEtapa = int(input("O experimento foi realizado 50x em 30min? Digite 1 para SIM e 2 para NÃO ")) # lê a condição do experimento

        # a condição verifica se os requisitos para seguir para a próxima fase foram atendidos 
        if statusSegundaEtapa == 1: 
            print("O experimento seguirá para a próxima fase.")
        else: 
            print("O experimento ainda não pode seguir para a próxima fase.")


else: 
    print("Oops! Só é possível começar o treinamento quando o animal estiver habituado :(")