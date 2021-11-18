import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

def f(x,y):
    return y-x**2+np.exp(x)+1

def rk4n(F, V, U, h, m):
    nF = len(F)
    nV = len(V)
    K1 = np.zeros([nF],dtype=sy.Symbol)
    K2 = np.zeros([nF],dtype=sy.Symbol)
    K3 = np.zeros([nF],dtype=sy.Symbol)
    K4 = np.zeros([nF],dtype=sy.Symbol)
    res = np.zeros([m,nV],dtype=float)
    T = list(np.copy(U))

    for p in range(m):
        for i in range(nF):
            K1[i] = F[i]
            K2[i] = F[i]
            K3[i] = F[i]
            K4[i] = F[i]
        for i in range(nF):
            for j in range(nV):
                K1[i] = K1[i].subs(V[j],float(T[j]))
            K1[i] = h*K1[i]
        for i in range(nF):
            K2[i] = K2[i].subs(V[0],float(T[0])+h/2)
            for j in range(1,nV):
                K2[i] = K2[i].subs(V[j],float(T[j])+K1[j-1]/2)
            K2[i] = h*K2[i]
        for i in range(nF):
            K3[i] = K3[i].subs(V[0],float(T[0])+h/2)
            for j in range(1,nV):
                K3[i] = K3[i].subs(V[j],float(T[j])+K2[j-1]/2)
            K3[i] = h*K3[i]
        for i in range(nF):
            K4[i] = K4[i].subs(V[0],float(T[0])+h)
            for j in range(1,nV):
                K4[i] = K4[i].subs(V[j],float(T[j])+K3[j-1])
            K4[i] = h*K4[i]
        T[0] = T[0]+h
        res[p,0] = T[0]
        for i in range(nF):
            T[i+1] = T[i+1] + (K1[i]+2*K2[i]+2*K3[i]+K4[i])/6
            res[p,i+1] = T[i+1]
    return res

def rk2(f, x, y, h, m):
    u = np.zeros([m,2],float)
    for i in range(m):
        k1 = h*f(x,y)
        k2 = h*f(x+h,y+k1)
        y = y + (k1+k2)/2
        x += h
        u[i,0] = x
        u[i,1] = y
    return u

def rk4(f, x, y, h, m):
    u = np.zeros([m,2],dtype=float)
    for i in range(m):
        k1 = h*f(x,y)
        k2 = h*f(x+h/2,y+k1/2)
        k3 = h*f(x+h/2,y+k2/2)
        k4 = h*f(x+h,y+k3)
        y = y + (k1+2*k2+2*k3+k4)/6
        x += h
        u[i,0] = x
        u[i,1] = y
    return u

def rk2n(F, V, U, h, m):
    
    nF = len(F)
    nV = len(V)
    K1 = np.zeros([nF],dtype=sy.Symbol)
    K2 = np.zeros([nF],dtype=sy.Symbol)
    res = np.zeros([m,nV],dtype=float)
    T = list(np.copy(U))

    for p in range(m):
        for i in range(nF):
            K1[i] = F[i]
            K2[i] = F[i]
        for i in range(nF):
            for j in range(nV):
                K1[i] = K1[i].subs(V[j],float(T[j]))
            K1[i] = h*K1[i]
        for i in range(nF):
            K2[i] = K2[i].subs(V[0],float(T[0])+h)
            for j in range(1,nV):
                K2[i] = K2[i].subs(V[j],float(T[j])+K1[j-1])
            K2[i] = h*K2[i]
        T[0] = T[0]+h
        res[p,0] = T[0]
        for i in range(nF):
            T[i+1] = T[i+1] + (K1[i]+K2[i])/2
            res[p,i+1] = T[i+1]
    return res

# ua = rk4(f,0,1,0.1,20)
# np.set_printoptions(precision=6)
# print(ua)
x,y,z = sy.symbols('x,y,z')
f = sy.exp(x)+y+z-1
g = y+sy.cos(x)-z
ua = rk4n([f,g],[x,y,z],[0,1,2],0.1,20)
np.set_printoptions(precision=6)
print(ua)