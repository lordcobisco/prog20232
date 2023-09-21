# Problema experimento com 
# coleta e processamento 

# dados (entrada e saída)
# tempo? 

def coletarDados(tempoExperimento, frequenciaSensor): # o nome da função é um verbo/ação
    qtdDados = tempoExperimento*frequenciaSensor
    # coleta
    """
    Essa função é só para colocar os dados
    """
    dado = []
    for contador in range(qtdDados):
        dado.append(float(input()))
    return dado

# processamento 
def integrar(dado, frequenciaSensor): 
    for data in dado: 
        soma = soma + (1 / frequenciaSensor) * dado
    return soma

tempo = 1 
freq = 1 
integral = integrar(coletarDados(tempo, freq), freq)

processar = integrar # integrar não é uma coisa, é uma memória/abstração, pode generalizar e usar de outras formas 
processar(coletarDados(tempo, freq), freq)

# processar = {"int":integrar}
# processar["int"](coletarDados(tempo, freq), freq)