from time import perf_counter
from scipy import rand, matmul
from numpy import double

Ns = [2,4,8,15,30,60,125,250,500,1000,2000,4000,8000]

Ncorridas = 4

for corrida in range(Ncorridas):
    
    print (f'corrida = {corrida}')
    name = f'matmul_matriz_llena_{corrida}.txt'
    
    file = open(name, 'w')
        
    for N in Ns:
           
        print (f'N = {N}')    
        
        t1 = perf_counter()
        
        A = rand(N,N)
        A = double(A)
        B = rand(N,N)
        B = double(B)
        
        t2 = perf_counter()

        C = A@B

        t3 = perf_counter()
        
        dt1 = t2-t1
        dt2 = t3-t2
        
        file.write(f'{N} {dt1} {dt2}\n')
        file.flush
    
    file.close() 