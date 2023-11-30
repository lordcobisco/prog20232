
print ("Olá, seja bem vinda(o) ao porgrama de optogenética!")

print(" Para iniciar o programa você deverá configurar a cor do LED de acordo com o código RGB de cada cor: (1,2,3 para vermelho), ( 2,3,1 para verde), (3,1,2 para azul).")


def led_luz(): 
   onda = int(input("Insira o comprimemto de onda em nanometros: ")) 
   potencia = int(input("Insira a potência em mW mm²: ")) 
   print("Os parâmetros de estimulação setados foram:", onda,"nm", potencia,"mW mm²")

led_A= int(input("Insira o código RGB do LED com apenas um número:"))
led_B = int(input("Insira o código RGB do LED com apenas um número:"))
led_C = int(input("Insira o código RGB do LED com apenas um número:"))
cores_dos_leds = (led_A, led_B, led_C)

if cores_dos_leds == (1,2,3): 
    print("led vermelho acionado")
    led_luz() 
if cores_dos_leds ==(2,3,1):
    print("led verde acionado")
    led_luz() 
if cores_dos_leds ==(3,1,2):
    print("led azul acionado")
    led_luz()


import time,sys 
tempo = int(input("Insira o tempo para ativação do canal: ")) 
for temp in range(0, tempo): 
    sys.stdout.write("experimento ativado! {} ,".format(temp))
    sys.stdout.flush()
    time.sleep(1)

print ("experimento finalizada com socesso !")