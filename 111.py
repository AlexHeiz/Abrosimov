import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


N = 20
def my_func(x):
    return  0.5*x+ 3.5 * ((1/np.power(1-(x/6.5), 2))-1)
# 1 - 0.5*x - 3.5 * ((1/np.power(1-(x/6.5), 2))-1)
#3.5 * ((1/np.power(1-(x/6.5),2))-1)

def integrate_a_0_koef(my_func):
    koef_a_0 = quad(my_func, -np.pi, np.pi)
    res = (1/(2*np.pi))*koef_a_0[0]
    return res



def func_cos(i):
    return lambda x:  (0.5*x+ 3.5 * ((1/np.power(1-(x/6.5), 2))-1))*np.cos((i*x))
    # (1 - 0.5 * x - 3.5 * ((1 / np.power(1 - (x / 6.5), 2)) - 1)) * np.cos((i * x))
    # return lambda x: 3.5 * ((1/np.power(1-(x/6.5),2))-1)*np.cos((i*x))

def func_sin(i):
    return lambda x:  (0.5*x+ 3.5 * ((1/np.power(1-(x/6.5), 2))-1))*np.sin((i*x))
    # (1 - 0.5 * x - 3.5 * ((1 / np.power(1 - (x / 6.5), 2)) - 1)) * np.sin((i * x))
    # return lambda x: 3.5 * ((1/np.power(1-(x/6.5),2))-1)*np.sin((i*x))
def koef_an_bn():
    mass_an = []
    mass_bn = []
    for i in range(1, N):
        result1 = quad(func_cos(i), -np.pi, np.pi)
        result_result1 = result1[0]*(1/(2*np.pi))
        mass_an.append(result_result1)
        result2 = quad(func_sin(i), -np.pi, np.pi)
        result_result2 = result2[0]*(1/(2*np.pi))
        mass_bn.append(result_result2)
    return mass_an, mass_bn

an_values = koef_an_bn()[0]
bn_values = koef_an_bn()[1]
x = np.linspace(-3*np.pi, 3*np.pi, 1000)
y = my_func(x)
fig, ax = plt.subplots()

#all garmonics
# y1 = (integrate_a_0_koef(my_func)/2) + an_values[0]*np.cos(x/2)+bn_values[0]*np.sin(x/2)
# ax.plot(x, y1, linewidth=1.0, color='gray')
# for i in range(1, N):
#     if i == N-1:
#         break
#     y1 += an_values[i]*np.cos((i*x)/2)+bn_values[i]*np.sin((i*x)/2)
#     ax.plot(x, y1, linewidth=1.0, color='gray')

#last garmonic
y1 = (integrate_a_0_koef(my_func)/2) + an_values[0]*np.cos(x)+bn_values[0]*np.sin(x)
# y1 = (integrate_a_0_koef(my_func)/2) + an_values[0]*np.cos(x/2)+bn_values[0]*np.sin(x/2)
# ax.plot(x, y1, linewidth=1.0, color='gray')
for i in range(1, N):
    if i == N-1:
        break
    y1 += an_values[i]*np.cos((i*x))+bn_values[i]*np.sin((i*x))
    # y1 += an_values[i] * np.cos((i * x) / 2) + bn_values[i] * np.sin((i * x) / 2)
    if i == N-2:
        ax.plot(x, y1, linewidth=1.0, color='red')





ax.plot(x, y, linewidth=3.0, color='grey')

plt.axvline(x=0, color='black', label='X')
plt.axhline(y=0, color='black', label='Y')

ax.set(xlim=(-3*np.pi, 3*np.pi), xticks=np.arange(-3*3, 3*3),
       ylim=(-3, 6), yticks=np.arange(-3, 6))
plt.grid(True)
plt.show()