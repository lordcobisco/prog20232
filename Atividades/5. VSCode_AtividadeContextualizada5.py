#a)
casos_covid = [
    ["regiao", "estado", "municipio", "coduf", "codmun", "codRegiaoSaude", "nomeRegiaoSaude", "data", "semanaEpi", "populacaoTCU2019", "casosAcumulado", "casosNovos", "obitosAcumulado", "obitosNovos", "interior/metropolitana"], 
["Norte", "RO", "Colorado do Oeste", 11, 110006, 11006, "CONE SUL", "2020-07-31", 31, 15882, 80, 0, 0, 0, 0], 
["Norte", "RO", "Costa Marques", 11, 110008, 11007, "VALE DO GUAPORE", "2020-07-31", 31, 18331, 82, 3, 1, 0, 0], 
["Norte", "AC", "Acrelândia", 12, 120001, 12002, "BAIXO ACRE E PURUS", "2020-07-31", 31, 15256, 277, 0, 6, 0, 0], 
["Norte", "AC", "Assis Brasil", 12, 120005, 12001, "ALTO ACRE", "2020-07-31", 31, 7417, 316, 0, 6, 0, 0], 
["Norte", "AM", "Alvarães", 13, 130002, 13008, "TRIANGULO", "2020-07-31", 31, 16041, 1148, 12, 13, 0, 0], 
["Norte", "AM", "Amaturã" , 13, 130006, 13009, "ALTO SOLIMOES", "2020-07-31", 31, 11536, 506, 0, 8, 0, 0], 
["Norte", "RR", "Amajari", 14, 140002, 14001, "CENTRO NORTE", "2020-07-31", 31, 12796, 244, 1, 6, 0, 0], 
["Norte", "RR", "Alto Alegre", 14, 140005, 14001, "CENTRO NORTE", "2020-07-31", 31, 15510, 389, 2, 9, 0, 1], 
["Norte", "PA", "Abaetetuba", 15, 150010, 15011, "TOCANTINS", "2020-07-31", 31, 157698, 2673, 32, 109, 0, 0], 
["Norte", "PA", "Abel Figueiredo", 15, 150013, 15003, "CARAJAS", "2020-07-31", 31, 7434, 148, 8, 1, 0, 0], 
["Norte", "AP", "Serra do Navio", 16, 160005, 16001, "AREA CENTRAL", "2020-07-31", 31, 5397, 552, 0, 4, 0, 0], 
["Norte", "AP", "Amapá", 16, 160010, 16002, "AREA NORTE", "2020-07-31", 31, 9109, 400, 2, 4, 0, 0], 
["Norte", "TO", "Abreulândia", 17, 170025, 17007, "CANTAO", "2020-07-31", 31, 2579, 12, 0, 2, 0, 0], 
["Norte", "TO", "Aguiarnópolis", 17, 170030, 17002, "BICO DO PAPAGAIO", "2020-07-31", 31, 6733, 279, 1, 6, 0, 0], 
["Nordeste", "MA", "Afonso Cunha", 21, 210010, 21005, "CAXIAS", "2020-07-31", 31, 6524, 131, 0, 2, 0, 0], 
["Nordeste", "MA", "Aldeias Altas", 21, 210030, 21005, "CAXIAS", "2020-07-31", 31, 26532, 485, 6, 0, 0, 0], 
["Nordeste", "PI", "Acauã", 22, 220005, 22009, "VALE DO RIO GUARIBAS", "2020-07-31", 31, 7084, 20, 0, 0, 0, 0], 
["Nordeste", "PI", "Agricolândia", 22, 220010, 22004, "ENTRE RIOS", "2020-07-31", 31, 5139, 19, 2, 0, 0, 0], 
["Nordeste", "CE", "Acopiara", 23, 230030, 23018, "18ª REGIAO IGUATU", "2020-07-31", 31, 54270, 463, 3, 22, 0, 0], 
["Nordeste", "CE", "Aracati", 23, 230110, 23007, "7ª REGIAO ARACATI", "2020-07-31", 31, 74547, 1305, 16, 46, 0, 0], 
["Nordeste", "RN", "Extremoz", 24, 240360, 24007, "7ª REGIAO DE SAUDE - METROPOLITANA", "2020-07-31", 31, 28583, 438, 5, 25, 0, 1], 
["Nordeste", "RN", "Macaíba", 24, 240710, 24007, "7ª REGIAO DE SAUDE - METROPOLITANA", "2020-07-31", 31, 80792, 678, 4, 38, 0, 1], 
["Nordeste", "PB", "Alagoinha", 25, 250050, 25002, "2ª REGIAO", "2020-07-31", 31, 14489, 763, 15, 7, 0, 0], 
["Nordeste", "PE", "Belo Jardim", 26, 260170, 26003, "CARUARU", "2020-07-31", 31, 76439, 676, 26, 23, 0, 0], 
["Nordeste", "AL", "Belo Monte", 27, 270090, 27007, "7ª REGIAO DE SAUDE", "2020-07-31", 31, 6704, 41, 0, 2, 0, 0], 
["Nordeste", "SE", "Gracho Cardoso", 28, 280260, 28005, "NOSSA SENHORA DA GLORIA", "2020-07-31", 31, 5818, 52, 0, 0, 0, 0], 
["Nordeste", "BA", "Baixa Grande", 29, 290260, 29006, "FEIRA DE SANTANA", "2020-07-31", 31, 20468, 11, 0, 0, 0, 0], 
["Sudeste", "MG", "Araguari", 31, 310350, 31075, "UBERLANDIA / ARAGUARI", "2020-07-31", 31, 117267, 1450, 26, 30, 1, 0], 
["Sudeste", "ES", "Dores do Rio Preto", 32, 320200, 32004, "SUL", "2020-07-31", 31, 6749, 56, 0, 1, 0, 0], 
["Sudeste", "RJ", "Miguel Pereira", 33, 330290, 33003, "CENTRO-SUL", "2020-07-31", 31, 25538, 208, 0, 11, 0, 0], 
["Sudeste", "SP", "Alfredo Marcondes", 35, 350080, 35112, "ALTA SOROCABANA", "2020-07-31", 31, 4166, 30, 0, 1, 0, 0], 
["Sul", "PR", "Atalaia", 41, 410220, 41015, "15ª RS MARINGA", "2020-07-31", 31, 3892, 40, 0, 0, 0, 0], 
["Sul", "SC", "Anita Garibaldi", 42, 420100, 42013, "SERRA CATARINENSE", "2020-07-31", 31, 7133, 103, 2, 1, 0, 0], 
["Sul", "RS", "Balneário Pinhal", 43, 430163, 43005, "REGIAO 05", "2020-07-31", 31, 14068, 39, 0, 1, 0, 0], 
["Centro-Oeste", "MS", "Bataguassu", 50, 500190, 50004, "TRES LAGOAS", "2020-07-31", 31, 23024, 617, 23, 2, 0, 0], 
["Centro-Oeste", "MT", "General Carneiro", 51, 510390, 51005, "GARCAS ARAGUAIA", "2020-07-31", 31, 5540, 157, 2, 7, 0, 0], 
["Centro-Oeste", "GO", "Amaralina", 52, 520082, 52014, "SERRA DA MESA", "2020-07-31", 31, 3812, 3, 0, 0, 0, 0], 
["Centro-Oeste", "DF", "Brasília", 53, 530010, 53001, "DISTRITO FEDERAL", "2020-07-31;31", 3015268, 106292, 1850, 1469, 25, 1]

]

casos_covid2 = (
    ("regiao", "estado", "municipio", "coduf", "codmun", "codRegiaoSaude", "nomeRegiaoSaude", "data", "semanaEpi", "populacaoTCU2019", "casosAcumulado", "casosNovos", "obitosAcumulado", "obitosNovos", "interior/metropolitana"), 
("Norte", "RO", "Colorado do Oeste", 11, 110006, 11006, "CONE SUL", "2020-07-31", 31, 15882, 80, 0, 0, 0, 0), 
("Norte", "RO", "Costa Marques", 11, 110008, 11007, "VALE DO GUAPORE", "2020-07-31", 31, 18331, 82, 3, 1, 0, 0), 
("Norte", "AC", "Acrelândia", 12, 120001, 12002, "BAIXO ACRE E PURUS", "2020-07-31", 31, 15256, 277, 0, 6, 0, 0), 
("Norte", "AC", "Assis Brasil", 12, 120005, 12001, "ALTO ACRE", "2020-07-31", 31, 7417, 316, 0, 6, 0, 0), 
("Norte", "AM", "Alvarães", 13, 130002, 13008, "TRIANGULO", "2020-07-31", 31, 16041, 1148, 12, 13, 0, 0), 
("Norte", "AM", "Amaturã" , 13, 130006, 13009, "ALTO SOLIMOES", "2020-07-31", 31, 11536, 506, 0, 8, 0, 0), 
("Norte", "RR", "Amajari", 14, 140002, 14001, "CENTRO NORTE", "2020-07-31", 31, 12796, 244, 1, 6, 0, 0), 
("Norte", "RR", "Alto Alegre", 14, 140005, 14001, "CENTRO NORTE", "2020-07-31", 31, 15510, 389, 2, 9, 0, 1), 
("Norte", "PA", "Abaetetuba", 15, 150010, 15011, "TOCANTINS", "2020-07-31", 31, 157698, 2673, 32, 109, 0, 0), 
("Norte", "PA", "Abel Figueiredo", 15, 150013, 15003, "CARAJAS", "2020-07-31", 31, 7434, 148, 8, 1, 0, 0), 
("Norte", "AP", "Serra do Navio", 16, 160005, 16001, "AREA CENTRAL", "2020-07-31", 31, 5397, 552, 0, 4, 0, 0), 
("Norte", "AP", "Amapá", 16, 160010, 16002, "AREA NORTE", "2020-07-31", 31, 9109, 400, 2, 4, 0, 0), 
("Norte", "TO", "Abreulândia", 17, 170025, 17007, "CANTAO", "2020-07-31", 31, 2579, 12, 0, 2, 0, 0), 
("Norte", "TO", "Aguiarnópolis", 17, 170030, 17002, "BICO DO PAPAGAIO", "2020-07-31", 31, 6733, 279, 1, 6, 0, 0), 
("Nordeste", "MA", "Afonso Cunha", 21, 210010, 21005, "CAXIAS", "2020-07-31", 31, 6524, 131, 0, 2, 0, 0), 
("Nordeste", "MA", "Aldeias Altas", 21, 210030, 21005, "CAXIAS", "2020-07-31", 31, 26532, 485, 6, 0, 0, 0), 
("Nordeste", "PI", "Acauã", 22, 220005, 22009, "VALE DO RIO GUARIBAS", "2020-07-31", 31, 7084, 20, 0, 0, 0, 0), 
("Nordeste", "PI", "Agricolândia", 22, 220010, 22004, "ENTRE RIOS", "2020-07-31", 31, 5139, 19, 2, 0, 0, 0), 
("Nordeste", "CE", "Acopiara", 23, 230030, 23018, "18ª REGIAO IGUATU", "2020-07-31", 31, 54270, 463, 3, 22, 0, 0), 
("Nordeste", "CE", "Aracati", 23, 230110, 23007, "7ª REGIAO ARACATI", "2020-07-31", 31, 74547, 1305, 16, 46, 0, 0), 
("Nordeste", "RN", "Extremoz", 24, 240360, 24007, "7ª REGIAO DE SAUDE - METROPOLITANA", "2020-07-31", 31, 28583, 438, 5, 25, 0, 1), 
("Nordeste", "RN", "Macaíba", 24, 240710, 24007, "7ª REGIAO DE SAUDE - METROPOLITANA", "2020-07-31", 31, 80792, 678, 4, 38, 0, 1), 
("Nordeste", "PB", "Alagoinha", 25, 250050, 25002, "2ª REGIAO", "2020-07-31", 31, 14489, 763, 15, 7, 0, 0), 
("Nordeste", "PE", "Belo Jardim", 26, 260170, 26003, "CARUARU", "2020-07-31", 31, 76439, 676, 26, 23, 0, 0), 
("Nordeste", "AL", "Belo Monte", 27, 270090, 27007, "7ª REGIAO DE SAUDE", "2020-07-31", 31, 6704, 41, 0, 2, 0, 0), 
("Nordeste", "SE", "Gracho Cardoso", 28, 280260, 28005, "NOSSA SENHORA DA GLORIA", "2020-07-31", 31, 5818, 52, 0, 0, 0, 0), 
("Nordeste", "BA", "Baixa Grande", 29, 290260, 29006, "FEIRA DE SANTANA", "2020-07-31", 31, 20468, 11, 0, 0, 0, 0), 
("Sudeste", "MG", "Araguari", 31, 310350, 31075, "UBERLANDIA / ARAGUARI", "2020-07-31", 31, 117267, 1450, 26, 30, 1, 0), 
("Sudeste", "ES", "Dores do Rio Preto", 32, 320200, 32004, "SUL", "2020-07-31", 31, 6749, 56, 0, 1, 0, 0), 
("Sudeste", "RJ", "Miguel Pereira", 33, 330290, 33003, "CENTRO-SUL", "2020-07-31", 31, 25538, 208, 0, 11, 0, 0), 
("Sudeste", "SP", "Alfredo Marcondes", 35, 350080, 35112, "ALTA SOROCABANA", "2020-07-31", 31, 4166, 30, 0, 1, 0, 0), 
("Sul", "PR", "Atalaia", 41, 410220, 41015, "15ª RS MARINGA", "2020-07-31", 31, 3892, 40, 0, 0, 0, 0), 
("Sul", "SC", "Anita Garibaldi", 42, 420100, 42013, "SERRA CATARINENSE", "2020-07-31", 31, 7133, 103, 2, 1, 0, 0), 
("Sul", "RS", "Balneário Pinhal", 43, 430163, 43005, "REGIAO 05", "2020-07-31", 31, 14068, 39, 0, 1, 0, 0), 
("Centro-Oeste", "MS", "Bataguassu", 50, 500190, 50004, "TRES LAGOAS", "2020-07-31", 31, 23024, 617, 23, 2, 0, 0), 
("Centro-Oeste", "MT", "General Carneiro", 51, 510390, 51005, "GARCAS ARAGUAIA", "2020-07-31", 31, 5540, 157, 2, 7, 0, 0), 
("Centro-Oeste", "GO", "Amaralina", 52, 520082, 52014, "SERRA DA MESA", "2020-07-31", 31, 3812, 3, 0, 0, 0, 0), 
("Centro-Oeste", "DF", "Brasília", 53, 530010, 53001, "DISTRITO FEDERAL", "2020-07-31;31", 3015268, 106292, 1850, 1469, 25, 1)

)

#b)
print(casos_covid[30][10])
print(casos_covid2[30][10])

#c)
print(casos_covid[1][1], casos_covid[1][12])
print(casos_covid[2][1], casos_covid[2][12])
print(casos_covid[3][1], casos_covid[3][12])
print(casos_covid[4][1], casos_covid[4][12])
print(casos_covid[5][1], casos_covid[5][12])
print(casos_covid[6][1], casos_covid[6][12])
print(casos_covid[7][1], casos_covid[7][12])
print(casos_covid[8][1], casos_covid[8][12])
print(casos_covid[9][1], casos_covid[9][12])
print(casos_covid[10][1], casos_covid[10][12])
print(casos_covid[11][1], casos_covid[11][12])
print(casos_covid[12][1], casos_covid[12][12])
print(casos_covid[13][1], casos_covid[13][12])
print(casos_covid[14][1], casos_covid[14][12])
print(casos_covid[15][1], casos_covid[15][12])
print(casos_covid[16][1], casos_covid[16][12])
print(casos_covid[17][1], casos_covid[17][12])
print(casos_covid[18][1], casos_covid[18][12])
print(casos_covid[19][1], casos_covid[19][12])
print(casos_covid[20][1], casos_covid[20][12])
print(casos_covid[21][1], casos_covid[21][12])
print(casos_covid[22][1], casos_covid[22][12])
print(casos_covid[23][1], casos_covid[23][12])
print(casos_covid[24][1], casos_covid[24][12])
print(casos_covid[25][1], casos_covid[25][12])
print(casos_covid[26][1], casos_covid[26][12])
print(casos_covid[27][1], casos_covid[27][12])
print(casos_covid[28][1], casos_covid[28][12])
print(casos_covid[29][1], casos_covid[29][12])
print(casos_covid[30][1], casos_covid[30][12])
print(casos_covid[31][1], casos_covid[31][12])
print(casos_covid[32][1], casos_covid[32][12])
print(casos_covid[33][1], casos_covid[33][12])
print(casos_covid[34][1], casos_covid[34][12])
print(casos_covid[35][1], casos_covid[35][12])
print(casos_covid[36][1], casos_covid[36][12])
print(casos_covid[37][1], casos_covid[37][12])
print(casos_covid[38][1], casos_covid[38][12]) 

#d)
casos_covid[23][12] = 25
#print(casos_covid[23][12])
#casos_covid2[23][12] = 25

#e)
#Não foi possível realizar a operação de substituição na tupla, pois os elementos da tupla são imutáveis. 

#f) 
dados_ES = [
    ["Sudeste", "ES", "Afonso Cláudio", 32, 320010, 32002, "METROPOLITANA", "2020-07-31", 31, 30586, 529, 3, 12, 0, 0], 
["Sudeste", "ES", "Águia Branca", 32, 320013, 32001, "CENTRAL", "2020-07-31", 31, 9642, 202, 2, 3, 0, 0], 
["Sudeste", "ES", "Água Doce do Norte", 32, 320016, 32003, "NORTE", "2020-07-31", 31, 11019, 117, 2, 5, 0, 0], 
["Sudeste", "ES", "Alegre", 32, 320020, 32004, "SUL", "2020-07-31", 31, 30084, 246, 2, 13, 0, 0], 
["Sudeste", "ES", "Alfredo Chaves", 32, 320030, 32004, "SUL", "2020-07-31", 31, 14601, 247, 1, 4, 0, 0], 
["Sudeste", "ES", "Alto Rio Novo", 32, 320035, 32001, "CENTRAL", "2020-07-31", 31, 7836, 111, 0, 5, 0, 0], 
["Sudeste", "ES", "Anchieta", 32, 320040, 32004, "SUL", "2020-07-31", 31, 29263, 579, 10, 16, 1, 0], 
["Sudeste", "ES", "Apiacá", 32, 320050, 32004, "SUL", "2020-07-31", 31, 7567, 90, 0, 2, 0, 0] 
]
# ["Sudeste;ES;Aracruz;32;320060;32001;CENTRAL;2020-07-31;31;101220;2386;45;53;0;;;0"], 
# ["Sudeste;ES;Atáio Vivacqua;32;320070;32004;SUL;2020-07-31;31;11936;200;0;3;1;;;"], 
# ["Sudeste;ES;Baixo Guandu;32;320080;32001;CENTRAL;2020-07-31;31;30998;518;12;12;0;;;0"], 
# ["Sudeste;ES;Barra de São Francisco;32;320090;32003;NORTE;2020-07-31;31;44650;311;6;12;1;;;0"], 
# ["Sudeste;ES;Boa Esperança;32;320100;32003;NORTE;2020-07-31;31;15037;277;8;12;0;;;0"], 
# ["Sudeste;ES;Bom Jesus do Norte;32;320110;32004;SUL;2020-07-31;31;9936;202;3;5;2;;;0"], 
# ["Sudeste;ES;Brejetuba;32;320115;32002;METROPOLITANA;2020-07-31;31;12404;304;6;0;0;;;0"], 
# ["Sudeste;ES;Cachoeiro de Itapemirim;32;320120;32004;SUL;2020-07-31;31;208972;3528;167;105;2;;;0"], 
# ["Sudeste;ES;Cariacica;32;320130;32002;METROPOLITANA;2020-07-31;31;381285;8957;35;334;2;;;1"], 
# ["Sudeste;ES;Castelo;32;320140;32004;SUL;2020-07-31;31;37534;771;37;21;0;;;0"], 
# ["Sudeste;ES;Colatina;32;320150;32001;CENTRAL;2020-07-31;31;122499;3716;87;82;1;;;0"], 
# ["Sudeste;ES;Conceição da Barra;32;320160;32003;NORTE;2020-07-31;31;31063;173;2;8;0;;;0"], 
# ["Sudeste;ES;Conceição do Castelo;32;320170;32002;METROPOLITANA;2020-07-31;31;12723;153;4;3;0;;;0"], 
# ["Sudeste;ES;Divino de São Lourenç;32;320180;32004;SUL;2020-07-31;31;4304;102;3;0;0;;;0"], 
# ["Sudeste;ES;Domingos Martins;32;320190;32002;METROPOLITANA;2020-07-31;31;33850;502;13;9;2;;;0"], 
# ["Sudeste;ES;Dores do Rio Preto;32;320200;32004;SUL;2020-07-31;31;6749;56;0;1;0;;;0"], 
# ["Sudeste;ES;Ecoporanga;32;320210;32003;NORTE;2020-07-31;31;22923;335;10;7;0;;;0"], 
# ["Sudeste;ES;FundÃ£o;32;320220;32002;METROPOLITANA;2020-07-31;31;21509;477;6;13;0;;;1"], 
# ["Sudeste;ES;Governador Lindenberg;32;320225;32001;CENTRAL;2020-07-31;31;12709;105;2;0;0;;;0"], 
# ["Sudeste;ES;Guaçá;32;320230;32004;SUL;2020-07-31;31;30867;249;6;12;0;;;0"], 
# ["Sudeste;ES;Guarapari;32;320240;32002;METROPOLITANA;2020-07-31;31;124859;1972;44;79;0;;;1"], 
# ["Sudeste;ES;Ibatiba;32;320245;32002;METROPOLITANA;2020-07-31;31;26082;288;12;9;2;;;0"], 
# ["Sudeste;ES;Ibiraçu;32;320250;32001;CENTRAL;2020-07-31;31;12479;378;7;9;0;;;0"], 
# ["Sudeste;ES;Ibitirama;32;320255;32004;SUL;2020-07-31;31;8889;65;2;4;0;;;0"], 
# ["Sudeste;ES;Iconha;32;320260;32004;SUL;2020-07-31;31;13860;296;11;0;0;;;0"], 
# ["Sudeste;ES;Irupi;32;320265;32004;SUL;2020-07-31;31;13377;169;-1;3;0;;;0"], 
# ["Sudeste;ES;Itaguaçu;32;320270;32002;METROPOLITANA;2020-07-31;31;14066;78;8;1;0;;;0"], 
# ["Sudeste;ES;Itapemirim;32;320280;32004;SUL;2020-07-31;31;34348;721;6;35;0;;;0"], 
# ["Sudeste;ES;Itarana;32;320290;32002;METROPOLITANA;2020-07-31;31;10555;58;0;1;0;;;0"], 
# ["Sudeste;ES;Jaguará;32;320305;32003;NORTE;2020-07-31;31;30477;336;27;5;0;;;0"], 
# ["Sudeste;ES;Jerônimo Monteiro;32;320310;32004;SUL;2020-07-31;31;12192;145;3;5;0;;;0"], 
# ["Sudeste;ES;João Neiva;32;320313;32001;CENTRAL;2020-07-31;31;16668;320;6;6;0;;;0"], 
# ["Sudeste;ES;Laranja da Terra;32;320316;32002;METROPOLITANA;2020-07-31;31;10947;63;1;1;0;;;0"], 
# ["Sudeste;ES;Linhares;32;320320;32001;CENTRAL;2020-07-31;31;173555;4371;43;72;0;;;0"], 
# ["Sudeste;ES;Mantenópolis;32;320330;32001;CENTRAL;2020-07-31;31;15350;157;4;4;0;;;0"], 
# ["Sudeste;ES;Marechal Floriano;32;320334;32002;METROPOLITANA;2020-07-31;31;16694;602;0;17;0;;;0"], 
# ["Sudeste;ES;Mimoso do Sul;32;320340;32004;SUL;2020-07-31;31;26153;562;1;3;0;;;0"], 
# ["Sudeste;ES;Montanha;32;320350;32003;NORTE;2020-07-31;31;18833;132;4;4;0;;;0"], 

casos_covid.append(dados_ES)   

#g) 
del casos_covid[1][6]
#print(casos_covid[1])
del casos_covid[2][6]
del casos_covid[3][6]
del casos_covid[4][6]
del casos_covid[5][6]
del casos_covid[6][6]
del casos_covid[7][6]
del casos_covid[8][6]
del casos_covid[9][6]
del casos_covid[10][6]
del casos_covid[11][6]
del casos_covid[12][6]
del casos_covid[13][6]
del casos_covid[14][6]
del casos_covid[15][6]
del casos_covid[16][6]
del casos_covid[17][6]
del casos_covid[18][6]
del casos_covid[19][6]
del casos_covid[20][6]
del casos_covid[21][6]
del casos_covid[22][6]
del casos_covid[23][6]
del casos_covid[24][6]
del casos_covid[25][6]
del casos_covid[26][6]
del casos_covid[27][6]
del casos_covid[28][6]
del casos_covid[29][6]
del casos_covid[30][6]
del casos_covid[31][6]
del casos_covid[32][6]
del casos_covid[33][6]
del casos_covid[34][6]
del casos_covid[35][6]
del casos_covid[36][6]
del casos_covid[37][6]
del casos_covid[38][6]

#h) 
soma_acumulados = casos_covid[1][10] +  casos_covid[2][10] + casos_covid[3][10] + casos_covid[4][10] + casos_covid[5][10]
+ casos_covid[6][10] + casos_covid[7][10] + casos_covid[8][10] + casos_covid[9][10] + casos_covid[10][10]
+ casos_covid[11][10] + casos_covid[12][10] + casos_covid[13][10] + casos_covid[14][10] + casos_covid[15][10]
+ casos_covid[16][10]
+ casos_covid[17][10]
+ casos_covid[18][10]
+ casos_covid[19][10]
+casos_covid[20][10]
+casos_covid[21][10]
+casos_covid[22][10]
+casos_covid[23][10]
+casos_covid[24][10]
+casos_covid[25][10]
+casos_covid[26][10]
+casos_covid[27][10]
+casos_covid[28][10]
+casos_covid[29][10]
+casos_covid[30][10]
+casos_covid[31][10]
+ casos_covid[32][10]
+casos_covid[33][10]
+casos_covid[34][10]
+casos_covid[35][10]
+casos_covid[36][10]
+casos_covid[37][10]
+casos_covid[38][10]

if soma_acumulados == 2074860:
    print(soma_acumulada)
    print(soma_acumulados == 2074860)

#i) 
print(len(casos_covid))

#j) 
obtos_novos = [
    casos_covid[1][-2], casos_covid[2][-2], casos_covid[3][-2], casos_covid[4][-2],  casos_covid[5][-2],
      casos_covid[6][-2],  casos_covid[7][-2],  casos_covid[8][-2],  casos_covid[9][-2],  casos_covid[10][-2], 
        casos_covid[11][-2],  casos_covid[12][-2],  casos_covid[13][-2],  casos_covid[14][-2],  casos_covid[15][-2], 
          casos_covid[16][-2], casos_covid[17][-2], casos_covid[18][-2], casos_covid[19][-2], casos_covid[20][-2], 
          casos_covid[21][-2], casos_covid[22][-2], casos_covid[23][-2], casos_covid[24][-2], casos_covid[25][-2], 
          casos_covid[26][-2], casos_covid[27][-2], casos_covid[28][-2], casos_covid[29][-2], casos_covid[30][-2], 
          casos_covid[31][-2], casos_covid[32][-2], casos_covid[33][-2], casos_covid[34][-2], casos_covid[35][-2], 
          casos_covid[36][-2], casos_covid[37][-2], casos_covid[38][-2]
]
print(min(obtos_novos))
print(max(obtos_novos))

#k) 
Acaua = {"Estado": "PI", "Casos novos": 0}
Agricolandia = {"Estado": "PI", "Casos novos": 2}
Teresina = {"Estado":"PI", "Casos novos": 328}, 

#l)
print(Teresina["Casos novos"])


