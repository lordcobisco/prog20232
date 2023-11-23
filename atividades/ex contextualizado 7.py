print('Iniciaremos a seguir o experimento de optogenética.')

iniciarEx = []
red = []
green = []
blue = []  
tempoEx = [] 
   
class dispositivo:
    def led(red,green,blue):
        intensidade=[]
        red = int(input('Digite a intensidade do led vermelho: '))
        green = int(input('Digite a intensidade do led verde: '))
        blue = int(input('Digite a intensidade do led azul: '))
    intensidade=led(red, green, blue)
    print('A intensidade dos leds regulados para o dispositivo foram: ', intensidade)

parar = input('Você deseja parar o experimento? (1 sim/ 2 nao)')
if parar == 1 : break 
else: continue

tempoEx = float(input('Qual o tempo do experimento? '))
matEletrodos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
eletrodos = print('As 32 variáveis reais que compõe a matriz de eletrodos são: ', matEletrodos)
rgb = print('As 3 variáveis do led RGB são: ', [red,green,blue])

parar = input('Você deseja parar o experimento? (sim/nao) ')
if parar == 'sim': Break
else: Continue

def canal():
    x = int(input('Quantos canais serão utilizados neste experimento? São possíveis até 32 canais. '))
    for i in range(0,x,32):
        print("Agora, digite os dados do canal ", i+1) 
        led()
        fimEx = time.time() - inicioEx
        print("Temporização: ", fimEx)    
canal()