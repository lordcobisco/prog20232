
# Método de discriminação de estímulos auditivos para primatas através do condicionamento operante
# Adaptação do problema para utilizar funções, principalmente os trechos de código dentro das estruturas de repetição.

def realizar_habituacao():
    Habituacao_animal = input("O animal está habituado? (sim ou não)?")
    if Habituacao_animal == "sim":
        print("Animal habituado!. Começar  o treinamento.")
        return True
    else:
        print("Realize a etapa de habituação")
        return False

def aproximacoes_sucessivas():
    print("APROXIMAÇÕES SUCESSIVAS")
    aproximacao = float(input("Quantos cm o animal se aproximou? "))
    if aproximacao <= 30:
        print("Liberar 0,5 mL de recompensa")
        return True
    else:
        print("Só liberar quando a aproximação ficar menor que 30cm")
        return False

def tocar_barra():
    return input("O sagui tocou 20x na barra? (sim ou não)") == "sim"

def emitir_som(recompensa):
    resposta = input(recompensa + " (sim ou não)")
    if resposta == "sim":
        print("Liberar 0,5 mL de recompensa")
    else:
        print("Não liberar recompensa")

def realizar_experimento():
    Tempo = float(input("Quanto tempo durou o experimento? "))
    Repeticoes = float(input("Quantas repetições foram realizadas? "))
    return Tempo < 30 and Repeticoes >= 50

# Chama as funções 
if realizar_habituacao():
    if aproximacoes_sucessivas():
        if tocar_barra():
            emitir_som("O som 1 foi emitido ao toque do animal na barra esquerda?")
            emitir_som("O som 2 foi emitido ao toque do animal na barra direita?")

if realizar_experimento():
    print("Experimento seguirá para a próxima fase")
else:
    print("O experimento não seguirá para a próxima fase")
