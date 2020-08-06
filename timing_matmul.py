from scipy import matmul, rand
from time import perf_counter

x = [3,7,10,13,17,20,30,40,48,49,50,60,63,65,70,100,110,150,200,300,400,500,600,800,1000,2000,5000,10000]
 
for i in range(10):
   
    archivo=open(f'corrida {i}.txt','w') 

    for j in x:
       
        N = j
        
        A = rand(N,N)
        B = rand(N,N)
        
        t1 = perf_counter()
        
        C = A@B        
        
        t2 = perf_counter()
        
        dt = t2 - t1
        
        if i!=9:
            archivo.write(f'{dt},')
        else:
            archivo.write(f'{dt}')
   
    archivo.close()  