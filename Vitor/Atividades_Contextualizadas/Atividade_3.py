'''Variáveis:
        Format -- Resolução de imagem desejada
        Tipo de célula a ser escaneada
        Zoom Factor?
        Quantos fotodetectores serão utilizados? (PMT 1/2/3 e/ou 4)
        Speed -- Numero de linhas lidas por segundo pela varredura do laser (Medida em Hz)
        Qual laser será usado? (Diodo 405 / Argônio / HeNe 543 / HeNe 594 / Hene633)
        Intensidade dos lasers --- Medido em porcentagem (20/30%)
        Número de pixels --- (Usar megapixels)
        gain ---- Quanto mais alto, mais alta é a intensidade dos pixels (0 à 255)
        offset --- Quanto mais alto, menores são os valores dos pixels
        '''
objeto = 'microtúbulos'
Format = '1920x1080'
laser = 'Argônio'
intensidade_laser = 20
speed = 400
zoom = 3
rotation = 0
gain = 255
save = 'csv'
rgb = '455 / 233 / 0'

print('Esse programa tem como objetivo receber dados para configurar o microscópio através do programa de controle e exibição de imagens')

objeto = input('Qual a célula a ser escaneada? : ')
q_1 = print(f'Houve alteração na variável inserida? {objeto!="microtubulos"}')

Format = input('Qual a resolução de imagem desejada?:  ')
q_2 = print(f'Houve alteração na variável inserida? {Format != "1920x1080"}')

laser = input('Digite quais os lasers que você quer que sejam usados (Diodo 405 / Argônio (488nm) / HeNe 543 / HeNe594 / HeNe633): ')
q_3 = print(f'Houve alteração na variável inserida? {laser != "Argônio"}')

intensidade_laser = int(input('Qual a intensidade do laser? (0-100%): '))
q_4 = print(f'Houve alteração na variável inserida? {intensidade_laser != 20}')

speed = int(input('Digite a velocidade (em Hz) de leitura das linhas (10 - 1400): '))
q_5 = print(f'Houve alteração na variável inserida? {speed != 400}')

zoom = int(input('Qual o zoom que deve ser aplicado? (1-10): '))
q_6 = print(f'Houve alteração na variável inserida? {zoom != 3}')

rotation = int(input('Ângulo de rotação da imagem (-180 até 180): '))
q_7 = print(f'Houve alteração na variável inserida? {rotation != 0}')

gain = int(input('Qual a intensidade dos pixels? (0-255): '))
q_8 = print(f'Houve alteração na variável inserida? {gain != 255}')

save = input('Qual o formato em que a imagem deve ser salva?: ')
q_9 = print(f'Houve alteração na variável inserida? {save != "csv"}')

rgb = input('Defina, no sistema RGB e separado por "/" os valores respectivos de R,G e B para a imagem: ')
q_10 = print(f'Houve alteração na variável inserida? {rgb != "455 / 233 / 0"}')

print(f'As informações de configurações setadas pelo usuário são: \nA célula a ser analisada é: {objeto} \nA resolução setada é: {Format} \nO(s) laser(s) utilizado(s) é(são): {laser} e sua intensidade é {intensidade_laser}% \nA velocidade setada é {speed}Hz \nO zoom aplicado é: {zoom} \nO ângulo de rotação é: {rotation} \nA intensidade dos pixels setada é: {gain} \nO rgb setado para as imagens é: {rgb} \nA imagem será salva no formato: {save}')


print('A partir de agora calibre o equipamento no sentido horizontal. Utilize a primeira e a última letra do seu nome para definir as direções: ')

primeira_letra=  input('Digite a primeira letra do seu nome: ')
ultima_letra = input('Digite a ultima letra do seu nome: ')

contador_primera = 0
contador_ultima = 0

N = int(input('Quantas vezes pretende alterar o equipamento: '))
while N%2 != 0:
     N = int(input('Digite um número par, por favor: '))

while contador_primera + contador_ultima <= N:
    
    letra = input('Digite a primeira ou a ultima letra do seu nome: ')

    if letra == primeira_letra:
        if contador_primera < N/2:
                print(f'Informação correta. A letra digitada é {letra}')
                contador_primera +=1
        else:
             print('O número máximo de uso desse comando foi alcançado')

    elif letra == ultima_letra:
        if contador_ultima < N/2:
                print(f'Informação correta. A letra digitada é {letra}')
                contador_ultima +=1
        else:
             print('O número máximo de uso desse comando foi alcançado')
    else:
         print('Informação errônea. Tente novamente')


print('Calibre o equipamento no sentido vertical agora usando a segunda e penultima letra do seu nome:')

segunda_letra=  input('Digite a primeira letra do seu nome: ')
penultima_letra = input('Digite a ultima letra do seu nome: ')

contador_segunda = 0
contador_penultima = 0

P = int(input('Quantas vezes pretende alterar o equipamento: '))

while P%2 != 0:
     N = int(input('Digite um número par, por favor: '))

while contador_segunda + contador_penultima <= P:
    
    letra_2 = input('Digite a primeira ou a ultima letra do seu nome: ')

    if letra_2 == segunda_letra:
        if contador_segunda < N/2:
                print(f'Informação correta. A letra digitada é {letra_2}')
                contador_segunda +=1
        else:
             print('O número máximo de uso desse comando foi alcançado')

    elif letra_2 == penultima_letra:
        if contador_penultima < N/2:
                print(f'Informação correta. A letra digitada é {letra_2}')
                contador_penultima +=1
        else:
             print('O número máximo de usos desse comando foi alcançado')
    else:
         print('Informação errônea. Tente novamente')