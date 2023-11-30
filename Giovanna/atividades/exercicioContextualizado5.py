# lista
dataBaseLista = [
    # 0 regiao; 1 estado; 2 municipio; 3 coduf; 4 codmun; 5 codRegiaoSaude; 6 nomeRegiaoSaude; 7 data; 8 semanaEpi; 9 populacaoTCU2019; 10 casosAcumulado; 11 casosNovos; 12 obitosAcumulado; 13 obitosNovos; 14 Recuperadosnovos
    ["Norte", "AP", "Serra do Navio", 16, 160005, 16001, "AREA CENTRAL", "2023-01-01", 1, 5397, 1996, 0, 5, 0, 0],
    ["Norte", "PA", "Bom Jesus do Tocantins", 15, 150157, 15003, "CARAJAS", "2023-06-25", 26, 16981, 1436, 0, 29, 0, 0],
    ["Norte", "TO", "Almas", 17, 170040, 17003, "SUDESTE", "2022-08-03", 31, 7055, 324, 1, 5, 0, 0],
    ["Norte", "RO", "São Francisco do Guaporé", 11, 110149, 11007, "VALE DO GUAPORE", "2022-07-02", 26, 20266, 5341, 9, 58, 0, 0],
    ["Norte", "AC", "Acrelândia", 12, 120001, 12002, "BAIXO ACRE E PURUS", "2022-07-02", 26, 15256, 2907, 1, 40, 0, 0],
    ["Norte", "RR", "Amajari", 14, 140002, 14001, "CENTRO Norte", "2022-08-30", 35, 12796, 1447, 3, 26, 0, 0],

    ["Nordeste", "RN", "Acari", 24, 240010, 24004, "4ª REGIAO DE SAUDE - CAICO", "2023-01-01", 1, 11136, 1494, 0, 26, 0, 0],
    ["Nordeste", "PB", "Água Branca", 25, 250010, 25011, "11ª REGIAO", "2023-03-16", 11, 10234, 2201, 0, 16, 20, 0],
    ["Nordeste", "PI", "Wall Ferraz", 22, 221170, 22009, "VALE DO RIO GUARIBAS", "2022-12-31", 52, 4462, 338, 0, 3, 0, 0],
    ["Nordeste", "PE", "Gravatá", 26, 260640, 26003, "CARUARU", "2022-08-01", 31, 84074, 10575, 0, 167, 0, 0],
    ["Nordeste", "CE", "Potengi", 23, 231120, 23020, "20ª REGIAO CRATO", "2022-07-13", 28, 11045, 924, 3, 7, 0, 0],
    ["Nordeste", "MA", "Santa Helena", 21, 210980, 21011, "PINHEIRO", "2022-07-15", 28, 42130, 2252, 0, 32, 0, 0],
    ["Nordeste", "AL", "Olho d'Água das Flores", 27, 270570, 27009, "9ª REGIAO DE SAUDE", "2022-11-09", 45, 21688, 2054, 0, 44, 0, 0],
    ["Nordeste", "SE", "Rosário do Catete", 28, 280610, 28006, "NOSSA SENHORA DO SOCORRO", "2022-08-16", 33, 10855, 1221, 0, 22, 0, 0],
    ["Nordeste", "BA", "Barra do Rocha", 29, 290310, 29015, "JEQUIE", "2022-11-16", 46, 5714, 788, 0, 8, 0, 0],
    
    ["Sudeste", "SP", "Pardinho", 35, 353610, 35063, "POLO CUESTA", "2022-11-27", 48, 6435, 1205, 0, 19, 0, 0],
    ["Sudeste", "MG", "Itaú de Minas", 31, 313375, 31092, "PASSOS", "2022-10-02", 40, 16108, 5762, 0, 49, 0, 0],
    ["Sudeste", "ES", "Itapemirim", 32, 320280, 32004, "SUL", "2022-12-04", 49, 34348, 10462, 1, 179, 0, 0],
    ["Sudeste", "RJ", "Rio de Janeiro", 33, 330455, 33005, "METROPOLITANA I", "2022-12-27", 52, 6718903, 1280519, 1150, 37891, 3, 1],

    ["Sul", "PR", "Palotina", 41, 411790, 41020, "20ª RS TOLEDO", "2022-10-25", 43, 31846, 10741, 0, 104, 0, 0],
    ["Sul", "SC", "Garopaba", 42, 420570, 42007, "GRANDE FLORIANOPOLIS", "2022-11-13", 46, 23078, 6985, 0, 55, 0, 0],
    ["Sul", "RS", "Cândido Godói", 43, 430430, 43014, "REGIAO 14", "2022-11-16", 46, 6198, 1332, 0, 5, 0, 0],

    ["Centro-Oeste", "GO", "Caçu", 52, 520430, 52015, "SUDOESTE I", "2022-09-19", 38, 16009, 3001, -3, 46, 0, 0],
    ["Centro-Oeste", "DF", "Brasília", 53, 530010, 53001, "DISTRITO FEDERAL", "2022-12-20", 51, 3015268, 880172, 1193, 11837, 0, 1],
    ["Centro-Oeste", "MT", "Barra do Garças", 51, 510180, 51005, "GARCAS ARAGUAIA", "2022-07-17", 29, 61012, 15993, 0, 407, 0, 0],
    ["Centro-Oeste", "MS", "Ivinhema", 50, 500470, 50003, "DOURADOS", "2022-12-20", 51, 23187, 8050, 47, 79, 2, 0]
]

# tupla 
dataBaseTupla = (
    # 0 regiao; 1 estado; 2 municipio; 3 coduf; 4 codmun; 5 codRegiaoSaude; 6 nomeRegiaoSaude; 7 data; 8 semanaEpi; 9 populacaoTCU2019; 10 casosAcumulado; 11 casosNovos; 12 obitosAcumulado; 13 obitosNovos;Recuperadosnovos;emAcompanhamentoNovos;interior/metropolitana
    ("Norte", "AM", "Presidente Figueiredo", 13, 130353, 13001, "MANAUS", "ENTORNO E ALTO RIO NEGRO", "2023-04-05", 14, 36279, 8603, 0, 123, 0 , 1),
    ("Norte", "AP", "Serra do Navio", 16, 160005, 16001, "AREA CENTRAL", "2023-01-01", 1, 5397, 1996, 0, 5, 0, 0),
    ("Norte", "PA", "Bom Jesus do Tocantins", 15, 150157, 15003, "CARAJAS", "2023-06-25", 26, 16981, 1436, 0, 29, 0, 0),
    ("Norte", "TO", "Almas", 17, 170040, 17003, "SUDESTE", "2022-08-03", 31, 7055, 324, 1, 5, 0, 0),
    ("Norte", "RO", "São Francisco do Guaporé", 11, 110149, 11007, "VALE DO GUAPORE", "2022-07-02", 26, 20266, 5341, 9, 58, 0, 0),
    ("Norte", "AC", "Acrelândia", 12, 120001, 12002, "BAIXO ACRE E PURUS", "2022-07-02", 26, 15256, 2907, 1, 40, 0, 0),
    ("Norte", "RR", "Amajari", 14, 140002, 14001, "CENTRO Norte", "2022-08-30", 35, 12796, 1447, 3, 26, 0, 0),

    ("Nordeste", "RN", "Acari", 24, 240010, 24004, "4ª REGIAO DE SAUDE - CAICO", "2023-01-01", 1, 11136, 1494, 0, 26, 0, 0),
    ("Nordeste", "PB", "Água Branca", 25, 250010, 25011, "11ª REGIAO", "2023-03-16", 11, 10234, 2201, 0, 16, 20, 0),
    ("Nordeste", "PI", "Wall Ferraz", 22, 221170, 22009, "VALE DO RIO GUARIBAS", "2022-12-31", 52, 4462, 338, 0, 3, 0, 0),
    ("Nordeste", "PE", "Gravatá", 26, 260640, 26003, "CARUARU", "2022-08-01", 31, 84074, 10575, 0, 167, 0, 0),
    ("Nordeste", "CE", "Potengi", 23, 231120, 23020, "20ª REGIAO CRATO", "2022-07-13", 28, 11045, 924, 3, 7, 0, 0),
    ("Nordeste", "MA", "Santa Helena", 21, 210980, 21011, "PINHEIRO", "2022-07-15", 28, 42130, 2252, 0, 32, 0, 0),
    ("Nordeste", "AL", "Olho d'Água das Flores", 27, 270570, 27009, "9ª REGIAO DE SAUDE", "2022-11-09", 45, 21688, 2054, 0, 44, 0, 0),
    ("Nordeste", "SE", "Rosário do Catete", 28, 280610, 28006, "NOSSA SENHORA DO SOCORRO", "2022-08-16", 33, 10855, 1221, 0, 22, 0, 0),
    ("Nordeste", "BA", "Barra do Rocha", 29, 290310, 29015, "JEQUIE", "2022-11-16", 46, 5714, 788, 0, 8, 0, 0),
    
    ("Sudeste", "SP", "Pardinho", 35, 353610, 35063, "POLO CUESTA", "2022-11-27", 48, 6435, 1205, 0, 19, 0, 0),
    ("Sudeste", "MG", "Itaú de Minas", 31, 313375, 31092, "PASSOS", "2022-10-02", 40, 16108, 5762, 0, 49, 0, 0),
    ("Sudeste", "ES", "Itapemirim", 32, 320280, 32004, "SUL", "2022-12-04", 49, 34348, 10462, 1, 179, 0, 0),
    ("Sudeste", "RJ", "Rio de Janeiro", 33, 330455, 33005, "METROPOLITANA I", "2022-12-27", 52, 6718903, 1280519, 1150, 37891, 3, 1),

    ("Sul", "PR", "Palotina", 41, 411790, 41020, "20ª RS TOLEDO", "2022-10-25", 43, 31846, 10741, 0, 104, 0, 0),
    ("Sul", "SC", "Garopaba", 42, 420570, 42007, "GRANDE FLORIANOPOLIS", "2022-11-13", 46, 23078, 6985, 0, 55, 0, 0),
    ("Sul", "RS", "Cândido Godói", 43, 430430, 43014, "REGIAO 14", "2022-11-16", 46, 6198, 1332, 0, 5, 0, 0),

    ("Centro-Oeste", "GO", "Caçu", 52, 520430, 52015, "SUDOESTE I", "2022-09-19", 38, 16009, 3001, -3, 46, 0, 0),
    ("Centro-Oeste", "DF", "Brasília", 53, 530010, 53001, "DISTRITO FEDERAL", "2022-12-20", 51, 3015268, 880172, 1193, 11837, 0, 1),
    ("Centro-Oeste", "MT", "Barra do Garças", 51, 510180, 51005, "GARCAS ARAGUAIA", "2022-07-17", 29, 61012, 15993, 0, 407, 0, 0),
    ("Centro-Oeste", "MS", "Ivinhema", 50, 500470, 50003, "DOURADOS", "2022-12-20", 51, 23187, 8050, 47, 79, 2, 0)
)

# printar na tela o número de casos acumulados para o estado do rio de janeiro tanto para a tupla quanto para a lista
print(dataBaseLista[19][10])
print(dataBaseTupla[19][10])

# printar na tela todos os óbitos acumulados mostrando os casos apenas para o caso dos estados (sem mostrar regiões de saúde, etc..).
for dados in dataBaseLista:
    print(dados[1], " - Total de óbitos acumulados: ", dados[12])

# Assuma que os dados de óbitos novos para o estado da paraíba estejam errados em 10 unidades para menos. Sobrescreva a informação tanto na lista quanto na tupla, corrigindo os dados. 
dataBaseLista[8][12] += 10
# dataBaseTupla[8][13] += 10 para tupla não é possível alterar o valor

# Retorne o tamanho total da lista
print("O tamanho total da lista é: ", len(dataBaseLista))

# Verifique qual é o maior valor numérico de óbitos novos e o menor valor numérico de óbitos novos.
obitosNovos = dataBaseLista[0][13] 
for dados in dataBaseLista: 
    if obitosNovos < dados[13]: 
        obitosNovos = dados[13]
print("O maior valor de óbitos novos é: ", obitosNovos)

obitosNovos = dataBaseLista[0][13] 
for dados in dataBaseLista: 
    if obitosNovos > dados[13]: 
        obitosNovos = dados[13]
print("O menor valor de óbitos novos é: ", obitosNovos)

# Remova da lista os dados das regiões de saúde
for dados in dataBaseLista:
    dados.pop(5) # exclui o código da região
    dados.pop(5) # exclui o nome da região, é o mesmo índice porque os índices atualizaram com o comando anterior

# Extraia os dados de Wall Ferraz/PI apresentando os casos novos com um print
print("O total de casos novos em Wall Ferraz/PI é: ", dataBaseTupla[9][11])