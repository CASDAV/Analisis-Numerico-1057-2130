import numpy as np
import pylab as pl

def f(x,y):
    return y-x**2+np.cos(x)+1

def euler(f, x, y, h, m):
    u = np.zeros([m,2])
    for i in range(m):
        x += h
        y += h*f(x,y)
        u[i,0] = x
        u[i,1] = y
    return u

def eulerMejorado(f, x, y, h, m):
    u = np.zeros([m,2],dtype=float)
    for i in range(m):
        yn = y + h*f(x,y)
        y = y + h*(f(x,y) + f(x+h,yn))/2
        x += h
        u[i,0] = x
        u[i,1] = y
    return u


ua = eulerMejorado(f,0,1,0.1,20)
np.set_printoptions(precision=5)
pl.plot(ua[:,0],ua[:,1],'ob')
print(ua)
# np.set_printoptions(precision=16)