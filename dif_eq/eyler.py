import numpy as np
def eyler(A, B, h, y0, f):
    # A and B - limits of method, y0 - precondition
    ar = np.linspace(A, B, num=h)
    # ar is a numpy array of x's
    yar = np.zeros(h)
    yar[0] = y0
    for i in range(1,h):
        yar[i] = yar[i-1]+f(ar[i-1],yar[i-1])*(B-A)/h
    print(ar, yar)
    return [ar,yar]
