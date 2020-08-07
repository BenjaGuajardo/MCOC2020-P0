from numpy import *
from matplotlib import pyplot as plt
import math

x = [3,7,10,13,17,20,30,40,48,49,50,60,63,65,70,100,110,150,200,300,400,500,600,800,1000,2000,5000,10000]
x = [3,7,10,13,17,20,30,40,48,49,50,60,63,65,70,100,110,150,200,300,400,500]

corridas=3

time=[]
tiempo=[]

'''GRAFICO DE TIEMPO'''

for i in range(corridas):
    
    corrida=open(f'Corridas/mimatmul {i}.txt')
    lista_corrida_x=[]
    for linea in corrida:
        lista_corrida_x.append(float(linea))
    time.append(lista_corrida_x)
      
plt.subplot(2,1,1)

for i in range(len(time)):
    plt.plot(x,time[i],'-o')
    
ejex=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
ejey=[0.0001,0.001,0.01,0.1,1,10,60,600]
ejey_2=['0.1 ms','1 ms','10 ms','0.1 s','1 s','10 s','1 min','10 min']

plt.title('A@B')
plt.xscale('log')
plt.yscale('log')
plt.xticks(ejex,[],rotation=45) #tamanos de matriz
plt.yticks(ejey,ejey_2) #tiempo en segundos
plt.ylabel('Tiempo transcurrido')
plt.grid()
plt.axis([0,20000,0,600]) 

'''GRAFICO DE MEMORIA'''

memoria=[]
for i in x:
    n=i*i
    m=3*n*8
    memoria.append(m)

ejey_memoria=[1000,10000,100000,1000000,10000000,100000000,1000000000,10000000000]
ejey_memoria_2=['1 KB','10 KB','100 KB','1 MB','10 MB','100 MB','1 GB','10 GB']
plt.subplot(2,1,2)
plt.plot(x,memoria,'-o')
plt.plot([0,20000],[8000000000,8000000000],'--k')
plt.xscale('log')
plt.yscale('log')
plt.xticks(ejex,ejex,rotation=45)
plt.yticks(ejey_memoria,ejey_memoria_2)
plt.ylabel('Uso de memoria')
plt.xlabel('Tamaño matriz N')
plt.grid()
plt.axis([0,20000,0,40000000000]) 

plt.show()