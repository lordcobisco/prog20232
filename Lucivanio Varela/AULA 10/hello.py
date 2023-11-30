# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np

# t = np.arange(0,2,0.01)
# s = 1+np.sin(2*np.pi*t)

# fig, ax = plt.subplots()
# ax.plot(t,s)
# plt.show()


import numpy as np
import matplotlib.pyplot as plt

# plt.axis([0, 10, 0, 1])

for i in range(1):
    y = np.random.random()
    plt.scatter(i,y)
    plt.pause(0.05)

plt.show()