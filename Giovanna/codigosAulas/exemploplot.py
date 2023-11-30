# pesquisei no google plot real time 

import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 10, 0, 1])

for i in range(1000):
    y = np.random.random() #aquisição de dados novos, no OpenVibe vai ser o chump
    plt.scatter(i, y) # plotando pontos espaçados no gráfico 
    plt.pause(0.05) # atualizando o dado em tempo real, o suficiente para a tela randerizar, sem isso, ele só plota no final  

plt.show()