#COLETA E PROCESSAMENTO 
def coletarDados (tempodeexperimento, frequenciasensor):    #definir função e as variaveis que vou usar 
    quantdados = tempodeexperimento * frequenciasensor #instrução
    dado = []  #o que eu recebo
    for contador in range (quantdados): #quantas vezes o for vai rodar depende do tempo e da frequencia 
        dado.append(float(input()))   #coleta no dado
    return dado 

dados = coletarDados(1,10) #chamar a função
def integrar(dado, frequenciasensor):
    soma = 0  
    for data in dado :
        soma = soma + (1 / frequenciasensor ) * data
    return soma

temp = 1
freq = 10
dadosEx1 = coletarDados (temp,freq)
integral = integrar(coletarDados (temp, freq), freq)

processar = integrar
processar (coletarDados(temp, freq), freq)
print (processar)

# dicionário 
#dicionario {[maria]}