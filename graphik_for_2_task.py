import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


N = 70

x = np.linspace(-3*np.pi, 3*np.pi, 1000)

fig, ax = plt.subplots()

#all garmonics
y1 = -np.sin(x)
# y1 = -(1/2)*np.sin(x)
# ax.plot(x, y1, linewidth=1.0, color='gray')
for i in range(1, N):
    if i == N-1:
        break
    y1 += (np.power( -1, i) * 2*(i+1)*np.sin((i)*x))/((i)*(i+1))
    # y1 += (np.power(-1, i + 1) * 2 * (i + 1) * np.sin((i + 1) * x)) / ((2 * i - 1) * (2 * i + 1))
    ax.plot(x, y1, linewidth=1.0, color='gray')

#last garmonic
# y1 = -(1/2)*np.sin(x)
#
# ax.plot(x, y1, linewidth=1.0, color='gray')
# for i in range(1, N):
#     if i == N-1:
#         break
#     y1 += (np.power( -1, i+1) * 2*(i+1)*np.sin((i+1)*x))/((2*i-1)*(2*i+1))
#     # y1 += an_values[i] * np.cos((i * x) / 2) + bn_values[i] * np.sin((i * x) / 2)
#     if i == N-2:
#         ax.plot(x, y1, linewidth=1.0, color='red')




y1 = -np.sin(x)

# ax.plot(x, y1, linewidth=1.0, color='gray')
for i in range(1, N):
    if i == N-1:
        break
    y1 += (np.power( -1, i) * 2*(i+1)*np.sin((i)*x))/((1+i)*(i))
    # y1 += an_values[i] * np.cos((i * x) / 2) + bn_values[i] * np.sin((i * x) / 2)
    if i == N-2:
        ax.plot(x, y1, linewidth=1.0, color='red')





# ax.plot(x, y, linewidth=3.0, color='grey')

plt.axvline(x=0, color='black', label='X')
plt.axhline(y=0, color='black', label='Y')

ax.set(xlim=(-3*np.pi, 3*np.pi), xticks=np.arange(-3*3, 3*3),
       ylim=(-4, 4), yticks=np.arange(-4, 4))
plt.grid(True)
plt.show()