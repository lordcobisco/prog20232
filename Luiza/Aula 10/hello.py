import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Para plotar precisa-se, pelo menos, do eixo X e do eixo Y:
#t = np.arange(0,2,0.01)
#s = 1 + np.sin(2*np.pi*t)

#fig,ax = plt.subplots()
#ax.plot(t,s)  #Posso colocar quantos plots que eu quiser
#plt.show()

#plt.axis([0,10,0,1])

#Isso serve para fazer clusterização
for i in range(1000):
    y = np.random.random()
    plt.scatter(i,y)
    plt.pause(0.05)

plt.show()
    
