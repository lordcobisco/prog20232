''' Esse código simula o que seria um código de uma coleta em tempo real '''

''' Duração do protocolo de aquisição '''
tempoExperimento = 1 #s

''' Frequência em que os dados estão sendo coletados '''
frequenciaSensor = 10 #hz - Coletas / segundo

'''Uma lista que no caso de uma coleta com sensores EEG, representaria um canal, ou seja, um sensor. '''
dado = []

''' Essa variável representa quantas tuplas / valores uma lista ira armazenar.'''
qtdDados = tempoExperimento*frquenciaSensor

for contador in range(qtdDados):
  
  '''Essa entrada, que atualmente será realizada manualmente, representa a porta de entrada
  para dados que seriam coletados através de um sensor'''
  dado.append(float(input()))
