from scipy import zeros
from numpy.linalg import inv
from numpy import matrix
from time import perf_counter

Ns = [
    2, 5, 10,
    12, 15, 20,
    30, 40, 45, 50, 55,
    60, 75, 100,
    125, 160, 200,
    250, 350, 500,
    600, 800, 1000,
    2000, 5000, 10000]

corridas = 1

for corrida in range(corridas):
    
    archivo=open(f'caso_1_single {corrida} prueba.txt','w')
    
    #for n in range(3,N+1):
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
    
        A = single(A) 
           
        memoria=n*n*4 #averiguar cuanta memoria se ocupa segun numeros
        
        t1 = perf_counter()
        
        Ainv = inv(matrix(A))
        
        t2 = perf_counter()
        
        dt = t2 - t1
        
        archivo.write(f'{n} {dt} {memoria}\n')
            
    archivo.close()
    
#linalg solo acepta single y double
#half = 16 bits = 2 B
#single = 
#double = 
#longdouble = 128 bits