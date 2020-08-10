from numpy import *

def mimatmul(A,B):
    result=zeros((len(A),len(A)))
    C = []
    # filas de X
    for i in range(len(A)):
       # columnas de Y
       for j in range(len(B[0])):
           #  filas de Y
           for k in range(len(B)):
               result[i][j] += A[i][k] * B[k][j]
    for r in result:
        C.append(r)
    return C