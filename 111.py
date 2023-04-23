import matplotlib.pyplot as plt
import numpy as np



fig = plt.subplots()
x = np.linspace(-np.pi, np.pi/2, 100)
y = np.exp(x)*np.sin(2*x)
plt.plot(x, y, "r-")

ax = plt.gca()
ax.spines['left'].set_position("center")
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.set_xlabel("X", fontsize=15, color='blue', labelpad=120)    # +
ax.set_ylabel("Y", fontsize=15, color='orange', labelpad=140)  # +

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')



plt.show()