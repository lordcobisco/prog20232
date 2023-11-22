#item a
habituacao = True

#item b
import time

dist_0 = 30.0 #cm
rec = False
som1 = False
som2 = False
bar_esq = False
bar_dir = False
etapa_2 = False
fase_2 = False
repeticoes = 19

time_0 = time.time()

dist = float(input("Distancia: "))
if dist<dist_0:
    rec = True
    repeticoes += 1
    rec=False

if repeticoes==20:
    etapa_2=True
    repeticoes=0

if som1==True and bar_esq==True:
    rec=True
    repeticoes += 1
    re=False
if som2==True and bar_dir==True:
    rec=True
    repeticoes += 1
    rec=False

if repeticoes>49 and time.time()>(30*60):
    fase_2 = True
    print()
