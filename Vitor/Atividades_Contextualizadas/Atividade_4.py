def habituacao():  
    hab = input('O animal está habituado? (S/N): ').upper()

    if hab == 'S':
        print('O animal deve começar a se aproximar da barra \n')
        print(200*'=')
        print('\n')
        aproximacao()
    
    else:
        print('O animal ainda não está habituado, retorne ao treino de habituação')

def aproximacao():
    S = 30
    while S >= 0.001:
        aproximar = input('O animal está se aproximando das barras? (S/N): ').upper()

        if aproximar == 'S':
            distancia = float(input('O quanto ele andou (cm)? '))
            S = S - distancia
            print(f'O animal está a {S}cm das barras agora e foi liberado 0.5ml de rec')
            
        
        else:
            print(f'Não houve aproximação. O animal continua a {S}cm das barras e nada acontece')

    print('O animal está próximo das barras, passaremos ao próximo teste')
    print(200*'=')
    print('\n')
    etapa_1()

def etapa_1():
    contador = 0
    while contador < 20:
        acao = input('O animal tocou uma das barras? (S/N): ').upper()

        if acao == 'S':
            contador = contador +1
            print(f'O animal recebeu 0.5ml de rec e tocou uma das barras {contador} vezes até o momento.')
        
        else:
            print(f'O animal não tocou nenhuma das barras nesse momento. O total de vezes que a barra foi tocada até agora é {contador}')
    
    print('O experimento passará para a próxima etapa agora')
    print(200*'=')
    print('\n')
    etapa_2(N)

def etapa_2(N):
    contador_2 = 0
    while contador_2 <= N:
        emissao_do_som = input('Algum som foi emitido? (S/N): ').upper()

        if emissao_do_som == 'S':
            tipo_som = input('Qual dos sons foram emitidos? (phee/trill): ').lower()
            
            if tipo_som == 'phee':
                barra_esq = input('O animal tocou na barra esquerda? (S/N): '). upper()
                
                if barra_esq == 'S':
                    print('0.5 ml de rec foram liberados')
                    contador_2 = contador_2 + 1

                
                else:
                    print('Nenhuma recompensa foi liberada, a luz foi desligada por 5s e nesse tempo o som phee será tocado constantemente')
                    for i in range (1,6):
                        print(i)
                    print('A luz foi religada e o som phee foi interrompido')
                    contador_2 = contador_2 + 1
            
            else:
                barra_dir = input('O animal tocou na barra direita? (S/N) :').upper()

                if barra_dir == 'S':
                    print('0.5 ml de rec foram liberados')
                    contador_2 = contador_2 + 1

                else:
                    print('Nenhuma recompensa foi liberada, a luz foi desligada por 5s e nesse tempo o som trill será tocado constantemente')
                    for i in range (1,6):
                        print(i)
                    print('A luz foi religada e o som trill foi interrompido')
                    contador_2 = contador_2 + 1
        else:
            print('Nenhum som foi emitido. Atente-se aos sons que serão produzidos')
    
    print('Fim da etapa 2')
    print(200*'=')
    print('\n')



N = int(input('Quantas vezes pretende realizar o experimento?:  '))

habituacao()

tempo = int(input('Quantos minutos durou esse teste?: '))

if tempo <= 29:
    pergunta = input('O experimento ainda não poderá passar para a próxima fase. Deseja reiniciá-lo agora? (S/N): ').lower()
    if pergunta == 's':
        habituacao()
    else:
        print('Programa interrompido')
