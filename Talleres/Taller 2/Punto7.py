import numpy as np

# funcion LU
def descomposicionLu(A):
    n = len(A[0])
    L = np.zeros([n,n])
    U = np.zeros([n,n])
    for i in range(n):
        L[i][i]=1
        if i == 0:
            U[0][0]=A[0][0]
            for j in range(1,n):
                U[0][j]=A[0][j]
                L[j][0]=A[j][0]/U[0][0]
        else:
            for j in range (i, n):
                temp=0
                for k in range (0,i):
                    temp = temp + L[i][k]*U[k][j]
                U[i][j]= A[i][j]-temp
            for j in range (i+1, n):
                temp=0
                for k in range (0,i):
                    temp = temp + L[j][k]*U[k][i]
                L[j][i] = (A[j][i]-temp)/U[i][i]
    return L,U 

#main
A = [[1,-8,-2],[1,1,5],[3,-1,1]]
L,U=descomposicionLu(A)
print(L,'\n',U)