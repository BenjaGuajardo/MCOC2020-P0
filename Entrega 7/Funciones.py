from numpy import zeros,double

def matriz_laplaciana_llena(N):
    A = zeros((N,N),dtype=double)
    for i in range(N):
        for j in range(N):
            if i==j:
                A[i,j]=2
            if i+1==j:
                A[i,j]=-1
            if i-1==j:
                A[i,j]=-1       
    return A

from scipy.sparse import lil_matrix, csr_matrix, csc_matrix

def matriz_laplaciana_dispersa(N):
    A_lil = lil_matrix((N,N),dtype=double) 
    for i in range(N):
        for j in range(N):
            if i==j:
                A_lil[i,j]=2
            if i+1==j:
                A_lil[i,j]=-1
            if i-1==j:
                A_lil[i,j]=-1
    A = csr_matrix(A_lil)
    return A

def matriz_laplaciana_dispersa_inv(N):
    A_lil = lil_matrix((N,N),dtype=double) 
    for i in range(N):
        for j in range(N):
            if i==j:
                A_lil[i,j]=2
            if i+1==j:
                A_lil[i,j]=-1
            if i-1==j:
                A_lil[i,j]=-1
    A = csc_matrix(A_lil)
    return A