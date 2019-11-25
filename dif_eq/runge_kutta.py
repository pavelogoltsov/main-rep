import numpy as np
def rk(A, B, h, y0, f):
    # A and B - limits of method, y0 - precondition
    ar = np.linspace(A, B, num=h)
    # ar is a numpy array of x's
    yar = np.zeros(h)
    yar[0] = y0
    k1=0;k2=0;k3=0;k4=0
    hh = (B - A) / h
    for i in range(1,h):
        k1=f(ar[i-1],yar[i-1])
        k2=f(ar[i-1]+hh/2,yar[i-1]+k1*hh/2)
        k3=f(ar[i-1]+hh/2,yar[i-1]+k2*hh/2)
        k4=f(ar[i-1]+hh,yar[i-1]+hh*k3)
        yar[i] = yar[i-1]+hh/6*(k1+2*k2+2*k3+k4)
        print(i, k1, k2, k3, k4, yar[i])
    print(ar, yar)
    return [ar,yar]