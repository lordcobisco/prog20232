#Problema experimento com
#Coleta e Processamento de sinais

# preciso ter a descrição do que se faz depois uma entrada e uma saída e o que se faz e pronto.
# todo experiemento vai ter dados (entrada e saida) 
# todo experimento tem um tempo
# range = 
# processar = para processar o sinal vc não precisar saber qual é os filtros, e so escolher quando quer usar e quando quiser usar (o processar é definir)

#EXERCÍCIOS
# toda essa função é uma memoria
# tempoExperimento = 1 #S
# frequenciaSensor = 10 #Hz

def coletardados(tempoExperimento, 
                  frequenciaSensor ):

    quantidadedeDados = tempoExperimento*frequenciaSensor
# coleta
    dado = []
    for contador in range(quantidadedeDados) :
        dado.append(float(input()))

    return dado

# dado = coletardados

# so estara coletando (executar) dados quando utiliza:
coletardados(1,10)


#OUTRO EXEMPLO:
# dadosEx1 = coletardados(1,1)
# dadosEx2 = coletardados(1,2)
# dadosEx3 = coletardados(1,10)

#PROCESSAMENTO DE DADOS:

# 1 opção
dadosEx1 = coletardados(1,1)
def integrar(dado, frequencisensor):
    soma = 0
    for data in dado : #( a data vai fornecer dentro da informação dado)
        soma = soma + (1/frequencisensor)* data 
        return soma
    

# 2 opção
tempo = 1
freq = 1

dadosEx1 = coletardados(tempo, freq)
integral = integrar(dadosEx1, freq) # (pega os dados e passa a frequencia do sensor)

 # 3 opção
tempo = 1
freq = 1

integral = integrar(coletardados(tempo,freq), freq) # isso é uma lista, é o resultado do dado coletado

# 4 opção
tempo = 1
freq = 1

integral = integrar(dado = coletardados(tempo,freq), frequencisensor=freq) 

# 5 opção

processar = integrar
processar (coletardados(tempo,freq), freq) # (isso se chama polimorfismo)
