from scipy import rand
from mimatmul import mimatmul
from time import perf_counter

#Ns = [3,7,10,13,17,20,30,40,48,49,50,60,63,65,70,100,110,150,200,300,400,500,600,800,1000,2000,5000,10000]
Ns = [3,7,10,13,17,20,30,40,48,49,50,60,63,65,70,100,110,150,200,300,400,500]
corridas = 9

for i in range(corridas):
   
    archivo=open(f'mimatmul {i}.txt','w') 
    c = 0
    
    for j in Ns:
        
        c +=1

        N = j
        
        A = rand(N,N)
        B = rand(N,N)
        
        t1 = perf_counter()
        
        C = mimatmul(A,B)        
        
        t2 = perf_counter()
        
        dt = t2 - t1
        
        if c == len(Ns):
            archivo.write(f'{dt}')
        else:
            archivo.write(f'{dt}\r\n')

    archivo.close()