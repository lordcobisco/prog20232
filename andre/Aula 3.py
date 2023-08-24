#%%

informacaoDoTeclado = int(input()) #entrada; lê info do teclado; cria uma variável; cria uma memória; tudo que for digitado e apertar enter no terminal vai ser gravado como essa variável
#int() é uma função que transforma a variável 'str' em número inteiro -> se eu digitar uma palavra no terminal vai dar erro
print(informacaoDoTeclado + 2) #saída; mostra info no terminal; tudo que eu colocar dentro do () vai ser printado

#%%
peso = float(input('Digite o seu peso (kg):')) #float aceita números com vírgula 
altura = float(input('Digite a sua altura(m)'))
imc = peso/(altura*altura) #processamento / ou altura**2 

print('Seu IMC é:', imc)
print('Estou muito abaixo do peso?', imc < 17) #colocar vírgula entre as saídas que eu quero
print('Estou abaixo do peso normal?', imc >= 17 and imc < 18.5) # OU (17 <= imc < 18.5)
print('Estou com o peso dentro do normal?', 18.5 <= imc < 25)
print('Estou acima do peso normal?', 25 <= imc < 30)
print('Estou muito acima do peso?', imc >= 30)



#%%
peso = float(input('Digite o seu peso (kg):')) #float aceita números com vírgula 
altura = float(input('Digite a sua altura(m)'))
imc = peso/(altura*altura) #processamento / ou altura**2 

print('Seu IMC é:', imc)
if imc < 17: #tem que ter os dois pontos ":"
    print('Você está muito abaixo do peso.') #o espaço tab da linha de baixo significa que essa linha só será executada se a linha acima for verdadeira. 
elif imc >= 17 and imc < 18.5:
    print('Você está abaixo do peso normal.')
elif 18.5 <= imc < 25:
    print('Você está com o peso dentro do normal.')
elif 25 <= imc < 30:
    print('Você está acima do peso normal.')
else:
    print('Você está muito acima do peso.') 

# %%
peso = float(input('Digite o seu peso (kg):')) #float aceita números com vírgula 
altura = float(input('Digite a sua altura(m)'))
imc = peso/(altura*altura) #processamento / ou altura**2 
imc = round(imc,1) #substituo a variável de cima por essa de baixo. 

print('Seu IMC é:', imc)
if imc < 17: #tem que ter os dois pontos ":"
    print('Você está muito abaixo do peso.') #o espaço tab da linha de baixo significa que essa linha só será executada se a linha acima for verdadeira. 
elif imc >= 17 and imc < 18.5:
    print('Você está abaixo do peso normal.')
elif 18.5 <= imc < 25:
    print('Você está com o peso dentro do normal.')
elif 25 <= imc < 30:
    print('Você está acima do peso normal.')
else:
    print('Você está muito acima do peso.') 
# %%
