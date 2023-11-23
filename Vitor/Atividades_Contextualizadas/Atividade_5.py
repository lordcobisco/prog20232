'''Lista organizada, respectivamente, em: Região(1) / Estado(2) / Municipio(3) / cod_uf(4) / cod_mun(5) / codRegiaoSaude(6) / nomeRegiaoSaude(7) / data(8) / semanaEpi(9) / 
populacaoTCU2019(10) / casosAcumulado(11) / casos Novos(12) / obitosAcumulados(13) / obitosNovos(14)''' 

regiao = 0
estado = 1
municipio = 2
cod_uf = 3
cod_mun = 4
cod_regiao_saude = 5
nome_regiao_saude = 6
data = 7
semanaEpi = 8
populacaoTCU2019 = 9
casos_acumulados = 10
casos_novos = 11
obitos_acumulados = 12
obitos_novos = 13


lista_covid = [
               ['Norte', 'AM' , 'Atalaia do Norte' ,    13,    130020,   13009,    'ALTO SOLIMOES',      '2023-01-31',   5 ,    19921,    4241,    0,    11,    0,'  ',  0],
               ['Norte',  'RO',  'Nova Brasilândia D.Oeste',  11,  110014,  11005,  'ZONA DA MATA',  '2023-05-29,22',  20474,  5382,  0,  40,  0, '  ' , '  ' ,  0],
               ['Norte',  'AC',  'Porto Walter',  12,  120039,  12003,  'JURUA E TARAUACA/ENVIRA',   '2023-02-01',   5,   11982,   571,   0,  7,  0, '  ' , '  ' ,  0],
               ['Norte',  'RR',  'Caracaraí',  14,  140020,  14002,  'SUL',  '2023-02-02',  5,  21926,  5582,  0,  63,  0, '  ' , '  ' ,  0],
               ['Norte',  'PA',  'Goianésia do Pará',  15,  150309,  15004,  'LAGO DE TUCURUI',  '2023-01-03',  1,  40475,  3710,  0,  38,  0, '  ' , '  ' ,  0],
               ['Norte',  'TO',  'Crixás do Tocantins',  17,  170625,  17005,  'ILHA DO BANANAL',  '2023-06-25',  26,  1722,  404,  0,  0,  0, '  ' , '  ' ,  0],
               ['Nordeste',  'MA',  'Altamira do Maranhão',  21,  210040,  21002,  'BACABAL',  '2023-04-09',  15,  8128,  556,  0,  15,  0, '  ' , '  ' ,  0],
               ['Nordeste',  'PI',  'Pavussu',  22,  220785,  22011,  'VALE DOS RIOS PIAUI E ITAUEIRAS',  '2023-03-03',  9,  3677,  575,  0,  15,  0, '  ' , '  ' ,  0],
               ['Nordeste',  'CE',  'Fortaleza',  23,  230440,  23001,  '1ª REGIAO FORTALEZA',  '2023-06-30',  26,  2669342,  410654,  0,  11801,  0, ' ' , ' ' ,  1],
               ['Nordeste',  'RN',  'Natal',  24,  240810,  24007,  '7ª REGIAO DE SAUDE - METROPOLITANA',  '2023-06-26',  26,  884122,  156791,  0,  3142,  0, ' ' ,  ' ',  1],
               ['Nordeste',  'PB',  'Araruna',  25,  250100,  25002,  '2ª REGIAO',  '2023-05-04',  18,  20312,  1120,  0,  18,  0, ' ' , ' ' ,  0],
               ['Nordeste',  'PE',  'Manari',  26,  260915,  26002,  'ARCOVERDE',  '2023-06-22',  25,  21434,  960,  0,  8,  0, ' ' ,' '  ,  0],
               ['Nordeste',  'AL',  'Maceió',  27,  270430,  27001,  '1ª REGIAO DE SAUDE',  '2023-03-09',  10,  1018948,  131775,  0,  3208,  0, ' ' , ' ' ,  1],
               ['Nordeste',  'SE',  'General Maynard',  28,  280250,  28006,  'NOSSA SENHORA DO SOCORRO',  '2023-02-26',  9,  3346,  484,  0,  10,  0, ' ' ,' '  ,  0],
               ['Nordeste',  'BA',  'São Francisco do Conde',  29,  292920,  29020,  'SALVADOR',  '2023-05-26',  21,  39802,  5908,  0,  77,  0, ' ' , ' ' ,  1],
               ['Nordeste','PI','Teresina',22,221100,22004,'ENTRE RIOS','2023-06-30',26,864845,144071,0,3027,0,' ',' ', 1],
               ['Sudeste',  'MG',  'Galiléia',  31,  312730,  31036,  'GOVERNADOR VALADARES',  '2023-04-13',  15,  6817,  1240,  0,  32,  0, ' ' , ' ' ,  0],
               ['Sudeste',  'ES',  'Viana',  32,  320510,  32002,  'METROPOLITANA',  '2023-01-23',  4,  78239,  23100,  1,  314,  0, ' ' ,' '  ,  1],
               ['Sudeste',  'RJ',  'Rio de Janeiro',  33,  330455,  33005,  'METROPOLITANA I',  '2023-06-30',  26,  6718903,  1337413,  0,  38263,  0,' '  ,' '  ,  1],
               ['Sudeste',  'SP',  'Pederneiras',  35,  353670,  35062,  'BAURU',  '2023-06-30',  26,  46687,  10352,  0,  145,  0, ' ' , ' ' ,  0],
               ['Sul',  'PR',  'Maringá',  41,  411520,  41015,  '15ª RS MARINGA',  '2023-06-30',  26,  423666,  149050,  0,  1871,  0, ' ' ,' '  ,  0],
               ['Sul',  'SC',  'Chapadão do Lageado',  42,  420419,  42004,  'ALTO VALE DO ITAJAI',  '2023-06-30',  26,  2988,  751,  0,  6,  0, ' ' , ' ' ,  0],
               ['Sul',  'RS',  'Gramado',  43,  430910,  43023,  'REGIAO 23',  '2023-06-30',  26,  36232,  16631,  0,  167,  0,' '  ,' '  ,  0],
               ['Centro-Oeste',  'MS',  'Coronel Sapucaia',  50,  500315,  50003,  'DOURADOS',  '2023-01-18',  3,  15253,  1605,  0,  45,  0, ' ' ,' '  ,  0],
               ['Centro-Oeste', 'MT',  'Denise',  51,  510345,  51007,  'MEDIO NORTE MATOGROSSENSE',  '2023-06-30',  26,  9462,  1350,  0,  21,  0, ' ' ,' '  ,  0],
               ['Centro-Oeste',  'GO',  'Itumbiara',  52,  521150,  52017,  'SUL',  '2023-06-30',  26,  104742,  28556,  0,  533,  0, ' ' ,' '  ,  0]
               ]


tupla_covid = (
                ('Norte', 'AM' , 'Atalaia do Norte' , 13, 130020, 13009, 'ALTO SOLIMOES', '2023-01-31', 5 , 19921, 4241, 0, 11, 0,' ' , ' ', 0),
                ('Norte', 'RO', 'Nova Brasilândia D.Oeste', 11, 110014, 11005, 'ZONA DA MATA', '2023-05-29,22', 20474, 5382, 0, 40, 0,' ' , ' ', 0),
                ('Norte', 'AC', 'Porto Walter', 12, 120039, 12003, 'JURUA E TARAUACA/ENVIRA', '2023-02-01', 5, 11982, 571, 0, 7, 0,' ' ,' ' , 0),
                ('Norte', 'RR', 'Caracaraí', 14, 140020, 14002, 'SUL', '2023-02-02', 5, 21926, 5582, 0, 63, 0, ' ', ' ', 0),
                ('Norte', 'PA', 'Goianésia do Pará', 15, 150309, 15004, 'LAGO DE TUCURUI', '2023-01-03', 1, 40475, 3710, 0, 38, 0, ' ',' ' , 0),
                ('Norte', 'TO', 'Crixás do Tocantins', 17, 170625, 17005, 'ILHA DO BANANAL', '2023-06-25', 26, 1722, 404, 0, 0, 0,' ' ,' ' , 0),
                ('Nordeste', 'MA', 'Altamira do Maranhão', 21, 210040, 21002, 'BACABAL', '2023-04-09', 15, 8128, 556, 0, 15, 0, ' ', ' ', 0),
                ('Nordeste', 'PI', 'Pavussu', 22, 220785, 22011, 'VALE DOS RIOS PIAUI E ITAUEIRAS', '2023-03-03', 9, 3677, 575, 0, 15, 0,' ' , ' ', 0),
                ('Nordeste', 'CE', 'Fortaleza', 23, 230440, 23001, '1ª REGIAO FORTALEZA', '2023-06-30', 26, 2669342, 410654, 0, 11801, 0, ' ',' ' , 1),
                ('Nordeste', 'RN', 'Natal', 24, 240810, 24007, '7ª REGIAO DE SAUDE - METROPOLITANA', '2023-06-26', 26, 884122, 156791, 0, 3142, 0, ' ', ' ', 1),
                ('Nordeste', 'PB', 'Araruna', 25, 250100, 25002, '2ª REGIAO', '2023-05-04', 18, 20312, 1120, 0, 18, 0,' ' , ' ', 0),
                ('Nordeste', 'PE', 'Manari', 26, 260915, 26002, 'ARCOVERDE', '2023-06-22', 25, 21434, 960, 0, 8, 0, ' ', ' ', 0),
                ('Nordeste', 'AL', 'Maceió', 27, 270430, 27001, '1ª REGIAO DE SAUDE', '2023-03-09', 10, 1018948, 131775, 0, 3208, 0,' ' ,' ' , 1),
                ('Nordeste', 'SE', 'General Maynard', 28, 280250, 28006, 'NOSSA SENHORA DO SOCORRO', '2023-02-26', 9, 3346, 484, 0, 10, 0, ' ', ' ', 0),
                ('Nordeste', 'BA', 'São Francisco do Conde', 29, 292920, 29020, 'SALVADOR', '2023-05-26', 21, 39802, 5908, 0, 77, 0, ' ',' ' , 1),
                ('Nordeste','PI','Teresina',22,221100,22004,'ENTRE RIOS','2023-06-30',26,864845,144071,0,3027,0,' ',' ', 1),
                ('Sudeste', 'MG', 'Galiléia', 31, 312730, 31036, 'GOVERNADOR VALADARES', '2023-04-13', 15, 6817, 1240, 0, 32, 0, ' ', ' ', 0),
                ('Sudeste', 'ES', 'Viana', 32, 320510, 32002, 'METROPOLITANA', '2023-01-23', 4, 78239, 23100, 1, 314, 0,' ' , ' ', 1),
                ('Sudeste', 'RJ', 'Rio de Janeiro', 33, 330455, 33005, 'METROPOLITANA I', '2023-06-30', 26, 6718903, 1337413, 0, 38263, 0,' ' ,' ' , 1),
                ('Sudeste', 'SP', 'Pederneiras', 35, 353670, 35062, 'BAURU', '2023-06-30', 26, 46687, 10352, 0, 145, 0, ' ',' ' , 0),
                ('Sul', 'PR', 'Maringá', 41, 411520, 41015, '15ª RS MARINGA', '2023-06-30', 26, 423666, 149050, 0, 1871, 0, ' ',' ' , 0),
                ('Sul', 'SC', 'Chapadão do Lageado', 42, 420419, 42004, 'ALTO VALE DO ITAJAI', '2023-06-30', 26, 2988, 751, 0, 6, 0, ' ', ' ', 0),
                ('Sul', 'RS', 'Gramado', 43, 430910, 43023, 'REGIAO 23', '2023-06-30', 26, 36232, 16631, 0, 167, 0,' ' , ' ', 0),
                ('Centro-Oeste', 'MS', 'Coronel Sapucaia', 50, 500315, 50003, 'DOURADOS', '2023-01-18', 3, 15253, 1605, 0, 45, 0, ' ',' ' , 0),
                ('Centro-Oeste', 'MT', 'Denise', 51, 510345, 51007, 'MEDIO NORTE MATOGROSSENSE', '2023-06-30', 26, 9462, 1350, 0, 21, 0,' ' ,' ' , 0),
                ('Centro-Oeste', 'GO', 'Itumbiara', 52, 521150, 52017, 'SUL', '2023-06-30', 26, 104742, 28556, 0, 533, 0, ' ',' ' , 0)
                )
'''
print('\n \n')
print(f'Lista: O número de casos acumulados no RJ é de: {lista_covid[-8][casos_acumulados]}')
print(f'TUPLA: O número de casos acumulados no RJ é de: {tupla_covid[-8][casos_acumulados]}')

print('\n \n')

print('Expondo os estados e a quantidade de casos acumulados na lista')
print('ESTADOS:          CASOS ACUMULADOS:')
for i in range(len(lista_covid)):
    print(f'{lista_covid[i][estado]}                      {lista_covid[i][casos_acumulados]}')

print('\n\n')

print('Agora o mesmo para Tupla')

print('ESTADOS:          CASOS ACUMULADOS:')
for i in range(len(tupla_covid)):
    print(f'{tupla_covid[i][estado]}                      {tupla_covid[i][casos_acumulados]}')

print('\n\n')



print(f'LISTA: Houve um erro quanto ao índice de óbitos novos do estado da Paraíba. O valor anterior era {lista_covid[5][obitos_novos]}')

lista_covid[5][obitos_novos]+= 10

print(f'LISTA: Agora, atualizado, é {lista_covid[5][obitos_novos]}')
print('\n \n')


print(f'LISTA: Houve um erro quanto ao índice de óbitos novos do estado da Paraíba. O valor anterior era {tupla_covid[5][obitos_novos]}')

tupla_covid[5][obitos_novos]+= 10

print(f'LISTA: Agora, atualizado, é {tupla_covid[5][obitos_novos]}')

print('Não é possível fazer essa alteração em uma tupla, porque os itens dentro de uma tupla são imutáveis')

print('\n \n')

covid_sp = [
                ['Sudeste','SP','Adamantina',35,350010,35091,'ADAMANTINA','2023-09-15',37,35068,11662,0,192,0,' ',' ',0],
                ['Sudeste','SP','Adolfo',35,350020,35156,'JOSE BONIFACIO','2023-09-15',37,3562,1168,0,28,0,' ',' ',0],
                ['Sudeste','SP','Aguaí',35,350030,35142,'MANTIQUEIRA','2023-09-15',37,36305,7724,0,139,0,' ',' ',0],
                ['Sudeste','SP','Águas da Prata',35,350040,35142,'MANTIQUEIRA','2023-09-15',37,8180,2192,0,40,0,'','',0],
                ['Sudeste','SP','Águas de Lindóia',35,350050,35074,'CIRCUITO DAS AGUAS','2023-09-15',37,18705,5670,0,67,0,'','',0],
                ['Sudeste','SP','Águas de Santa Bárbara',35,350055,35061,'VALE DO JURUMIRIM','2023-09-15',37,6075,623,0,25,0,'','',0],
                ['Sudeste','SP','Águas de São Pedro',35,350060,35103,'PIRACICABA','2023-09-15',37,3451,478,0,17,0,'','',0],
                ['Sudeste','SP','Agudos',35,350070,35062,'BAURU','2023-09-15',37,37214,9337,0,123,0,'','',0],
                ['Sudeste','SP','Alambari',35,350075,35161,'ITAPETININGA','2023-09-15',37,6025,1671,0,13,0,'','',0],
                ['Sudeste','SP','Alambari',35,350075,35161,'ITAPETININGA','2023-09-15',37,6025,1671,0,13,0,'','',0],
                ['Sudeste','SP','Altair',35,350090,35051,'NORTE - BARRETOS','2023-09-15',37,4160,325,0,18,0,'','',0],
                ['Sudeste','SP','Bauru',35,350600,35062,'BAURU','2023-09-15',37,376818,91750,0,1498,0,'','',0]
]

lista_covid.append(covid_sp)

for i in range (len(covid_sp)):
    covid_sp[i].pop(cod_regiao_saude)
    covid_sp[i].pop(nome_regiao_saude-1)   #Alterou a posição do nome da região ao apagar o cod_regiao_saude
    print(covid_sp[i])

print(' \n \n')

print(len(lista_covid))

print('\n \n')



lista_obitos_novos = []

for i in range(len(lista_covid)):
    lista_obitos_novos.append(lista_covid[i][obitos_novos])

#Não é possível printar o máximo e o mínimo de obitos novos porque em 2023 não houve mais mortes por covid 19 declaradas pelo ministério da saúde
'''
print(280*"=")

municipio_lista = []
lista_info = []

for i in range (len(lista_covid)):
    municipio_lista.append(lista_covid[i][municipio])
    lista_info.append(lista_covid[i][estado])
    lista_info.append(lista_covid[i][nome_regiao_saude])
    lista_info.append(lista_covid[i][casos_novos])


dicionario_covid= {}

for i in range(len(municipio_lista)):
    for j in range(len(lista_covid)):
        dicionario_covid[municipio_lista[i]] = lista_covid[j-10]


print(lista_info)
print(80*'=')
print(dicionario_covid)
print('\n\n')
print('Extrairemos agora os dados de teresina')
print('\n')

print('Dados de Teresina(PI):')

print(f'Região: {dicionario_covid["Teresina"][regiao]}')
print(f'Estado: {dicionario_covid["Teresina"][estado]}')
print(f'Municipio: {dicionario_covid["Teresina"][municipio]}')
print(f'Região de Saúde: {dicionario_covid["Teresina"][nome_regiao_saude]}')
print(f'Data: {dicionario_covid["Teresina"][data]}')
print(f'Casos Acumulados: {dicionario_covid["Teresina"][casos_acumulados]}')
print(f'Casos Novos: {dicionario_covid["Teresina"][casos_novos]}')
print(f'Obitos Acumulados: {dicionario_covid["Teresina"][obitos_acumulados]}')
print(f'Obitos Novos: {dicionario_covid["Teresina"][obitos_novos]}')