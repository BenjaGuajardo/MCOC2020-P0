from time import perf_counter
import scipy as sp
import scipy.linalg as spLinalg
import numpy as np
from numpy import float32

def matriz_laplaciana(N,dtype):
    A = np.zeros((N,N),dtype=dtype) 
    c = 0 
    for i in A: 
        i[c] = 2             
        if c == 0:       
            i[c+1] = -1     
        elif c == N-1:         
            i[c-1] = -1       
        else:         
            i[c-1] = -1
            i[c+1] = -1
        c += 1             
    return A

Ns = [2,3,10,12,15,20,30,40,45,50,
      55,60,75,100,125,160,200,250,
      350,500,600,800,1000,2000,5000,10000]

Ncorridas = 10

names = ['A_invB_inv.txt', 'A_invB_npSolve.txt']

files = [open(name, 'w') for name in names]

for N in Ns:
    
    #arreglo con N filas y len(files) columnas
    dts = np.zeros((Ncorridas, len(files)))
    
    for i in range(Ncorridas):
        
        #Mediante la inversa
        A = matriz_laplaciana(N,float32)
        B = np.ones(N)
        t1 = perf_counter()
        A_inv = np.linalg.inv(A)
        A_invB = A_inv@B
        t2 = perf_counter()
        dt = t2-t1
        dts[i][0]=dt #Agrega el dt a la respectiva fila de la primera columna
        
        #Mediante solver de numpy
        A = matriz_laplaciana(N,float32)
        B = np.ones(N)
        t1 = perf_counter()
        A_invB = np.linalg.solve(A,B)
        t2 = perf_counter()
        dt = t2-t1
        dts[i][1]=dt #Agrega el dt a la respectiva fila de la segunda columna
    
    #Tiempo promedio de cada columna para cada calculo
    dts_mean = [np.mean(dts[:,j]) for j in range(len(files))]
    
    #Se escribe, en el archivo de texto, los promedios para cada nombre
    for j in range(len(files)):
        files[j].write(f'{N} {dts_mean[j]}\n')
        files[j].flush

[file.close() for file in files]