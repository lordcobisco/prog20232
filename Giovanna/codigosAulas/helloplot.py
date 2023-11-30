import matplotlib 
import matplotlib.pyplot as plt
import numpy as np 

t = np.arange(0, 2, 0.01)
s = 1 + np.sin(2*np.pi*t)

fig, ax = plt.subplots()
ax.plot(t, s)
plt.show()
