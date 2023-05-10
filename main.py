import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


x = np.linspace(-np.pi, np.pi, 100)
y = np.exp(x)*np.sin(2*x)

fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)
plt.axvline(x=0, color='black', label='X')
plt.axhline(y=0, color='black', label='Y')

ax.set(xlim=(-np.pi, np.pi), xticks=np.arange(-3, 3),
       ylim=(-1, 4), yticks=np.arange(0, 4))
plt.grid(True)
plt.show()
