from scipy import linalg, zeros
from numpy import matrix, half, single, double, longdouble
from time import perf_counter

Ns = [
    2, 5, 10,
    12, 15, 20,
    30, 40, 45, 50, 55,
    60, 75, 100,
    125, 160, 200,
    250, 350, 500,
    600, 800, 1000,
    2000]

corridas = 10

for corrida in range(corridas):
        
    archivo=open(f'caso_2_half {corrida}.txt','w')

    for n in Ns:
        
        A = zeros((n,n))
        
        contador = 0
        
        for i in A:
            
            i[contador] = 2
                    
            if contador == 0:
                
                i[contador+1] = -1
            
            elif contador == n-1:
                
                i[contador-1] = -1  
            
            else:
                
                i[contador-1] = -1
                i[contador+1] = -1
                
            contador += 1             
         
        A = half(A) 
           
        memoria=n*n*2 #Half
        
        t1 = perf_counter()
        
        Ainv = linalg.inv(matrix(A),overwrite_a=False)
        
        t2 = perf_counter()
        
        dt = t2 - t1
        
        archivo.write(f'{n} {dt} {memoria}\n')
            
    archivo.close()