
#dado =[123, 231, 312, 1234]
#soma = dado[0] + dado[1] + dado[2]
#print (soma)

#soma = 0
#for contador in range(4): #quant de informações 
#    soma += dado[contador] #soma acumulada
#print (soma)

#for contador in range(len(dado)): #len - variação do tamanho do dado 
#    soma += dado[contador] #soma acumulada
#print (soma)

#tempoExperimento = 1 #s
#frequenciaSensor = 10 #Hz
#quantDados = tempoExperimento*frequenciaSensor

#dado =[]
#for contador in range(quantDados): #len - variação do tamanho do dado 
#    dado.append(float(input())) #coleta - a cada dado recebido, será armazenada dentro do dado. append adiciona o dado dentro da ultima posição 
#print (dado)

#tempoExperimento = 1 #s
#frequenciaSensor = 10 #Hz
#quantDados = tempoExperimento*frequenciaSensor

#dado = []
#for contador in range(quantDados): #len - variação do tamanho do dado 
 #   dado.append(float(input())) #coleta - a cada dado recebido, será armazenada dentro do dado. append adiciona o dado dentro da ultima posição 

#soma = 0 
#for contador in range(len (dado)): 
 #   soma = soma + (1 / frequenciaSensor) * dado [contador]
#print (soma)


#Nova forma 
#for
#tempoExperimento = 1 #s
#frequenciaSensor = 10 #Hz
#quantDados = tempoExperimento*frequenciaSensor

#dado = []
#for contador in range(quantDados): #len - variação do tamanho do dado 
#    dado.append(float(input())) #coleta - a cada dado recebido, será armazenada dentro do dado. append adiciona o dado dentro da ultima posição 

#soma = 0 
#for data in dado: #Cria uma variável para adionar o que tem em dado 
#    soma = soma + (1 / frequenciaSensor) * dado [contador]
#print (soma)

#dicionario = { "Brasil":[1,2,3], 
#           "EUA": [4,5,6]
#}
#for pais in dicionario: 
 #   print (pais)
 #   print (dicionario[pais])

#while 
acabou = False
while not acabou: 
    acabou = (input () == 'x')
    print ("tente novamente")
    pass 
print("acabou o prog")

while True:
    if input () == "x":
        break #forçar a saida da repetição
    pass