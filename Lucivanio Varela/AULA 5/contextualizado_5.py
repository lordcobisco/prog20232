

# A) Realize o download dos dados de forma manual e crie uma lista e uma tupla com as informações disponíveis no documento csv (coloque pelo menos 1 linha por estado e 10 regiões de saúde diferentes, algo próximo de umas 40 linhas).

# Exercicio contextualizado 5

# HIST_PAINEL_COVIDBR_2023_06_SET_2023

# TABELA ATUALIZADA ATE JUNHO DE 2023

# FORAM ANALIZADOS APENAS 1 LINHA, NO CASO, O ULTIMO DIA DE JUNHO DE CADA ESTADO 30.06.2023

# Dados organizados por ordem alfabetica em formato - Lista

Lista_Estados = ["Acre - AC","Alagoas - AL","Amazonas - AM","Amapá - AP","Bahia - BA","Ceará - CE","Distrito federal - DF","Espírito santos - ES","Goiás - G0","Maranhão - MA","Minas gerais - MG","Mato gosso do sul - MS","Mato grosso - MT",
"Pará - PA","Paraiba - PB","Pernambuco - PE","Piauí - PI","Paraná - PR","Rio de Janeiro - RJ","Rio grande do norte - RN","Rondônia - RO","Roraíma - RR","Rio Grande do Sul - RS","Santa Catarina - SC","Sergipe - SE",
"São paulo - SP","Tocantins - TO"]
Lista_populacaoTCU2019 = [881935, 3337357, 4144597, 845731, 14873064, 9132078, 3015268, 4018650, 7018354, 7075181, 21168791, 2778986, 3484466, 8602865, 4018127, 9557071, 3273227, 11433957, 17264943, 3506853, 1777225, 605761, 11377239, 7164788, 2298696, 45919049, 1572866 ]
Lista_casos_Acumulados = [163868, 340354, 636911, 186176, 1803323, 1470846, 909776, 1338274, 1941547, 496391, 4209719, 614076, 885800, 882712, 712062, 1185892, 433128, 2946286, 2813903, 590476, 486816, 185735, 3047205, 2026146, 362844, 6629875, 371279]
Lista_casoS_Novos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Lista_obitos_Acumulado = [2062, 7290, 14479, 2169, 31646, 28194, 11862, 15103, 28254, 11074, 65740, 11075, 15123, 19130, 10563, 22930, 8389, 46417, 77291, 8960, 7461, 2197, 42344, 22834, 6523, 180612, 4242  ]
Lista_obitos_Novos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# Sequencia de informações : 0 - Lista_Estado; 1 - Lista_populacaoTCU2019; 2 - Lista_casos_Acumulados; 3 - Lista_casoS_Novos; 4 - Lista_obitos_Acumulado; 5 - Lista_obitos_Novos

#Lista

L_Acre = [Lista_Estados [0], Lista_populacaoTCU2019 [0], Lista_casos_Acumulados [0], Lista_casoS_Novos [0], Lista_obitos_Acumulado [0], Lista_obitos_Novos [0]]
L_Alagoas = [Lista_Estados [1], Lista_populacaoTCU2019 [1], Lista_casos_Acumulados [1], Lista_casoS_Novos [1], Lista_obitos_Acumulado [1], Lista_obitos_Novos [1]]
L_Amazonas = [Lista_Estados [2], Lista_populacaoTCU2019 [2], Lista_casos_Acumulados [2], Lista_casoS_Novos [2], Lista_obitos_Acumulado [2], Lista_obitos_Novos [2]]
L_Amapá = [Lista_Estados [3], Lista_populacaoTCU2019 [3], Lista_casos_Acumulados [3], Lista_casoS_Novos [3], Lista_obitos_Acumulado [3], Lista_obitos_Novos [3]]
L_Bahia = [Lista_Estados [4], Lista_populacaoTCU2019 [4], Lista_casos_Acumulados [4], Lista_casoS_Novos [4], Lista_obitos_Acumulado [4], Lista_obitos_Novos [4]]
L_Ceará = [Lista_Estados [5], Lista_populacaoTCU2019 [5], Lista_casos_Acumulados [5], Lista_casoS_Novos [5], Lista_obitos_Acumulado [5], Lista_obitos_Novos [5]]
L_Distrito_Federal = [Lista_Estados [6], Lista_populacaoTCU2019 [6], Lista_casos_Acumulados [6], Lista_casoS_Novos [6], Lista_obitos_Acumulado [6], Lista_obitos_Novos [6]]
L_Espírito_santos = [Lista_Estados [7], Lista_populacaoTCU2019 [7], Lista_casos_Acumulados [7], Lista_casoS_Novos [7], Lista_obitos_Acumulado [7], Lista_obitos_Novos [7]]
L_Goiás = [Lista_Estados [8], Lista_populacaoTCU2019 [8], Lista_casos_Acumulados [8], Lista_casoS_Novos [8], Lista_obitos_Acumulado [8], Lista_obitos_Novos [8]]
L_Maranhão = [Lista_Estados [9], Lista_populacaoTCU2019 [9], Lista_casos_Acumulados [9], Lista_casoS_Novos [9], Lista_obitos_Acumulado [9], Lista_obitos_Novos [9]]
L_Minas_Gerais = [Lista_Estados [10], Lista_populacaoTCU2019 [10], Lista_casos_Acumulados [10], Lista_casoS_Novos [10], Lista_obitos_Acumulado [10], Lista_obitos_Novos [10]]
L_Mato_Grosso_do_Sul = [Lista_Estados [11], Lista_populacaoTCU2019 [11], Lista_casos_Acumulados [11], Lista_casoS_Novos [11], Lista_obitos_Acumulado [11], Lista_obitos_Novos [11]]
L_Mato_grosso = [Lista_Estados [12], Lista_populacaoTCU2019 [12], Lista_casos_Acumulados [12], Lista_casoS_Novos [12], Lista_obitos_Acumulado [12], Lista_obitos_Novos [12]]
L_Pará = [Lista_Estados [13], Lista_populacaoTCU2019 [13], Lista_casos_Acumulados [13], Lista_casoS_Novos [13], Lista_obitos_Acumulado [13], Lista_obitos_Novos [13]]
L_Paraiba = [Lista_Estados [14], Lista_populacaoTCU2019 [14], Lista_casos_Acumulados [14], Lista_casoS_Novos [14], Lista_obitos_Acumulado [14], Lista_obitos_Novos [14]]
L_Pernambuco = [Lista_Estados [15], Lista_populacaoTCU2019 [15], Lista_casos_Acumulados [15], Lista_casoS_Novos [15], Lista_obitos_Acumulado [15], Lista_obitos_Novos [15]]
L_Piauí = [Lista_Estados [16], Lista_populacaoTCU2019 [16], Lista_casos_Acumulados [16], Lista_casoS_Novos [16], Lista_obitos_Acumulado [16], Lista_obitos_Novos [16]]
L_Paraná = [Lista_Estados [17], Lista_populacaoTCU2019 [17], Lista_casos_Acumulados [17], Lista_casoS_Novos [17], Lista_obitos_Acumulado [17], Lista_obitos_Novos [17]]
L_Rio_de_Janeiro = [Lista_Estados [18], Lista_populacaoTCU2019 [18], Lista_casos_Acumulados [18], Lista_casoS_Novos [18], Lista_obitos_Acumulado [18], Lista_obitos_Novos [18]]
L_Rio_Grande_do_Norte = [Lista_Estados [19], Lista_populacaoTCU2019 [19], Lista_casos_Acumulados [19], Lista_casoS_Novos [19], Lista_obitos_Acumulado [19], Lista_obitos_Novos [19]]
L_Rondônia = [Lista_Estados [20], Lista_populacaoTCU2019 [20], Lista_casos_Acumulados [20], Lista_casoS_Novos [20], Lista_obitos_Acumulado [20], Lista_obitos_Novos [20]]
L_Roraíma = [Lista_Estados [21], Lista_populacaoTCU2019 [21], Lista_casos_Acumulados [21], Lista_casoS_Novos [21], Lista_obitos_Acumulado [21], Lista_obitos_Novos [21]]
L_Rio_Grande_do_Sul = [Lista_Estados [22], Lista_populacaoTCU2019 [22], Lista_casos_Acumulados [22], Lista_casoS_Novos [22], Lista_obitos_Acumulado [22], Lista_obitos_Novos [22]]
L_Santa_Catarina = [Lista_Estados [23], Lista_populacaoTCU2019 [23], Lista_casos_Acumulados [23], Lista_casoS_Novos [23], Lista_obitos_Acumulado [23], Lista_obitos_Novos [23]]
L_Sergipe = [Lista_Estados [24], Lista_populacaoTCU2019 [24], Lista_casos_Acumulados [24], Lista_casoS_Novos [24], Lista_obitos_Acumulado [24], Lista_obitos_Novos [24]]
L_São_Paulo = [Lista_Estados [25], Lista_populacaoTCU2019 [25], Lista_casos_Acumulados [25], Lista_casoS_Novos [25], Lista_obitos_Acumulado [25], Lista_obitos_Novos [25]]
L_Tocantins = [Lista_Estados [26], Lista_populacaoTCU2019 [26], Lista_casos_Acumulados [26], Lista_casoS_Novos [26], Lista_obitos_Acumulado [26], Lista_obitos_Novos [26]]



# Dados organizados por ordem alfabetica em formato - Tupla

Tupla_Estados = ("Acre - AC","Alagoas - AL","Amazonas - AM","Amapá - AP","Bahia - BA","Ceará - CE","Distrito federal - DF","Espírito santos - ES","Goiás - G0","Maranhão - MA","Minas gerais - MG","Mato gosso do sul - MS","Mato grosso - MT",
"Pará - PA","Paraiba - PB","Pernambuco - PE","Piauí - PI","Paraná - PR","Rio de Janeiro - RJ","Rio grande do norte - RN","Rondônia - RO","Roraíma - RR","Rio Grande do Sul - RS","Santa Catarina - SC","Sergipe - SE",
"São paulo - SP","Tocantins - TO")
Tupla_populacaoTCU2019 = (881935, 3337357, 4144597, 845731, 14873064, 9132078, 3015268, 4018650, 7018354, 7075181, 21168791, 2778986, 3484466, 8602865, 4018127, 9557071, 3273227, 11433957, 17264943, 3506853, 1777225, 605761, 11377239, 7164788, 2298696, 45919049, 1572866)
Tupla_casos_Acumulados = (163868, 340354, 636911, 186176, 1803323, 1470846, 909776, 1338274, 1941547, 496391, 4209719, 614076, 885800, 882712, 712062, 1185892, 433128, 2946286, 2813903, 590476, 486816, 185735, 3047205, 2026146, 362844, 6629875, 371279)
Tupla_casoS_Novos = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
Tupla_obitos_Acumulado = (2062, 7290, 14479, 2169, 31646, 28194, 11862, 15103, 28254, 11074, 65740, 11075, 15123, 19130, 10563, 22930, 8389, 46417, 77291, 8960, 7461, 2197, 42344, 22834, 6523, 180612, 4242)
Tupla_obitos_Novos = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# Sequencia de informações : 0 - Tupla_Estado; 1 - Tupla_populacaoTCU2019; 2 - Tupla_casos_Acumulados; 3 - Tupla_casoS_Novos; 4 - Tupla_obitos_Acumulado; 5 - Tupla_obitos_Novos

#Tupla

T_Acre =(Tupla_Estados [0], Tupla_populacaoTCU2019 [0], Tupla_casos_Acumulados [0], Tupla_casoS_Novos [0], Tupla_obitos_Acumulado [0], Tupla_obitos_Novos [0])
T_Alagoas = (Tupla_Estados [1], Tupla_populacaoTCU2019 [1], Tupla_casos_Acumulados [1], Tupla_casoS_Novos [1], Tupla_obitos_Acumulado [1], Tupla_obitos_Novos [1])
T_Amazonas = (Tupla_Estados [2], Tupla_populacaoTCU2019 [2], Tupla_casos_Acumulados [2], Tupla_casoS_Novos [2], Tupla_obitos_Acumulado [2], Tupla_obitos_Novos [2])
T_Amapá = (Tupla_Estados [3], Tupla_populacaoTCU2019 [3], Tupla_casos_Acumulados [3], Tupla_casoS_Novos [3], Tupla_obitos_Acumulado [3], Tupla_obitos_Novos [3])
T_Bahia = (Tupla_Estados [4], Tupla_populacaoTCU2019 [4], Tupla_casos_Acumulados [4], Tupla_casoS_Novos [4], Tupla_obitos_Acumulado [4], Tupla_obitos_Novos [4])
T_Ceará = (Tupla_Estados [5], Tupla_populacaoTCU2019 [5], Tupla_casos_Acumulados [5], Tupla_casoS_Novos [5], Tupla_obitos_Acumulado [5], Tupla_obitos_Novos [5])
T_Distrito_Federal = (Tupla_Estados [6], Tupla_populacaoTCU2019 [6], Tupla_casos_Acumulados [6], Tupla_casoS_Novos [6], Tupla_obitos_Acumulado [6], Tupla_obitos_Novos [6])
T_Espírito_santos = (Tupla_Estados [7], Tupla_populacaoTCU2019 [7], Tupla_casos_Acumulados [7], Tupla_casoS_Novos [7], Tupla_obitos_Acumulado [7], Tupla_obitos_Novos [7])
T_Goiás = (Tupla_Estados [8], Tupla_populacaoTCU2019 [8], Tupla_casos_Acumulados [8], Tupla_casoS_Novos [8], Tupla_obitos_Acumulado [8], Tupla_obitos_Novos [8])
T_Maranhão = (Tupla_Estados [9], Tupla_populacaoTCU2019 [9], Tupla_casos_Acumulados [9], Tupla_casoS_Novos [9], Tupla_obitos_Acumulado [9], Tupla_obitos_Novos [9])
T_Minas_Gerais = (Tupla_Estados [10], Tupla_populacaoTCU2019 [10], Tupla_casos_Acumulados [10], Tupla_casoS_Novos [10], Tupla_obitos_Acumulado [10], Tupla_obitos_Novos [10])
T_Mato_Grosso_do_Sul = (Tupla_Estados [11], Tupla_populacaoTCU2019 [11], Tupla_casos_Acumulados [11], Tupla_casoS_Novos [11], Tupla_obitos_Acumulado [11], Tupla_obitos_Novos [11])
T_Mato_grosso = (Tupla_Estados [12], Tupla_populacaoTCU2019 [12], Tupla_casos_Acumulados [12], Tupla_casoS_Novos [12], Tupla_obitos_Acumulado [12], Tupla_obitos_Novos [12])
T_Pará = (Tupla_Estados [13], Tupla_populacaoTCU2019 [13], Tupla_casos_Acumulados [13], Tupla_casoS_Novos [13], Tupla_obitos_Acumulado [13], Tupla_obitos_Novos [13])
T_Paraiba = (Tupla_Estados [14], Tupla_populacaoTCU2019 [14], Tupla_casos_Acumulados [14], Tupla_casoS_Novos [14], Tupla_obitos_Acumulado [14], Tupla_obitos_Novos [14])
T_Pernambuco = (Tupla_Estados [15], Tupla_populacaoTCU2019 [15], Tupla_casos_Acumulados [15], Tupla_casoS_Novos [15], Tupla_obitos_Acumulado [15], Tupla_obitos_Novos [15])
T_Piauí = (Tupla_Estados [16], Tupla_populacaoTCU2019 [16], Tupla_casos_Acumulados [16], Tupla_casoS_Novos [16], Tupla_obitos_Acumulado [16], Tupla_obitos_Novos [16])
T_Paraná = (Tupla_Estados [17], Tupla_populacaoTCU2019 [17], Tupla_casos_Acumulados [17], Tupla_casoS_Novos [17], Tupla_obitos_Acumulado [17], Tupla_obitos_Novos [17])
T_Rio_de_Janeiro = (Tupla_Estados [18], Tupla_populacaoTCU2019 [18], Tupla_casos_Acumulados [18], Tupla_casoS_Novos [18], Tupla_obitos_Acumulado [18], Tupla_obitos_Novos [18])
T_Rio_Grande_do_Norte = (Tupla_Estados [19], Tupla_populacaoTCU2019 [19], Tupla_casos_Acumulados [19], Tupla_casoS_Novos [19], Tupla_obitos_Acumulado [19], Tupla_obitos_Novos [19])
T_Rondônia = (Tupla_Estados [20], Tupla_populacaoTCU2019 [20], Tupla_casos_Acumulados [20], Tupla_casoS_Novos [20], Tupla_obitos_Acumulado [20], Tupla_obitos_Novos [20])
T_Roraíma = (Tupla_Estados [21], Tupla_populacaoTCU2019 [21], Tupla_casos_Acumulados [21], Tupla_casoS_Novos [21], Tupla_obitos_Acumulado [21], Tupla_obitos_Novos [21])
T_Rio_Grande_do_Sul = (Tupla_Estados [22], Tupla_populacaoTCU2019 [22], Tupla_casos_Acumulados [22], Tupla_casoS_Novos [22], Tupla_obitos_Acumulado [22], Tupla_obitos_Novos [22])
T_Santa_Catarina = (Tupla_Estados [23], Tupla_populacaoTCU2019 [23], Tupla_casos_Acumulados [23], Tupla_casoS_Novos [23], Tupla_obitos_Acumulado [23], Tupla_obitos_Novos [23])
T_Sergipe = (Tupla_Estados [24], Tupla_populacaoTCU2019 [24], Tupla_casos_Acumulados [24], Tupla_casoS_Novos [24], Tupla_obitos_Acumulado [24], Tupla_obitos_Novos [24])
T_São_Paulo = (Tupla_Estados [25], Tupla_populacaoTCU2019 [25], Tupla_casos_Acumulados [25], Tupla_casoS_Novos [25], Tupla_obitos_Acumulado [25], Tupla_obitos_Novos [25])
T_Tocantins = (Tupla_Estados [26], Tupla_populacaoTCU2019 [26], Tupla_casos_Acumulados [26], Tupla_casoS_Novos [26], Tupla_obitos_Acumulado [26], Tupla_obitos_Novos [26])



# 10 Regiões de saúde diferentes - Lista

Lista_regiao_estado = ["RN", "PB", "PI", "PE", "CE", "MA", "CE", "SE", "BA", "RJ"]
Lista_regiao_municipio = ["Acari", "Agua Branca", "AcauÃ£", "Abreu e Lima", "Abaiara", "Afonso Cunha", "Abaiara", "Amparo de SÃ£o Francisco", "Acajutiba", "Angra dos Reis"]
Lista_Coduf = [24, 25, 22, 26, 23, 21, 23, 28, 29, 33]
Lista_Codmun = [240010, 250010, 220005, 260005, 230010, 210010, 230010, 280010, 290030, 330010]
Lista_cod_Regiao_Saude = [24004, 25011, 22009, 26010, 23019, 21005, 23019, 28007, 29001, 33001]
Lista_nome_Regiao_Saude = ["4Âª REGIAO DE SAUDE - CAICO", "11Âª REGIAO", "VALE DO RIO GUARIBAS", "RECIFE", "19Âª REGIAO BREJO SANTO" "CAXIAS", "19Âª REGIAO BREJO SANTO", "PROPRIA", "ALAGOINHAS", "BAIA DA ILHA GRANDE"]
Lista_regiao_populacao_TCU_2019 = [11136,10234,7084, 99990, 11737, 6524, 11737, 2374, 15159, 203785]
Lista_regiao_casos_Acumulado = [1502, 2243, 258, 6322, 1366, 461, 1366, 266, 758, 28085]
Lista_regiao_casos_Novos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Lista_regiao_obitos_Acumulado = [30, 16, 3, 261, 20, 2, 20, 6, 28, 621]
Lista_regiao_obitos_Novos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# Sequencia de informação: 0 - Lista_regiao_estado; 1 - Lista_regiao_municipio; 2 - Lista_Coduf; 3 - Lista_Codmun; 4 - Lista_cod_Regiao_Saude; 5 - Lista_nome_Regiao_Saude; 6 - Lista_regiao_populacao_TCU_2019; 7 - Lista_regiao_casos_Acumulado; 8 - Lista_regiao_casos_Novos; 9 - Lista_regiao_obitos_Acumulado; 10 - Lista_regiao_obitos_Novos


L_RN = [Lista_regiao_estado[0], Lista_regiao_municipio[0], Lista_Coduf[0], Lista_Codmun[0],Lista_cod_Regiao_Saude[0], Lista_nome_Regiao_Saude[0], Lista_regiao_populacao_TCU_2019[0], Lista_regiao_casos_Acumulado[0], Lista_regiao_casos_Novos[0], Lista_regiao_obitos_Acumulado[0], Lista_regiao_obitos_Novos[0]]
L_PB = [Lista_regiao_estado[1], Lista_regiao_municipio[1], Lista_Coduf[1], Lista_Codmun[1],Lista_cod_Regiao_Saude[1], Lista_nome_Regiao_Saude[1], Lista_regiao_populacao_TCU_2019[1], Lista_regiao_casos_Acumulado[1], Lista_regiao_casos_Novos[1], Lista_regiao_obitos_Acumulado[1], Lista_regiao_obitos_Novos[1]]
L_PI = [Lista_regiao_estado[2], Lista_regiao_municipio[2], Lista_Coduf[2], Lista_Codmun[2],Lista_cod_Regiao_Saude[2], Lista_nome_Regiao_Saude[2], Lista_regiao_populacao_TCU_2019[2], Lista_regiao_casos_Acumulado[2], Lista_regiao_casos_Novos[2], Lista_regiao_obitos_Acumulado[2], Lista_regiao_obitos_Novos[2]]
L_PE = [Lista_regiao_estado[3], Lista_regiao_municipio[3], Lista_Coduf[3], Lista_Codmun[3],Lista_cod_Regiao_Saude[3], Lista_nome_Regiao_Saude[3], Lista_regiao_populacao_TCU_2019[3], Lista_regiao_casos_Acumulado[3], Lista_regiao_casos_Novos[3], Lista_regiao_obitos_Acumulado[3], Lista_regiao_obitos_Novos[3]]
L_CE = [Lista_regiao_estado[4], Lista_regiao_municipio[4], Lista_Coduf[4], Lista_Codmun[4],Lista_cod_Regiao_Saude[4], Lista_nome_Regiao_Saude[4], Lista_regiao_populacao_TCU_2019[4], Lista_regiao_casos_Acumulado[4], Lista_regiao_casos_Novos[4], Lista_regiao_obitos_Acumulado[4], Lista_regiao_obitos_Novos[4]]
L_MA = [Lista_regiao_estado[5], Lista_regiao_municipio[5], Lista_Coduf[5], Lista_Codmun[5],Lista_cod_Regiao_Saude[5], Lista_nome_Regiao_Saude[5], Lista_regiao_populacao_TCU_2019[5], Lista_regiao_casos_Acumulado[5], Lista_regiao_casos_Novos[5], Lista_regiao_obitos_Acumulado[5], Lista_regiao_obitos_Novos[5]]
L_AL = [Lista_regiao_estado[6], Lista_regiao_municipio[6], Lista_Coduf[6], Lista_Codmun[6],Lista_cod_Regiao_Saude[6], Lista_nome_Regiao_Saude[6], Lista_regiao_populacao_TCU_2019[6], Lista_regiao_casos_Acumulado[6], Lista_regiao_casos_Novos[6], Lista_regiao_obitos_Acumulado[6], Lista_regiao_obitos_Novos[6]]
L_SE = [Lista_regiao_estado[7], Lista_regiao_municipio[7], Lista_Coduf[7], Lista_Codmun[7],Lista_cod_Regiao_Saude[7], Lista_nome_Regiao_Saude[7], Lista_regiao_populacao_TCU_2019[7], Lista_regiao_casos_Acumulado[7], Lista_regiao_casos_Novos[7], Lista_regiao_obitos_Acumulado[7], Lista_regiao_obitos_Novos[7]]
L_BA = [Lista_regiao_estado[8], Lista_regiao_municipio[8], Lista_Coduf[8], Lista_Codmun[8],Lista_cod_Regiao_Saude[8], Lista_nome_Regiao_Saude[8], Lista_regiao_populacao_TCU_2019[8], Lista_regiao_casos_Acumulado[8], Lista_regiao_casos_Novos[8], Lista_regiao_obitos_Acumulado[8], Lista_regiao_obitos_Novos[8]]



 # 10 Regiões de saúde diferentes - Tupa

Tupla_regiao_estado = ("RN", "PB", "PI", "PE", "CE", "MA", "CE", "SE", "BA", "RJ")
Tupla_regiao_municipio = ("Acari", "Agua Branca", "AcauÃ£", "Abreu e Lima", "Abaiara", "Afonso Cunha", "Abaiara", "Amparo de SÃ£o Francisco", "Acajutiba", "Angra dos Reis")
Tupla_Coduf = (24, 25, 22, 26, 23, 21, 23, 28, 29, 33)
Tupla_Codmun = (240010, 250010, 220005, 260005, 230010, 210010, 230010, 280010, 290030, 330010)
Tupla_cod_Regiao_Saude = (24004, 25011, 22009, 26010, 23019, 21005, 23019, 28007, 29001, 33001)
Tupla_nome_Regiao_Saude = ("4Âª REGIAO DE SAUDE - CAICO", "11Âª REGIAO", "VALE DO RIO GUARIBAS", "RECIFE", "19Âª REGIAO BREJO SANTO" "CAXIAS", "19Âª REGIAO BREJO SANTO", "PROPRIA", "ALAGOINHAS", "BAIA DA ILHA GRANDE")
Tupla_regiao_populacao_TCU_2019 = (11136,10234,7084, 99990, 11737, 6524, 11737, 2374, 15159, 203785)
Tupla_regiao_casos_Acumulado = (1502, 2243, 258, 6322, 1366, 461, 1366, 266, 758, 28085)
Tupla_regiao_casos_Novos = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
Tupla_regiao_obitos_Acumulado = (30, 16, 3, 261, 20, 2, 20, 6, 28, 621)
Tupla_regiao_obitos_Novos = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


# Sequencia de informação: 0 - Tupa_regiao_estado; 1 - Tupla_regiao_municipio; 2 - Tupla_Coduf; 3 - Tupla_Codmun; 4 - Tupla_cod_Regiao_Saude; 5 - Tupla_nome_Regiao_Saude; 6 - Tupla_regiao_populacao_TCU_2019; 7 - Tupla_regiao_casos_Acumulado; 8 - Tupla_regiao_casos_Novos; 9 - Tupla_regiao_obitos_Acumulado; 10 - Tupla_regiao_obitos_Novos


T_RN = (Tupla_regiao_estado[0], Tupla_regiao_municipio[0], Tupla_Coduf[0], Tupla_Codmun[0], Tupla_cod_Regiao_Saude[0], Tupla_nome_Regiao_Saude[0], Tupla_regiao_populacao_TCU_2019[0], Tupla_regiao_casos_Acumulado[0], Tupla_regiao_casos_Novos[0], Tupla_regiao_obitos_Acumulado[0], Tupla_regiao_obitos_Novos[0])
T_PB = (Tupla_regiao_estado[1], Tupla_regiao_municipio[1], Tupla_Coduf[1], Tupla_Codmun[1], Tupla_cod_Regiao_Saude[1], Tupla_nome_Regiao_Saude[1], Tupla_regiao_populacao_TCU_2019[1], Tupla_regiao_casos_Acumulado[1], Tupla_regiao_casos_Novos[1], Tupla_regiao_obitos_Acumulado[1], Tupla_regiao_obitos_Novos[1])
T_PI = (Tupla_regiao_estado[2], Tupla_regiao_municipio[2], Tupla_Coduf[2], Tupla_Codmun[2], Tupla_cod_Regiao_Saude[2], Tupla_nome_Regiao_Saude[2], Tupla_regiao_populacao_TCU_2019[2], Tupla_regiao_casos_Acumulado[2], Tupla_regiao_casos_Novos[2], Tupla_regiao_obitos_Acumulado[2], Tupla_regiao_obitos_Novos[2])
T_PE = (Tupla_regiao_estado[3], Tupla_regiao_municipio[3], Tupla_Coduf[3], Tupla_Codmun[3], Tupla_cod_Regiao_Saude[3], Tupla_nome_Regiao_Saude[3], Tupla_regiao_populacao_TCU_2019[3], Tupla_regiao_casos_Acumulado[3], Tupla_regiao_casos_Novos[3], Tupla_regiao_obitos_Acumulado[3], Tupla_regiao_obitos_Novos[3])
T_CE = (Tupla_regiao_estado[4], Tupla_regiao_municipio[4], Tupla_Coduf[4], Tupla_Codmun[4], Tupla_cod_Regiao_Saude[4], Tupla_nome_Regiao_Saude[4], Tupla_regiao_populacao_TCU_2019[4], Tupla_regiao_casos_Acumulado[4], Tupla_regiao_casos_Novos[4], Tupla_regiao_obitos_Acumulado[4], Tupla_regiao_obitos_Novos[4])
T_MA = (Tupla_regiao_estado[5], Tupla_regiao_municipio[5], Tupla_Coduf[5], Tupla_Codmun[5], Tupla_cod_Regiao_Saude[5], Tupla_nome_Regiao_Saude[5], Tupla_regiao_populacao_TCU_2019[5], Tupla_regiao_casos_Acumulado[5], Tupla_regiao_casos_Novos[5], Tupla_regiao_obitos_Acumulado[5], Tupla_regiao_obitos_Novos[5])
T_AL = (Tupla_regiao_estado[6], Tupla_regiao_municipio[6], Tupla_Coduf[6], Tupla_Codmun[6], Tupla_cod_Regiao_Saude[6], Tupla_nome_Regiao_Saude[6], Tupla_regiao_populacao_TCU_2019[6], Tupla_regiao_casos_Acumulado[6], Tupla_regiao_casos_Novos[6], Tupla_regiao_obitos_Acumulado[6], Tupla_regiao_obitos_Novos[6])
T_SE = (Tupla_regiao_estado[7], Tupla_regiao_municipio[7], Tupla_Coduf[7], Tupla_Codmun[7], Tupla_cod_Regiao_Saude[7], Tupla_nome_Regiao_Saude[7], Tupla_regiao_populacao_TCU_2019[7], Tupla_regiao_casos_Acumulado[7], Tupla_regiao_casos_Novos[7], Tupla_regiao_obitos_Acumulado[7], Tupla_regiao_obitos_Novos[7])
T_BA = (Tupla_regiao_estado[8], Tupla_regiao_municipio[8], Tupla_Coduf[8], Tupla_Codmun[8], Tupla_cod_Regiao_Saude[8], Tupla_nome_Regiao_Saude[8], Tupla_regiao_populacao_TCU_2019[8], Tupla_regiao_casos_Acumulado[8], Tupla_regiao_casos_Novos[8], Tupla_regiao_obitos_Acumulado[8], Tupla_regiao_obitos_Novos[8])



# B) Mande printar na tela o número de casos acumulados para o estado do rio de janeiro tanto para a tupla quanto para a lista.

print("Os casos acumulados para o estado do Rio de Janeiro foram:", L_Rio_de_Janeiro[2])
print("Os casos acumulados para o estado do Rio de Janeiro foram:", T_Rio_de_Janeiro[2])


# C) Apresente na tela todos os óbitos acumulados mostrando os casos apenas para o caso dos estados (sem mostrar regiões de saúde, etc..).


print("Estado:", L_Acre[0], "Óbitos acumulados:", L_Acre[4] )
print("Estado:", L_Alagoas[0], "Óbitos acumulados:", L_Alagoas[4] )
print("Estado:", L_Amazonas[0], "Óbitos acumulados:", L_Amazonas[4] )
print("Estado:", L_Amapá[0], "Óbitos acumulados:", L_Amapá[4] )
print("Estado:", L_Bahia[0], "Óbitos acumulados:", L_Bahia[4] )
print("Estado:", L_Ceará[0], "Óbitos acumulados:", L_Ceará[4] )
print("Estado:", L_Distrito_Federal[0], "Óbitos acumulados:", L_Distrito_Federal[4] )
print("Estado:", L_Espírito_santos[0], "Óbitos acumulados:", L_Espírito_santos[4] )
print("Estado:", L_Goiás[0], "Óbitos acumulados:", L_Goiás[4] )
print("Estado:", L_Maranhão[0], "Óbitos acumulados:", L_Maranhão[4] )
print("Estado:", L_Minas_Gerais[0], "Óbitos acumulados:", L_Minas_Gerais[4] )
print("Estado:", L_Mato_Grosso_do_Sul[0], "Óbitos acumulados:", L_Mato_Grosso_do_Sul[4] )
print("Estado:", L_Mato_grosso[0], "Óbitos acumulados:", L_Mato_grosso[4] )
print("Estado:", L_Pará[0], "Óbitos acumulados:", L_Pará[4] )
print("Estado:", L_Paraiba[0], "Óbitos acumulados:", L_Paraiba[4] )
print("Estado:", L_Pernambuco[0], "Óbitos acumulados:", L_Pernambuco[4] )
print("Estado:", L_Piauí[0], "Óbitos acumulados:", L_Piauí[4] )
print("Estado:", L_Paraná[0], "Óbitos acumulados:", L_Paraná[4] )
print("Estado:", L_Rio_de_Janeiro[0], "Óbitos acumulados:", L_Rio_de_Janeiro[4] )
print("Estado:", L_Rio_Grande_do_Norte[0], "Óbitos acumulados:", L_Rio_Grande_do_Norte[4] )
print("Estado:", L_Rondônia[0], "Óbitos acumulados:", L_Rondônia[4] )
print("Estado:", L_Roraíma[0], "Óbitos acumulados:", L_Roraíma[4] )
print("Estado:", L_Rio_Grande_do_Sul[0], "Óbitos acumulados:", L_Rio_Grande_do_Sul[4] )
print("Estado:", L_Santa_Catarina[0], "Óbitos acumulados:", L_Santa_Catarina[4] )
print("Estado:", L_Sergipe[0], "Óbitos acumulados:", L_Sergipe[4] )
print("Estado:", L_São_Paulo[0], "Óbitos acumulados:", L_São_Paulo[4] )
print("Estado:", L_Tocantins[0], "Óbitos acumulados:", L_Tocantins[4] )


# D) Assuma que os dados de óbitos novos para o estado da paraíba estejam errados em 10 unidades para menos. Sobrescreva a informação tanto na lista quanto na tupla, corrigindo os dados. 

# Dados de óbitos novos  - Lista/Tupla

L_Paraiba[5] = L_Paraiba[5] + 10
#T_Paraiba[5] = T_Paraiba[5] + 10 (não pode alterar valores da erro)

print ("Os dados de óbitos novos para a paraiba são:", L_Paraiba[5])
print("Os dados de óbitos novos para a paraiba são:", T_Paraiba[5]) # não pode alterar valores

# E) As duas operações foram possíveis (lista e tupla)? Justifique
#Não, pois a operação Tupla não pode alterar valores, logo Tupla é imutável.

# F) Crie uma nova lista com apenas dados de 1 estado e todos os municípios e adicione essa lista nova a lista já existente (append ou insert). 

criar_lista = []
criar_lista.append()