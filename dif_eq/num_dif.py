import numpy as np
import math as m
import matplotlib.pyplot as plt
# модуль с numpy массивами метода Эйлера eyler.py
from eyler import eyler
# модуль с numpy массивами метода Рунге-Кутты 4 порядка runge-kutta.py
from runge_kutta import rk
# ----------- input derivate parametres
# Ay+Bx+Cyx+Dyx2+Ey2+Fxy2+Gy2x2

def dif(x,y):
    #2 level derivate
    return y*A+x*B+y*x*C+y*x*x*D+y*y*E+y*y*x*F+y*y*x*x*G

x0, xn = [float(input()) for i in range(2)] # limits
acc = int(input()) # accurancy
# -----------
# Примеры. Для просмотра и построения один оставляем, остальные комментируем
# Экспонента метод Эйлера
A,B,C,D,E,F,G = 1, 0, 0, 0, 0, 0, 0
exp_eyler = rk(x0,xn,acc,2.72, dif)
plt.plot(exp_eyler[0], exp_eyler[1], color='red')
plt.plot(exp_eyler[0], np.exp(exp_eyler[0]), color='green')
plt.show()


# dy/dx = y*sin^2(x) метод Эйлера
dif_2 = lambda x, y: y*m.sin(x)*m.sin(x)
real = lambda x: m.exp(1/2*(x-m.sin(x)*m.cos(x)))
print(real(0))
exp_eyler_2 = eyler(0,50,acc,1, dif_2)
plt.plot(exp_eyler_2[0], exp_eyler_2[1], color='red')
plt.plot(exp_eyler_2[0], list(map(real, exp_eyler_2[0])), color='green')
plt.show()

# dy/dx = y*sin^2(x) Рунге-Кутта
dif_2 = lambda x, y: y*m.sin(x)*m.sin(x)
real = lambda x: m.exp(1/2*(x-m.sin(x)*m.cos(x)))
print(real(0))
exp_eyler_2 = rk(0,50,acc,1, dif_2)
plt.plot(exp_eyler_2[0], exp_eyler_2[1], color='red')
plt.plot(exp_eyler_2[0], list(map(real, exp_eyler_2[0])), color='green')
plt.show()