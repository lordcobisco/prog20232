import pandas as pd 

#regiao[0]	estado[1]	municipio[2]	coduf[3]	codmun[4]	codRegiaoSaude[5]	nomeRegiaoSaude[6]	data[7]	semanaEpi[8]	populacaoTCU2019[9]	casosAcumulado[10]	casosNovos[11]	obitosAcumulado[12]	obitosNovos[13]	interior/metropolitana[14]


#Foram pegos dados 3 regiões aleatórias dos 26 estados do brasil na data de 01/01/2022
lista_estados=[

['Norte', 'AC', 'Acrelândia', 12, 120001, 12002, 'BAIXO ACRE E PURUS', '01/01/2022', 52, 15256, 1798, 0, 37, 0, 0],
['Norte', 'AC', 'Assis Brasil', 12, 120005, 12001, 'ALTO ACRE', '01/01/2022', 52, 7417, 1827, 0, 24, 0, 0],
['Norte', 'AC','Cruzeiro do Sul',12,120020,12003,'JURUA E TARAUACA/ENVIRA','01/01/2022',52,88376,7920,0,169,0,0],
['Norte','AM','Amaturá',13,113000613009,'ALTO SOLIMOES','01/01/2022',52,11536,2406,0,18,0,0],
['Norte', 'AM', 'Alvarães', 13, 130002, 13008, 'TRIANGULO', '01/01/2022', 52, 16041, 2918, 1, 46, 0, 0],
['Norte', 'AM', 'Autazes', 13, 130030, 13001, 'MANAUS, ENTORNO E ALTO RIO NEGRO', '01/01/2022', 52, 39565, 3333, 0, 96, 0, 1],
['Norte', 'AP', 'Serra do Navio', 16, 160005, 16001, 'AREA CENTRAL', '01/01/2022', 52, 5397, 1340, 0, 5, 0, 0],
['Norte', 'AP', 'Amapá', 16, 160010, 16002, 'AREA NORTE', '01/01/2022', 52, 9109, 1428, 0, 13, 0, 0],
['Norte', 'AP', 'Laranjal do Jari', 16, 160027, 16003, 'AREA SUDOESTE', '01/01/2022', 52, 50410, 8403, 0, 95, 0, 0],
['Norte', 'PA', 'Abaetetuba', 15, 150010, 15011, 'TOCANTINS', '01/01/2022', 52, 157698, 9924, 0, 226, 0, 0],
['Norte', 'PA', 'Alenquer', 15, 150040, 15002, 'BAIXO AMAZONAS', '01/01/2022', 52, 56789, 3901, 0, 148, 0, 0],
['Norte', 'PA', 'Ananindeua', 15, 150080, 15006, 'METROPOLITANA I', '01/01/2022', 52, 530598, 26851, 0, 834, 0, 1],
['Norte', 'RO', 'Alta Floresta D.Oeste', 11, 110001, 11005, 'ZONA DA MATA', '01/01/2022', 52, 22945, 4668, 0, 72, 0, 0],
['Norte', 'RO', 'Jaru', 11, 110011, 11003, 'CENTRAL', '01/01/2022', 52, 51775, 8513, 0, 189, 0, 0],
['Norte', 'RO', 'Costa Marques', 11, 110008, 11007, 'VALE DO GUAPORE', '01/01/2022', 52, 18331, 2217, 0, 42, 0, 0],
['Norte', 'RR', 'Amajari', 14, 140002, 14001, 'CENTRO NORTE', '01/01/2022', 52, 12796, 1186, 0, 25, 0, 0],
['Norte', 'RR', 'Caracaraí', 14, 140020, 14002, 'SUL', '01/01/2022', 52, 21926, 2724, 0, 61, 0, 0],
['Norte', 'TO', 'Abreulândia', 17, 170025, 17007, 'CANTAO', '01/01/2022', 52, 2579, 332, 0, 8, 0, 0],
['Norte', 'TO', 'Aguiarnópolis', 17, 170030, 17002, 'BICO DO PAPAGAIO', '01/01/2022', 52, 6733, 720, 0, 14, 0, 0],
['Norte', 'TO', 'Aragominas', 17, 170130, 17001, 'MEDIO NORTE ARAGUAIA', '01/01/2022', 52, 5758, 581, 0, 11, 0, 0],
['Nordeste', 'PB', 'Água Branca', 25, 250010, 25011, '11ª REGIAO', '01/01/2022', 52, 10234, 1215, 1, 14, 0, 0],
['Nordeste', 'PB', 'Aparecida', 25, 250077, 25010, '10ª REGIAO', '01/01/2022', 52, 8347, 1094, 0, 14, 0, 0],
['Nordeste', 'PB', 'São João do Rio do Peixe', 25, 250070, 25009, '9ª REGIAO', '01/01/2022', 52, 18034, 1598, 0, 35, 0, 0],
['Nordeste', 'PE', 'Abreu e Lima', 26, 260005, 26010, 'RECIFE', '01/01/2022', 52, 99990, 3713, 0, 252, 0, 1],
['Nordeste', 'PE', 'Afogados da Ingazeira', 26, 260010, 26001, 'AFOGADOS DA INGAZEIRA', '01/01/2022', 52, 37259, 5300, 5, 75, 0, 0],
['Nordeste', 'PE', 'Afogados da Ingazeira', 26, 260010, 26001, 'AFOGADOS DA INGAZEIRA', '01/01/2022', 52, 37259, 5300, 5, 75, 0, 0],
['Nordeste', 'PI', 'Acauã', 22, 220005, 22009, 'VALE DO RIO GUARIBAS', '01/01/2022', 52, 7084, 219, 0, 2, 0, 0],
['Nordeste', 'PI', 'Assunção do Piauí', 22, 220105, 22001, 'CARNAUBAIS', '01/01/2022', 52, 7846, 404, 0, 9, 0, 0],
['Nordeste', 'PI', 'Alvorada do Gurguéia', 22, 220045, 22002, 'CHAPADA DAS MANGABEIRAS', '01/01/2022', 52, 5419, 453, 0, 12, 0, 0],
['Nordeste', 'RN', 'Acari', 24, 240010, 24004, '4ª REGIAO DE SAUDE - CAICO', '01/01/2022', 52, 11136, 1148, 0, 21, 0, 0],
['Nordeste', 'RN', 'Parnamirim', 24, 240325, 24007, '7ª REGIAO DE SAUDE - METROPOLITANA', '01/01/2022', 52, 261469, 33364, 11, 551, 0, 1],
['Nordeste', 'RN', 'Apodi', 24, 240100, 24002, '2ª REGIAO DE SAUDE - MOSSORO', '01/01/2022', 52, 35845, 6662, 0, 97, 0, 0],
['Nordeste', 'SE', 'Amparo de São Francisco', 28, 280010, 28007, 'PROPRIA', '01/01/2022', 52, 2374, 256, 0, 5, 0, 0],
['Nordeste', 'SE', 'Capela', 28, 280130, 28006, 'NOSSA SENHORA DO SOCORRO', '01/01/2022', 52, 34213, 2882, 0, 45, 0, 0],
['Nordeste', 'SE', 'Lagarto', 28, 280350, 28004, 'LAGARTO', '01/01/2022', 52, 104408, 7859, 2, 222, 0, 0],
['Nordeste', 'BA', 'Abaíra', 29, 290010, 29023, 'SEABRA', '01/01/2022', 52, 8739, 301, 0, 13, 0, 0],
['Nordeste', 'BA', 'Candeias', 29, 290650, 29020, 'SALVADOR', '01/01/2022', 52, 87076, 8381, 0, 195, 0, 1],
['Nordeste', 'BA', 'Érico Cardoso', 29, 290050, 29003, 'BRUMADO', '01/01/2022', 52, 10610, 333, 0, 5, 0, 0],
['Nordeste', 'CE', 'Abaiara', 23, 230010, 23019, '19ª REGIAO BREJO SANTO', '01/01/2022', 52, 11737, 641, 0, 17, 0, 0],
['Nordeste', 'CE', 'Alto Santo', 23, 230070, 23010, '10ª REGIAO LIMOEIRO DO NORTE', '01/01/2022', 52, 17146, 1954, 1, 35, 0, 0],
['Nordeste', 'CE', 'Jaguaretama', 23, 230670, 23009, '9ª REGIAO RUSSAS', '01/01/2022', 52, 18162, 1993, 0, 44, 0, 0],
['Nordeste', 'CE', 'Banabuiú', 23, 230185, 23008, '8ª REGIAO QUIXADA', '01/01/2022', 52, 18197, 2366, 0, 22, 0, 0],
['Nordeste', 'AL', 'Água Branca', 27, 270010, 27010, '10ª REGIAO DE SAUDE', '01/01/2022', 52, 20196, 555, 0, 24, 0, 0],
['Nordeste', 'AL', 'Canapi', 27, 270160, 27009, '9ª REGIAO DE SAUDE', '01/01/2022', 52, 17722, 448, 0, 12, 0, 0],
['Nordeste', 'AL', 'Belém', 27, 270080, 27008, '8ª REGIAO DE SAUDE', '01/01/2022', 52, 4344, 129, 0, 8, 0, 0],
['Nordeste', 'MA', 'Açailândia', 21, 210005, 21001, 'ACAILANDIA', '01/01/2022', 52, 112445, 5984, 0, 261, 0, 0],
['Nordeste', 'MA', 'Apicum-Açu', 21, 210083, 21011, 'PINHEIRO', '01/01/2022', 52, 17239, 605, 0, 11, 0, 0],
['Nordeste', 'MA', 'Altamira do Maranhão', 21, 210040, 21002, 'BACABAL', '01/01/2022', 52, 8128, 406, 0, 13, 0, 0],
['Sudeste', 'MG', 'Abadia dos Dourados', 31, 310010, 31074, 'PATROCINIO / MONTE CARMELO', '01/01/2022', 52, 6989, 601, 0, 20, 0, 0],
['Sudeste', 'MG', 'Contagem', 31, 311860, 31018, 'CONTAGEM', '01/01/2022', 52, 663855, 49414, 19, 1940, 0, 1],
['Sudeste', 'MG', 'Araguari', 31, 310350, 31075, 'UBERLANDIA / ARAGUARI', '01/01/2022', 52, 117267, 20183, 0, 474, 0, 0],
['Sudeste', 'SP', 'Adamantina', 35, 350010, 35091, 'ADAMANTINA', '01/01/2022', 52, 35068, 4131, 0, 148, 0, 0],
['Sudeste', 'SP', 'Águas de Lindóia', 35, 350050, 35074, 'CIRCUITO DAS AGUAS', '01/01/2022', 52, 18705, 2115, 0, 53, 0, 0],
['Sudeste', 'SP', 'Águas de São Pedro', 35, 350060, 35103, 'PIRACICABA', '01/01/2022', 52, 3451, 461, 0, 12, 0, 0],
['Centro-Oeste', 'DF', 'Brasília', 53, 530010, 53001, 'DISTRITO FEDERAL', '01/01/2022', 52, 3015268, 519811, 0, 11108, 0, 1],
['Centro-Oeste', 'GO', 'Abadia de Goiás', 52, 520005, 52001, 'CENTRAL', '01/01/2022', 52, 8773, 2003, 1, 44, 0, 1],
['Centro-Oeste', 'GO', 'Bonópolis', 52, 520357, 52008, 'NORTE', '01/01/2022', 52, 4405, 352, 0, 3, 0, 0],
['Centro-Oeste', 'GO', 'Água Limpa', 52, 520020, 52017, 'SUL', '01/01/2022', 52, 1850, 207, 0, 4, 0, 0],
['Centro-Oeste', 'MS', 'Água Clara', 50, 500020, 50004, 'TRES LAGOAS', '01/01/2022', 52, 15522, 2947, 0, 67, 0, 0],
['Centro-Oeste', 'MS', 'Alcinópolis', 50, 500025, 50001, 'CAMPO GRANDE', '01/01/2022', 52, 5343, 422, 0, 11, 0, 0],
['Centro-Oeste', 'MS', 'Amambai', 50, 500060, 50003, 'DOURADOS', '01/01/2022', 52, 39396, 3568, 1, 86, 0, 0],
['Centro-Oeste', 'MT', 'Acorizal', 51, 510010, 51002, 'BAIXADA CUIABANA', '01/01/2022', 52, 5399, 807, 0, 22, 0, 1],
['Centro-Oeste', 'MT', 'Alto Araguaia', 51, 510030, 51013, 'SUL MATOGROSSENSE', '01/01/2022', 52, 19044, 1651, 0, 31, 0, 0],
['Centro-Oeste', 'MT', 'Colíder', 51, 510320, 51010, 'NORTE MATOGROSSENSE', '01/01/2022', 52, 33438, 5902, 0, 149, 0, 0],
['Sudeste', 'ES', 'Afonso Cláudio', 32, 320010, 32002, 'METROPOLITANA', '01/01/2022', 52, 30586, 4268, 0, 73, 0, 0],
['Sudeste', 'ES', 'Águia Branca', 32, 320013, 32001, 'CENTRAL', '01/01/2022', 52, 9642, 2008, 0, 62, 0, 0],
['Sudeste', 'ES', 'Alegre', 32, 320020, 32004, 'SUL', '01/01/2022', 52, 30084, 3519, 0, 81, 0, 0],
['Sudeste', 'RJ', 'Angra dos Reis', 33, 330010, 33001, 'BAIA DA ILHA GRANDE', '01/01/2022', 52, 203785, 18434, 0, 572, 0, 0],
['Sudeste', 'RJ', 'Areal', 33, 330022, 33003, 'CENTRO-SUL', '01/01/2022', 52, 12572, 1661, 0, 51, 0, 0],
['Sudeste', 'RJ', 'Belford Roxo', 33, 330045, 33005, 'METROPOLITANA I', '01/01/2022', 52, 510906, 24561, 0, 972, 0, 1],
['Sul', 'PR', 'Abatiá', 41, 410010, 41018, '18ª RS CORNELIO PROCOPIO', '01/01/2022', 52, 7457, 1186, 0, 21, 0, 0],
['Sul', 'PR', 'Anahy', 41, 410105, 41010, '10ª RS CASCAVEL', '01/01/2022', 52, 2801, 470, 0, 13, 0, 0],
['Sul', 'PR', 'Altamira do Paraná', 41, 410045, 41011, '11ª RS CAMPO MOURAO', '01/01/2022', 52, 1942, 312, 0, 13, 0, 0],
['Sul', 'RS', 'Aceguá', 43, 430003, 43022, 'REGIAO 22', '01/01/2022', 52, 4901, 408, 0, 8, 0, 0],
['Sul', 'RS', 'Araricá', 43, 430087, 43007, 'REGIAO 07', '01/01/2022', 52, 5698, 1106, 0, 27, 0, 1],
['Sul', 'RS', 'Bossoroca', 43, 430250, 43011, 'REGIAO 11', '01/01/2022', 52, 6279, 510, 0, 22, 0, 0],
['Sul', 'SC', 'Abdon Batista', 42, 420005, 42008, 'MEIO OESTE', '01/01/2022', 52, 2563, 409, 0, 4, 0, 0],
['Sul', 'SC', 'Águas Mornas', 42, 420060, 42007, 'GRANDE FLORIANOPOLIS', '01/01/2022', 52, 6469, 766, 0, 10, 0, 1],
['Sul', 'SC', 'Araranguá', 42, 420140, 42014, 'EXTREMO SUL CATARINENSE', '01/01/2022', 52, 68228, 11543, 3, 259, 0, 0]

]

tupla_estados=[

('Norte', 'AC', 'Acrelândia', 12, 120001, 12002, 'BAIXO ACRE E PURUS', '01/01/2022', 52, 15256, 1798, 0, 37, 0, 0),
('Norte', 'AC', 'Assis Brasil', 12, 120005, 12001, 'ALTO ACRE', '01/01/2022', 52, 7417, 1827, 0, 24, 0, 0),
('Norte', 'AC', 'Cruzeiro do Sul', 12, 120020, 12003, 'JURUA E TARAUACA/ENVIRA', '01/01/2022', 52, 88376, 7920, 0, 169, 0, 0),
('Norte','AM','Amaturá',13,113000613009,'ALTO SOLIMOES','01/01/2022',52,11536,2406,0,18,0,0),
('Norte', 'AM', 'Alvarães', 13, 130002, 13008, 'TRIANGULO', '01/01/2022', 52, 16041, 2918, 1, 46, 0, 0),
('Norte', 'AM', 'Autazes', 13, 130030, 13001, 'MANAUS, ENTORNO E ALTO RIO NEGRO', '01/01/2022', 52, 39565, 3333, 0, 96, 0, 1),
('Norte', 'AP', 'Serra do Navio', 16, 160005, 16001, 'AREA CENTRAL', '01/01/2022', 52, 5397, 1340, 0, 5, 0, 0),
('Norte', 'AP', 'Amapá', 16, 160010, 16002, 'AREA NORTE', '01/01/2022', 52, 9109, 1428, 0, 13, 0, 0),
('Norte', 'AP', 'Laranjal do Jari', 16, 160027, 16003, 'AREA SUDOESTE', '01/01/2022', 52, 50410, 8403, 0, 95, 0, 0),
('Norte', 'PA', 'Abaetetuba', 15, 150010, 15011, 'TOCANTINS', '01/01/2022', 52, 157698, 9924, 0, 226, 0, 0),
('Norte', 'PA', 'Alenquer', 15, 150040, 15002, 'BAIXO AMAZONAS', '01/01/2022', 52, 56789, 3901, 0, 148, 0, 0),
('Norte', 'PA', 'Ananindeua', 15, 150080, 15006, 'METROPOLITANA I', '01/01/2022', 52, 530598, 26851, 0, 834, 0, 1),
('Norte', 'RO', 'Alta Floresta D.Oeste', 11, 110001, 11005, 'ZONA DA MATA', '01/01/2022', 52, 22945, 4668, 0, 72, 0, 0),
('Norte', 'RO', 'Jaru', 11, 110011, 11003, 'CENTRAL', '01/01/2022', 52, 51775, 8513, 0, 189, 0, 0),
('Norte', 'RO', 'Costa Marques', 11, 110008, 11007, 'VALE DO GUAPORE', '01/01/2022', 52, 18331, 2217, 0, 42, 0, 0),
('Norte', 'RR', 'Amajari', 14, 140002, 14001, 'CENTRO NORTE', '01/01/2022', 52, 12796, 1186, 0, 25, 0, 0),
('Norte', 'RR', 'Caracaraí', 14, 140020, 14002, 'SUL', '01/01/2022', 52, 21926, 2724, 0, 61, 0, 0),
('Norte', 'TO', 'Abreulândia', 17, 170025, 17007, 'CANTAO', '01/01/2022', 52, 2579, 332, 0, 8, 0, 0),
('Norte', 'TO', 'Aguiarnópolis', 17, 170030, 17002, 'BICO DO PAPAGAIO', '01/01/2022', 52, 6733, 720, 0, 14, 0, 0),
('Norte', 'TO', 'Aragominas', 17, 170130, 17001, 'MEDIO NORTE ARAGUAIA', '01/01/2022', 52, 5758, 581, 0, 11, 0, 0),
('Nordeste', 'PB', 'Água Branca', 25, 250010, 25011, '11ª REGIAO', '01/01/2022', 52, 10234, 1215, 1, 14, 0, 0),
('Nordeste', 'PB', 'Aparecida', 25, 250077, 25010, '10ª REGIAO', '01/01/2022', 52, 8347, 1094, 0, 14, 0, 0),
('Nordeste', 'PB', 'São João do Rio do Peixe', 25, 250070, 25009, '9ª REGIAO', '01/01/2022', 52, 18034, 1598, 0, 35, 0, 0),
('Nordeste', 'PE', 'Abreu e Lima', 26, 260005, 26010, 'RECIFE', '01/01/2022', 52, 99990, 3713, 0, 252, 0, 1),
('Nordeste', 'PE', 'Afogados da Ingazeira', 26, 260010, 26001, 'AFOGADOS DA INGAZEIRA', '01/01/2022', 52, 37259, 5300, 5, 75, 0, 0),
('Nordeste', 'PE', 'Afogados da Ingazeira', 26, 260010, 26001, 'AFOGADOS DA INGAZEIRA', '01/01/2022', 52, 37259, 5300, 5, 75, 0, 0),
('Nordeste', 'PI', 'Acauã', 22, 220005, 22009, 'VALE DO RIO GUARIBAS', '01/01/2022', 52, 7084, 219, 0, 2, 0, 0),
('Nordeste', 'PI', 'Assunção do Piauí', 22, 220105, 22001, 'CARNAUBAIS', '01/01/2022', 52, 7846, 404, 0, 9, 0, 0),
('Nordeste', 'PI', 'Alvorada do Gurguéia', 22, 220045, 22002, 'CHAPADA DAS MANGABEIRAS', '01/01/2022', 52, 5419, 453, 0, 12, 0, 0),
('Nordeste', 'RN', 'Acari', 24, 240010, 24004, '4ª REGIAO DE SAUDE - CAICO', '01/01/2022', 52, 11136, 1148, 0, 21, 0, 0),
('Nordeste', 'RN', 'Parnamirim', 24, 240325, 24007, '7ª REGIAO DE SAUDE - METROPOLITANA', '01/01/2022', 52, 261469, 33364, 11, 551, 0, 1),
('Nordeste', 'RN', 'Apodi', 24, 240100, 24002, '2ª REGIAO DE SAUDE - MOSSORO', '01/01/2022', 52, 35845, 6662, 0, 97, 0, 0),
('Nordeste', 'SE', 'Amparo de São Francisco', 28, 280010, 28007, 'PROPRIA', '01/01/2022', 52, 2374, 256, 0, 5, 0, 0),
('Nordeste', 'SE', 'Capela', 28, 280130, 28006, 'NOSSA SENHORA DO SOCORRO', '01/01/2022', 52, 34213, 2882, 0, 45, 0, 0),
('Nordeste', 'SE', 'Lagarto', 28, 280350, 28004, 'LAGARTO', '01/01/2022', 52, 104408, 7859, 2, 222, 0, 0),
('Nordeste', 'BA', 'Abaíra', 29, 290010, 29023, 'SEABRA', '01/01/2022', 52, 8739, 301, 0, 13, 0, 0),
('Nordeste', 'BA', 'Candeias', 29, 290650, 29020, 'SALVADOR', '01/01/2022', 52, 87076, 8381, 0, 195, 0, 1),
('Nordeste', 'BA', 'Érico Cardoso', 29, 290050, 29003, 'BRUMADO', '01/01/2022', 52, 10610, 333, 0, 5, 0, 0),
('Nordeste', 'CE', 'Abaiara', 23, 230010, 23019, '19ª REGIAO BREJO SANTO', '01/01/2022', 52, 11737, 641, 0, 17, 0, 0),
('Nordeste', 'CE', 'Alto Santo', 23, 230070, 23010, '10ª REGIAO LIMOEIRO DO NORTE', '01/01/2022', 52, 17146, 1954, 1, 35, 0, 0),
('Nordeste', 'CE', 'Jaguaretama', 23, 230670, 23009, '9ª REGIAO RUSSAS', '01/01/2022', 52, 18162, 1993, 0, 44, 0, 0),
('Nordeste', 'CE', 'Banabuiú', 23, 230185, 23008, '8ª REGIAO QUIXADA', '01/01/2022', 52, 18197, 2366, 0, 22, 0, 0),
('Nordeste', 'AL', 'Água Branca', 27, 270010, 27010, '10ª REGIAO DE SAUDE', '01/01/2022', 52, 20196, 555, 0, 24, 0, 0),
('Nordeste', 'AL', 'Canapi', 27, 270160, 27009, '9ª REGIAO DE SAUDE', '01/01/2022', 52, 17722, 448, 0, 12, 0, 0),
('Nordeste', 'AL', 'Belém', 27, 270080, 27008, '8ª REGIAO DE SAUDE', '01/01/2022', 52, 4344, 129, 0, 8, 0, 0),
('Nordeste', 'MA', 'Açailândia', 21, 210005, 21001, 'ACAILANDIA', '01/01/2022', 52, 112445, 5984, 0, 261, 0, 0),
('Nordeste', 'MA', 'Apicum-Açu', 21, 210083, 21011, 'PINHEIRO', '01/01/2022', 52, 17239, 605, 0, 11, 0, 0),
('Nordeste', 'MA', 'Altamira do Maranhão', 21, 210040, 21002, 'BACABAL', '01/01/2022', 52, 8128, 406, 0, 13, 0, 0),
('Sudeste', 'MG', 'Abadia dos Dourados', 31, 310010, 31074, 'PATROCINIO / MONTE CARMELO', '01/01/2022', 52, 6989, 601, 0, 20, 0, 0),
('Sudeste', 'MG', 'Contagem', 31, 311860, 31018, 'CONTAGEM', '01/01/2022', 52, 663855, 49414, 19, 1940, 0, 1),
('Sudeste', 'MG', 'Araguari', 31, 310350, 31075, 'UBERLANDIA / ARAGUARI', '01/01/2022', 52, 117267, 20183, 0, 474, 0, 0),
('Sudeste', 'SP', 'Adamantina', 35, 350010, 35091, 'ADAMANTINA', '01/01/2022', 52, 35068, 4131, 0, 148, 0, 0),
('Sudeste', 'SP', 'Águas de Lindóia', 35, 350050, 35074, 'CIRCUITO DAS AGUAS', '01/01/2022', 52, 18705, 2115, 0, 53, 0, 0),
('Sudeste', 'SP', 'Águas de São Pedro', 35, 350060, 35103, 'PIRACICABA', '01/01/2022', 52, 3451, 461, 0, 12, 0, 0),
('Centro-Oeste', 'DF', 'Brasília', 53, 530010, 53001, 'DISTRITO FEDERAL', '01/01/2022', 52, 3015268, 519811, 0, 11108, 0, 10),
('Centro-Oeste', 'GO', 'Abadia de Goiás', 52, 520005, 52001, 'CENTRAL', '01/01/2022', 52, 8773, 2003, 1, 44, 0, 1),
('Centro-Oeste', 'GO', 'Bonópolis', 52, 520357, 52008, 'NORTE', '01/01/2022', 52, 4405, 352, 0, 3, 0, 0),
('Centro-Oeste', 'GO', 'Água Limpa', 52, 520020, 52017, 'SUL', '01/01/2022', 52, 1850, 207, 0, 4, 0, 0),
('Centro-Oeste', 'MS', 'Água Clara', 50, 500020, 50004, 'TRES LAGOAS', '01/01/2022', 52, 15522, 2947, 0, 67, 0, 0),
('Centro-Oeste', 'MS', 'Alcinópolis', 50, 500025, 50001, 'CAMPO GRANDE', '01/01/2022', 52, 5343, 422, 0, 11, 0, 0),
('Centro-Oeste', 'MS', 'Amambai', 50, 500060, 50003, 'DOURADOS', '01/01/2022', 52, 39396, 3568, 1, 86, 0, 0),
('Centro-Oeste', 'MT', 'Acorizal', 51, 510010, 51002, 'BAIXADA CUIABANA', '01/01/2022', 52, 5399, 807, 0, 22, 0, 1),
('Centro-Oeste', 'MT', 'Alto Araguaia', 51, 510030, 51013, 'SUL MATOGROSSENSE', '01/01/2022', 52, 19044, 1651, 0, 31, 0, 0),
('Centro-Oeste', 'MT', 'Colíder', 51, 510320, 51010, 'NORTE MATOGROSSENSE', '01/01/2022', 52, 33438, 5902, 0, 149, 0, 0),
('Sudeste', 'ES', 'Afonso Cláudio', 32, 320010, 32002, 'METROPOLITANA', '01/01/2022', 52, 30586, 4268, 0, 73, 0, 0),
('Sudeste', 'ES', 'Águia Branca', 32, 320013, 32001, 'CENTRAL', '01/01/2022', 52, 9642, 2008, 0, 62, 0, 0),
('Sudeste', 'ES', 'Alegre', 32, 320020, 32004, 'SUL', '01/01/2022', 52, 30084, 3519, 0, 81, 0, 0),
('Sudeste', 'RJ', 'Angra dos Reis', 33, 330010, 33001, 'BAIA DA ILHA GRANDE', '01/01/2022', 52, 203785, 18434, 0, 572, 0, 0),
('Sudeste', 'RJ', 'Areal', 33, 330022, 33003, 'CENTRO-SUL', '01/01/2022', 52, 12572, 1661, 0, 51, 0, 0),
('Sudeste', 'RJ', 'Belford Roxo', 33, 330045, 33005, 'METROPOLITANA I', '01/01/2022', 52, 510906, 24561, 0, 972, 0, 1),
('Sul', 'PR', 'Abatiá', 41, 410010, 41018, '18ª RS CORNELIO PROCOPIO', '01/01/2022', 52, 7457, 1186, 0, 21, 0, 0),
('Sul', 'PR', 'Anahy', 41, 410105, 41010, '10ª RS CASCAVEL', '01/01/2022', 52, 2801, 470, 0, 13, 0, 0),
('Sul', 'PR', 'Altamira do Paraná', 41, 410045, 41011, '11ª RS CAMPO MOURAO', '01/01/2022', 52, 1942, 312, 0, 13, 0, 0),
('Sul', 'RS', 'Aceguá', 43, 430003, 43022, 'REGIAO 22', '01/01/2022', 52, 4901, 408, 0, 8, 0, 0),
('Sul', 'RS', 'Araricá', 43, 430087, 43007, 'REGIAO 07', '01/01/2022', 52, 5698, 1106, 0, 27, 0, 1),
('Sul', 'RS', 'Bossoroca', 43, 430250, 43011, 'REGIAO 11', '01/01/2022', 52, 6279, 510, 0, 22, 0, 0),
('Sul', 'SC', 'Abdon Batista', 42, 420005, 42008, 'MEIO OESTE', '01/01/2022', 52, 2563, 409, 0, 4, 0, 0),
('Sul', 'SC', 'Águas Mornas', 42, 420060, 42007, 'GRANDE FLORIANOPOLIS', '01/01/2022', 52, 6469, 766, 0, 10, 0, 1),
('Sul', 'SC', 'Araranguá', 42, 420140, 42014, 'EXTREMO SUL CATARINENSE', '01/01/2022', 52, 68228, 11543, 3, 259, 0, 0)

]

# B- Mande printar na tela o número de casos acumulados para o estado do rio de janeiro tanto para a tupla quanto para a lista.

Casos_acumulados_RJ = lista_estados[67][10]+lista_estados[68][10]+lista_estados[69][10]
print(Casos_acumulados_RJ)

Casos_acumulados_RJ_tupla= tupla_estados[67][10] + tupla_estados[68][10] + tupla_estados[69][10]
print(Casos_acumulados_RJ_tupla)

# C- Apresente na tela todos os óbitos acumulados mostrando os casos apenas para o caso dos estados (sem mostrar regiões de saúde, etc..).

for i in lista_estados:
    print(i[0], i[10])

# #Assuma que os dados de óbitos novos para o estado da paraíba estejam errados em 10 unidades para menos. Sobrescreva a informação tanto na lista quanto na tupla,corrigindo os dados.


lista_estados[20].insert(13,-10)
print(type(-10))
lista_estados[21].insert(13,-10)
lista_estados[22].insert(13,-10)

# # tupla_estados[20].insert(13,-10)
# # tupla_estados[21].insert(13,-10)
# # tupla_estados[22].insert(13,-10)

#Crie uma nova lista com apenas dados de 1 estado e todos os municípios e adicione essa lista nova a lista já existente (append ou insert).

nova_lista=[
["Norte", "AC", "Brasiléia", 12, 120010, 12001, "ALTO ACRE", "01/01/2022", 52, 26278, 3016, 0, 44, 0, 0],
["Norte", "AC", "Bujari", 12, 120013, 12002, "BAIXO ACRE E PURUS", "01/01/2022", 52, 10266, 1153, 0, 17, 0, 0],
["Norte", "AC", "Capixaba", 12, 120017, 12002, "BAIXO ACRE E PURUS", "01/01/2022", 52, 11733, 675, 0, 17, 0, 0],
["Norte", "AC", "Epitaciolândia", 12, 120025, 12001, "ALTO ACRE", "01/01/2022", 52, 18411, 1594, 0, 36, 0, 0],
["Norte", "AC", "Feijó", 12, 120030, 12003, "JURUA E TARAUACA/ENVIRA", "01/01/2022", 52, 34780, 3338, 0, 63, 0, 0],
["Norte", "AC", "Jordão", 12, 120032, 12002, "BAIXO ACRE E PURUS", "01/01/2022", 52, 8317, 706, 0, 2, 0, 0],
["Norte", "AC", "Mâncio Lima", 12, 120033, 12003, "JURUA E TARAUACA/ENVIRA", "01/01/2022", 52, 18977, 2992, 0, 32, 0, 0],
["Norte", "AC", "Manoel Urbano", 12, 120034, 12002, "BAIXO ACRE E PURUS", "01/01/2022", 52, 9459, 907, 0, 14, 0, 0],
["Norte", "AC", "Marechal Thaumaturgo", 12, 120035, 12003, "JURUA E TARAUACA/ENVIRA", "01/01/2022", 52, 18867, 1370, 0, 13, 0, 0],
["Norte", "AC", "Plácido de Castro", 12, 120038, 12002, "BAIXO ACRE E PURUS", "01/01/2022", 52, 19761, 1796, 0, 20, 0, 0],
["Norte", "AC", "Porto Walter", 12, 120039, 12003, "JURUA E TARAUACA/ENVIRA", "01/01/2022", 52, 11982, 554, 1, 6, 0, 0],
["Norte", "AC", "Rio Branco", 12, 120040, 12002, "BAIXO ACRE E PURUS", "01/01/2022", 52, 407319, 38392, 1, 1095, 0, 1],
["Norte", "AC", "Rodrigues Alves", 12, 120042, 12003, "JURUA E TARAUACA/ENVIRA", "01/01/2022", 52, 18930, 1016, 0, 14, 0, 0],
["Norte", "AC", "Santa Rosa do Purus", 12, 120043, 12002, "BAIXO ACRE E PURUS", "01/01/2022", 52, 6540, 1014, 0, 7, 0, 0],
["Norte", "AC", "Senador Guiomard", 12, 120045, 12002, "BAIXO ACRE E PURUS", "01/01/2022", 52, 23024, 1207, 0, 42, 0, 0],
["Norte", "AC", "Sena Madureira", 12, 120050, 12002, "BAIXO ACRE E PURUS", "01/01/2022", 52, 45848, 5894, 0, 83, 0, 0],
["Norte", "AC", "Tarauacá", 12, 120060, 12003, "JURUA E TARAUACA/ENVIRA", "01/01/2022", 52, 42567, 6609, 0, 47, 0, 0],
["Norte", "AC", "Xapuri", 12, 120070, 12001, "ALTO ACRE", "01/01/2022", 52, 19323, 3054, 0, 31, 0, 0],
["Norte", "AC", "Porto Acre", 12, 120080, 12002, "BAIXO ACRE E PURUS", "01/01/2022", 52, 18504, 1554, 0, 38, 0, 0]
]




#Adiciona nova lista
lista_estados+=nova_lista
total_lista=len(lista_estados)
print(total_lista)

##Exclui regiões de saude 

for lista in lista_estados:
    del lista[6]
#Verifique qual é o maior valor numérico de óbitos novos e o menor valor numérico de óbitos novos  


max=float()

for lista in lista_estados:
    if max < lista[12]:
        max= lista[12]
print(max)


max=float()

for lista in lista_estados:
    if max > lista[12]:
        max= lista[12]       
print(max)

#Crie um dicionário de forma que seja possível encontrar os municípios associados a um estado específico e extrair os dados de casos novos em apenas um comando.

dicionario= {"Região":["Norte"],"Estado":["AC"],"Municipio":["Porto Acre"],"coduf":[12],"codmun": [120080],"codRegiaoSaude":[12002],"nomeRegiaoSaude": ["BAIXO ACRE E PURUS"],"data":["01/01/2022"], "Semanaepi":[52],"populaçãoTCI2019": [18504], "casoacumulado":[1554], "casosnovos":[0], "obitosacumulados":[38], "obtosnovos":[0],"interior/metropolitana":[0]}

#Extraia os dados de Teresina/PI apresentando os casos novos com um print.
#Observação, não acrescentei o municipio de teresina/PI, por isso utilizo outro estado.

print(dicionario['Municipio'],dicionario['casosnovos'])

