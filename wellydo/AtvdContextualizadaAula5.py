from pandas.core.indexes.base import FrozenList
import pandas as pd

covid_table = pd.read_csv('/content/HIST_PAINEL_COVIDBR_2023_Parte1_04out2023.csv', sep=';') #importando tabela baixada do site

regioes_only = covid_table.drop_duplicates(subset=['nomeRegiaoSaude'])

estados_only = regioes_only.drop_duplicates(subset=['estado'])

lista_covid = estados_only.to_dict(orient='records')

tupla_covid = tuple(lista_covid)

casosAcumuladosLista = next((d.get("casosAcumulado") for d in lista_covid if d.get("estado") == "RJ"), None)

print("Lista:", casosAcumuladosLista)

casosAcumuladosTupla = next((d.get("casosAcumulado") for d in tupla_covid if d.get("estado") == "RJ"), None)

print("Tupla:", casosAcumuladosTupla)

colunasobitoacu_filtro = ['estado', 'obitosAcumulado']

obitos_only = estados_only[colunasobitoacu_filtro]

chave_de_interesse = "estado"
valor_da_chave = "PB"
chave_alterar = 'obitosNovos'
novo_valor_ob = 10

for d in lista_covid:
  if d.get(chave_de_interesse) == valor_da_chave:
    d[chave_alterar] = novo_valor_ob

lista_covid

for d in tupla_covid:
  if d.get(chave_de_interesse) == valor_da_chave:
    d[chave_alterar] = novo_valor_ob

tupla_covid

filtro_municipios = covid_table['estado'] == "PB"

municipios_tabela = covid_table[filtro_municipios]
municipios_tabela = municipios_tabela.drop_duplicates(subset=['municipio'])

for i in municipios_tabela:
   lista_covid.append(i)

unwanted_keys = ['nomeRegiaoSaude', 'codRegiaoSaude']
updated_lista_covid = []

for item in lista_covid:
    if isinstance(item, dict):
        for key in unwanted_keys:
            item.pop(key, None)
        updated_lista_covid.append(item)
    else:
        updated_lista_covid.append(item)


# Faltou realizar as seguintes etapas:
# Verifique se a soma dos dados dos municípios na data de 18/08/2020 é igual ao dado da lista, mostrando na tela apenas se for verdadeiro.
# Retorne o tamanho total da lista.
# Verifique qual é o maior valor numérico de óbitos novos e o menor valor numérico de óbitos novos.
# Crie um dicionário de forma que seja possível encontrar os municípios associados a um estado específico e extrair os dados de casos novos em apenas um comando.
# Extraia os dados de Teresina/PI apresentando os casos novos com um print.
