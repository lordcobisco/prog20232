
# Esse programa tem o objetivo de auxiliar na realização de uma cirurgia esterotáxica em ratos

# Parte 1 - Anestesia 
print("Parte 1 - Anestesia")
pesoRato = float(input("Informe o peso do seu animal em Kg: "))

# O cálculo do volume é (de acordo com o POP)
    # ketamina - (70 x peso em kg)/100 
    # xilazina - (3 x peso em kg)/20 
    # resultado em mL 
volumeKetamina = (70*pesoRato)/100
volumeXilazina = (3*pesoRato)/20
print("Aplique ", volumeKetamina, "mL de ketamina e ", volumeXilazina, "mL de xilazina")
input("Aperte em qualquer tecla para continuar...")

# Parte 2 - Poscionamento do animal no estereotáxico 
print("Parte 2 - Posicionamento no estereotáxico")
print("As barras que suportam o peso do animal devem ser posicionadas no ouvido externo do animal.")
posiconamento = int(input("Verifique a angulação da cabeça do animal. Ela deve estar sem diferenças de angulação entre o bregma e o lambda, para ter uma superfície de cirurgia plana. A angulação está correta? Digite 1 para SIM ou 0 para NÃO."))
while posiconamento == 0: 
    posiconamento = int(input("Para seguir com o procedimento, é preciso ajustar bem a angulação. Lembre-se que a cabeça do animal deve estar sem diferenças de angulação entre o bregma e o lambda, para ter uma superfície de cirurgia plana. A angulação está correta? Digite 1 para SIM ou 0 para NÃO.\n"))

# Parte 3 - Limpeza do campo de trabalho 
input("Parte 3 - Limpeza do campo de trabalho")
input("Passo I - Retire a pelagem que recobre a parte superior da calota craniana")
input("Passo II - Retire os tecidos moles (epiderme, derme e tecido conjuntivo) até alcançar a parte óssea da caixa craniana.")
input("Passo III - Limpe a calota craniana de qualquer resto de “pele” que esteja sobrando utilizando H 2 O 2 10 volumes.")
input("Passo IV - Utilize uma pequena camada de poliacrilato em todo o perímetro externo para evitar sangramentos.")

# Parte 4 - Posicionamento dos parafusos 
print("Parte 4 - Posicionamento dos parafusos")
input("Deve-se escolher um ponto para a fixação de parafusos, de preferência na parte posterior da calota craniana, pois a camada óssea é mais espessa e suporta uma maior profundidade do parafuso. Obs: Cuidar para não aprofundar muito o parafuso. Com parafusos maiores deve-se dar até 3 voltas no parafuso.")

# Parte 5 - Cálculos 
print("Parte 5 - Cálculos das coordenadas")
print("Posicione a agulha sobre o bregma. Depois de posicionar...")
referencias = {}
referencias['AP'] = float(input("Informe o valor encontrado na régua Antero-Posterior do estereotáxico: ")) 
referencias['LL'] = float(input("Informe o valor encontrado na régua Latero-Lateral do estereotáxico: "))
referencias['DV'] = float(input("Informe o valor encontrado na régua Dorso-Ventral do estereotáxico: "))

coordenadas = [1, 2, 3]
coordenadas[0] = float(input("Informe a coordenada Antero-Posterior da região da cirurgia:")) 
coordenadas[1] = float(input("Informe a coordenada Latero-Lateral da região da cirurgia (valor positivo):"))
coordenadas[2] = float(input("Informe a coordenada Dorso-lateral da região da cirurgia:"))

posicoes = (
    referencias['AP'] + coordenadas[0], 
    referencias['LL'] + coordenadas[1],
    referencias['LL'] - coordenadas[1],
    referencias['DV'] + coordenadas[2]
)

# Parte 6 - Introdução da primeira cânula-guia
print("Parte 6 - Introdução da cânula guia")
print("As coordenadas para o ponto de inserção da clánula guia para o hemisfério 1 são:\n",
      "AP - ", posicoes[0], "\n",
      "LL - ", posicoes[1], "\n",
      )
input("Posicione a agulha das coordenadas acima e faça um furo com a broca até alcançar as meninges.")
print("Introduza a cânula-guia previamente confeccionada até o valor Dorso-Ventral: ", posicoes[3])
print("Logo após, drene qualquer sangue ou líquido cefalorraquidiano que esteja saindo pelo orifício criado no crânio. Para isso utilize pequenos rolos de papel absorvente.")

# Parte 7 - Confecção de parte do capacete
print("Parte 7 - Confecção da primeira parte do capacete")
print("Faça uma mistura do acrílico polimerizante com o solvente até ficar com textura espessa porém maleável (o ideal é que a mistura seja capaz de cobrir a parte desejada sem escorrer por todo o crânio). Com essa mistura faça um capacete abrangendo o crânio, a cânula-guia e o parafuso. Deixe secar até ficar suficientemente rígido. O tempo de secagem varia de acordo com a temperatura e umidade da sala.")

# Parte 8 - Introdução da segunda cânula-guia
print("Parte 6 - Introdução da cânula guia")
print("As coordenadas para o ponto de inserção da clánula guia para o hemisfério 2 são:\n",
      "AP - ", posicoes[0], "\n",
      "LL - ", posicoes[2], "\n",
      )
input("Posicione a agulha das coordenadas acima e faça um furo com a broca até alcançar as meninges.")
print("Introduza a cânula-guia previamente confeccionada até o valor Dorso-Ventral: ", posicoes[3])
input("Logo após, drene qualquer sangue ou líquido cefalorraquidiano que esteja saindo pelo orifício criado no crânio. Para isso utilize pequenos rolos de papel absorvente.")
print("Use a mistura do acrílico polimerizante com o solvente para finalizar o capacete abrangendo o crânio, a cânula-guia e o parafuso. Deixe secar até ficar suficientemente rígido. De preferência espalhar o cimento sobre a maior área do crânio, sempre deixando um espaço entre o capacete e o início da área tecidual. Este cuidado previne de um futuro descolamento do capacete devido a entrada de sangue u outro líquido entre o capacete e o crânio.")

# Parte 9 - Finalização
print("Acomodar o animal em uma caixa aquecida por uma lâmpada e sem outros animais acordados. Assim que o animal despertar colocá-lo de volta a sua caixa-moradia.")
statusCirurgia = int(input("A cirurgia teve alguma complicação? Digite 1 para SIM e 0 para NÃO"))
if statusCirurgia == 1: 
    print("Registre no livros de cirurgia e entre em contato com o médico veterinário responsável para informar.")
else:
    print("Não esqueça de acompanhar o animal no pós-operatório!")