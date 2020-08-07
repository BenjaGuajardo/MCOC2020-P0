from scipy import matmul, rand
from numpy import *

def mimatmul(A,B):
    result=zeros((len(A),len(A)))
    C = []
    # iterate through rows of X
    for i in range(len(A)):
       # iterate through columns of Y
       for j in range(len(B[0])):
           # iterate through rows of Y
           for k in range(len(B)):
               result[i][j] += A[i][k] * B[k][j]
    for r in result:
        C.append(r)
    return C
#
#N=3
#A = rand(N,N)
#B = rand(N,N)
#
#C=mimatmul(A,B)
#D=A@B
#print (f'C= {C}')
#print (f'D= {D}')