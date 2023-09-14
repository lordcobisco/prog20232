''' Esse código simula o que seria um código de uma coleta em tempo real '''

''' Duração do protocolo de aquisição '''
tempoExperimento = 1 #s

''' Frequência em que os dados estão sendo coletados '''
frequenciaSensor = 10 #hz - Coletas / segundo

'''Uma lista que no caso de uma coleta com sensores EEG, representaria um canal, ou seja, um sensor. '''
dado = []

''' Essa variável representa quantas tuplas / valores uma lista ira armazenar.'''
qtdDados = tempoExperimento*frquenciaSensor

soma = 0
for contador in range(len(dado)):
  soma = soma + (1 / frequenciaSensor) * dado[contador] # Representação de uma integral - Soma de riemann
print(soma)
