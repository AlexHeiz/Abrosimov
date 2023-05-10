import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


N = 70

def my_func(x):
    return np.exp(x) - 1


def integrate_a_0_koef(my_func):
    koef_a_0 = quad(my_func, -np.pi, np.pi)
    res = (1/(np.pi))*koef_a_0[0]
    return res



def func_cos(i):
    return lambda x: (np.exp(x) - 1) * np.cos((i*x)/2)

def func_sin(i):
    return lambda x: (np.exp(x) - 1) * np.sin((i*x)/2)

def koef_an_bn():
    mass_an = []
    mass_bn = []
    for i in range(N):
        result1 = quad(func_cos(i), -np.pi, np.pi)
        result_result1 = result1[0]*(1/(2*np.pi))
        mass_an.append(result_result1)
        result2 = quad(func_sin(i), -np.pi, np.pi)
        result_result2 = result2[0]*(1/(2*np.pi))
        mass_bn.append(result_result2)
    return mass_an, mass_bn

an_values = koef_an_bn()[0]
bn_values = koef_an_bn()[1]
x = np.linspace(-np.pi, np.pi, 100)
y = my_func(x)
fig, ax = plt.subplots()


y1 = (integrate_a_0_koef(my_func)/2) + an_values[0]*np.cos(x/2)+bn_values[0]*np.sin(x/2)
ax.plot(x, y1, linewidth=1.0, color='gray')
for i in range(N):
    if i == N:
        break
    y1 += an_values[i]*np.cos((i*x)/2)+bn_values[i]*np.sin((i*x)/2)
    ax.plot(x, y1, linewidth=1.0, color='gray')


ax.plot(x, y, linewidth=3.0)

plt.axvline(x=0, color='black', label='X')
plt.axhline(y=0, color='black', label='Y')

ax.set(xlim=(-2*np.pi, 2*np.pi), xticks=np.arange(-6, 6),
       ylim=(-3, 10), yticks=np.arange(-3, 10))
plt.grid(True)
plt.show()