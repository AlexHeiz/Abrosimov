import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


itter_num = 7

def my_func(x):
    return np.exp(x)*np.sin(2*x)*np.cos(x)

def my_func_for_an(x):
    itter_num = 7
    for i in range(1, itter_num):
        return np.exp(x)*np.sin(2*x)*np.cos(i*x)

koef_a_0 = quad(my_func, -np.pi, np.pi)
print(koef_a_0[0])



def integrate_a_0_koef(my_func):
    koef_a_0 = quad(my_func, -np.pi, np.pi)
    res = (1/(2*np.pi))*koef_a_0[0]
    return res
a_0_koef = integrate_a_0_koef(my_func)
print('11111', a_0_koef)


def Furie_an(my_func_for_an):
    mass = []
    n = 7
    for i in range(len(my_func_for_an)):
        print(i)
        koef_a_n = quad(my_func_for_an, -np.pi, np.pi)
        mass.append(koef_a_n[0])
    return print('ffffffffffffffff', mass)




def not_intergrate():
    mass = []
    x = np.arange(-np.pi, np.pi, 0.01)
    for i in x:
        a = i*2
        mass.append(a)
    return mass
# print(not_intergrate())
print(len(not_intergrate()))

# for i in range(intergrate()):
#     r = i*2
#     print(r)




# def koef_a_n(x, itter_num):
#     mass_1 = []
#     for i in range(1, itter_num):
#         print(i)
#         # i = i
#         a = (np.exp(x)*np.sin(2*x))*np.cos(i*x)
#         mass_1.append(a)
#     return mass_1
# # koef_a_n(itter_num)
# print('1111111', koef_a_n(x, itter_num))







# print(result[0])
# print(list)
# list.append(result)
# print(list[0])

# def integrating():
#     spisok1 = []
#     x = 10
#     n = 10
#     for a in range(x):
#         spisok = []
#         spisok1.append(spisok)
#         for i in range(n):
#             i = i+1
#             spisok.append(i)
#     return spisok1
# print('+++++++', integrating())
# a = integrating()
# b = a[0]
# print(a[0])  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] <-- result a[0]
# print(b[0])  1 <-- result b(a[0])