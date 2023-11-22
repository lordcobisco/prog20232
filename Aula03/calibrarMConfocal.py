print("Sistema de Microscópio confocal.")
  
#Dados de entrada do Microscópio
print("Calibração do equipamento:") 
  tipo_celula=input("Qual tipo de célula:")
  comprimento_ondadaluz=float(input("Insira o comprimento de onda desejada em (nm):"))
  intensidade_dolazer=float(input("Insira a intensidade do laser desejada (W):"))
  abertura_numerica=float(input("Insira o valor de abertura desejada :"))
  varredurax=float(input("Insira o eixo X da varredura:"))
  varreduray=float(input("Insira o eixo Y da varredura:"))
  varreduraz=float(input("Insira o eixo Z da varredura:"))
  resolucao_espacial=float(input("Insira a resolução espacial desejada em (nm) ou (um):"))
  resolucao_espectral=float(input("Insira a resolução espectral desejada em (nm):"))
  Filtro_emissao=float(input("insira a faixa de comprimento de onda (nm):"))
  Tempo_exposicao=float(input("Insira o tempo de expoisição em segundos:"))


# Exibir informações para calibração
print("Configurações setadas pelo usuário são:")
print(f"Tipo de célula: {tipo_celula}")
print(f"Comprimento de onda desejado: {comprimento_ondadaluz} (nm)")
print(f"Intensidade do laser desejada: {intensidade_dolazer} (W)")
print(f"Abertura numérica desejada: {abertura_numerica}")
print(f"Varredura X: {varredurax}")
print(f"Varredura Y: {varreduray}")
print(f"Varredura Z: {varreduraz}")
print(f"Resolução espacial desejada: {resolucao_espacial} (nm/µm)")
print(f"Resolução espectral desejada: {resolucao_espectral} (nm)")
print(f"Faixa de comprimento de onda: {Filtro_emissao} (nm)")
print(f"Tempo de exposição: {Tempo_exposicao} (s)")

#Calibração horizontal 
print("Para calibração do eixo horizontal utilize o primeiro e ultimo caractere * (10), do seu nome")
  caractere_inicial=input("Digite a primeira letra do seu nome:")
  caractere_final= input("Digite a ultima letra do seu nome:")
  calibracao= input("Inicie a calibração: ")
  verificador = [calibracao]

for letra in calibracao:
 print("caractere digitado",letra)
if letra [:10] != caractere_inicial * 10:
 print("Erro na calibração, verifique os caracteres digitados")
elif letra [-10:] != caractere_final * 10:
 print("Erro na calibração, verifique os caracteres digitados")
else:
    print("Calibração Horizontal realizada com sucesso")

#Calibração Vertical
print("Para calibração do eixo vertical utilize o segundo e penultimo caractere * (10), do seu nome")
  caractere_segundo=input("Digite a segunda letra do seu nome:")
  caractere_penultimo= input("Digite a penultima letra do seu nome:")
  calibracao= input("Inicie a calibração: ")

for letra in calibracao:
 print("caractere digitado",letra)
if letra [:10] != caractere_segundo * 10:
 print("Erro na calibração, verifique os caracteres digitados")
elif letra [-10:] != caractere_penultimo * 10:
 print("Erro na calibração, verifique os caracteres digitados")
else:
    print("Calibração Vertical realizada com sucesso")
    print("Calibração do sistema foi realizada com sucesso!")
