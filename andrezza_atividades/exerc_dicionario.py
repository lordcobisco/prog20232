# USANDO FOR E DICIONARIO
dicionario = {
    "Brasil":[1,2,2,1,4,5,3],
    "EUA" :[3,4,56,3,6,4,2]
}
for pais in dicionario:
    print(pais)
    print(dicionario[pais])

# USANDO  WHILE
acabouPrograma = False
while not acabouPrograma:
    acabouPrograma=input() == "x"
    pass

while True:
    if input() == "x":
        break
    pass

