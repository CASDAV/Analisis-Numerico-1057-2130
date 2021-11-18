import sympy as sp
import numpy as np

def derive(f,nd):
    t=f
    for j in range(1,nd+1):
        d=sp.diff(f.subs(y,y(x)),x)
        f = d.subs(sp.Derivative(y(x),x),t).subs(y(x),y)
    return f

def taylor(f,a,b,h,m,k):
    u = np.zeros([m,2])
    D = [ ]
    for j in range(1,k+1):
        D = D+[derive(f,j)]
    for i in range(m):
        g = f.subs(x,a).subs(y,b)
        t = b+h*g
        for j in range(1,k+1):
            z = D[j-1].subs(x,a).subs(y,b)
            t = float(t+h**(j+1)/sp.factorial(j+1)*z)
        b=t
        a=a+h
        u[i,0]=a
        u[i,1]=b
    return u

x,y = sp.symbols('x,y')
f = y+x-x**2+1
ua = taylor(f,0,1,0.1,5,3) 
print(ua)