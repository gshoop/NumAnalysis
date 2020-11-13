import numpy as np

def naiveGauss(A,b):
    n = len(b)
    x = np.zeros(n)
    for j in range (1,n-1):
        if np.abs(A[j][j]) < 0.0001:
            break
        for i in range(j+1,n):
            mult = A[i][j]/A[j][j]
            for k in range(j+1,n):
                A[i][k] = A[i][k] - mult*A[j][k]
            b[i] = b[i] - mult*b[j]
    # Back substitution
    for i in range(n,1,-1):
        for j in range(i + 1,n):
            b[i] = b[i] - A[i][j]*x[j]
        x[i] = b[i]/A[i][i]                     #Out of Range error here
    return x

