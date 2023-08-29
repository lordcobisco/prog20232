peso = float (input ("digite seu peso (kg):"))
altura = float(input ("digite sua altura(m):"))
IMC = peso/(altura**2)
print ("seu IMC", IMC)

if IMC <17: 
    print("muito abaixo do peso")
elif IMC >= 17 and IMC <18.5:
    print("abaixo do peso")
elif IMC >= 18.5 and IMC <25:
    print("peso normal", )
elif  IMC >= 25 and IMC <30:
    print("acima do peso")
else:
    print("muito acima do peso")