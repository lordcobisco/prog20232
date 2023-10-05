animalHabituado = input("O animal está habituado? Digite S para sim e N para não.")

if animalHabituado == "S":
    print ("Passe para o treinamento!")
else:
    print("Habitue-o.")

"""
Aqui se separam as fases de habituação e treinamento.
"""

distanciaBarra = int(30)
aproximacaoAnimal = float(input("O animal se aproximou da barra quantos centímetros aproximadamente?: "))

if distanciaBarra - aproximacaoAnimal < distanciaBarra:
    print("Liberar recompensa de 0,5ml")
else:
    print("Aguarde o animal se mexer")

vezesBarraTocada = int(input("O animal tocou na barra quantas vezes?: "))

if vezesBarraTocada >= 20:
    print("O experimento deve passar para a próxima fase!")
else:
    print("Aguarde no mínimo 20 vezes.")

somTocado = int(input("Você quer tocar o som 1 ou 2?"))
barraEsquerdaTocada = str(input("O animal tocou a barra esquerda?"))
barraDireitaTocada = str(input("O animal tocou a barra direita?"))

if (somTocado == 1 and barraEsquerdaTocada == "sim") or (somTocado == 2 and barraDireitaTocada == "sim"):
    print("Liberar recompensa de 0,5ml")
else:
    print("Não liberar nada!")

tempoLimite = input("O experimento foi realizado 50 vezes em 30 minutos ou menos?")

if tempoLimite == "S":
    print("Passe para a próxima fase!")
else:
    print("Continue nesta fase.")