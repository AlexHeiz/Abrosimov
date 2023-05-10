import scipy as sc
from scipy import integrate
import numpy as np

x = np.arange(1, 11, 1)
# print(x[1])
# print(type(x))
n = 10
def integrating(n):
    spisok1 = []
    x = 10

    for a in range(x):
        spisok = []
        spisok1.append(spisok)
        for i in range(n):
            i = i+1
            spisok.append(i)
    return spisok1
print('+++++++', integrating(n))
a = integrating(n)
b = a[0]
print(a[0])
print(b[0])













# # опишем подынтегральную функцию

# result = integrate.quad(target_function_f, -np.pi, np.pi)
# print(result)
# print(result[0])
#
#
# # посмотрим результат
# print(type(result))

#
# a=10
# def summa(a):
#     new = []
#     for i in range(a):
#         i = i+i
#         new.append(i)
#         print(new)
#     return new
#
# print(summa(a))

