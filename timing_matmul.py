from scipy import matmul, rand
from time import perf_counter

Ns = [3,7,10,13,17,20,30,40,48,49,50,60,63,65,70,100,110,150,200,300,400,500,600,800,1000,2000,5000,10000]

corridas = 10

for i in range(corridas):
   
    archivo=open(f'corrida {i}.txt','w') 
    c = 0
    
    for j in Ns:

        N = j
        
        A = rand(N,N)
        B = rand(N,N)
        
        t1 = perf_counter()
        
        C = A@B        
        
        t2 = perf_counter()
        
        dt = t2 - t1
        
        if c == len(Ns):
            archivo.write(f'{dt}')
        else:
            archivo.write(f'{dt}\r\n')
    
    archivo.close()

#solo guarde en .txt los tiempos. Para la memoria utilice la
#siguiente funcion en el codigo para graficar

memoria=[]
for i in Ns:
    n=i*i
    m=3*n*8
    memoria.append(m)