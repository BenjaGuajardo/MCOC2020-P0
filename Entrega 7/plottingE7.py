from matplotlib import pyplot as plt
import numpy as np

def unicode_exp(exp):
    if exp == 1:
       return chr(0xB9)
    if exp == 2 or exp == 3:
       return chr(0xB0 + exp)
    else:
       return chr(0x2070 + exp)

imagen = 'inv_matriz_llena'
titulo = 'INVERSA MATRIZ LLENA'
names = ['inv_matriz_llena_0.txt',
         'inv_matriz_llena_1.txt',
         'inv_matriz_llena_2.txt',
         'inv_matriz_llena_3.txt']

N = np.array([2,4,8,15,30,60,125,250,500,1000,2000,4000,8000,16000])#poner 16000 por matmul
plt.figure()

for name in names:
    
    data = np.loadtxt(name)
    Ns = data[:,0]
    dts1 = data[:,1]
    dts2 = data[:,2]
    
    plt.subplot(2,1,1) 
    plt.loglog(Ns,dts1, 'k-o', linewidth=1.5, alpha = 0.5, markersize = 3)  

    plt.subplot(2,1,2) 
    plt.loglog(Ns,dts2, 'k-o', linewidth=1.5, alpha = 0.5, markersize = 3)
 
plt.subplot(2,1,1)

plt.hlines(dts1[13],0,16000,colors='b',linestyle='--',color='dodgerblue')#cambiar numero por matmul +1 y 16000

exp = [1,0.5,1/3,0.25]
data = dts1[13]#cambiar numero por matmul +1
L = []

for i in exp:
    data = data**i
    datos = []
    for i in range(14):#cambiar numero por matmul +1
        datos.append(data)
        data = data/2
    datos.sort()
    L.append(datos)
    data = dts1[13]#cambiar numero por matmul +1

plt.loglog(N,np.array(L[0]),'--',color='darkorange')
plt.loglog(N,np.array(L[1])**2,'--',color='limegreen')
plt.loglog(N,np.array(L[2])**3,'--',color='crimson')
plt.loglog(N,np.array(L[3])**4,'--',color='mediumpurple')

ejex=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
ejey=[0.0001,0.001,0.01,0.1,1,10,60,600]
ejey_labels=['0.1 ms','1 ms','10 ms','0.1 s','1 s','10 s','1 min','10 min']
plt.xticks(ejex,[])
plt.yticks(ejey,ejey_labels)
plt.ylabel('Tiempo de ensamblado')
plt.tight_layout()
plt.ylim(0.00001,600)
plt.title(titulo)

plt.subplot(2,1,2)

plt.hlines(dts2[13],0,16000,colors='b',linestyle='--', color='dodgerblue', label = 'Constante')#cambiar numero por matmul +1 y 16000

exp = [1,0.5,1/3,0.25]
data = dts2[13]#cambiar numero por matmul +1
L = []

for i in exp:
    data = data**i
    datos = []
    for i in range(14): #cambiar numero por matmul +1
        datos.append(data)
        data = data/2
    datos.sort()
    L.append(datos)
    data = dts2[13]#cambiar numero por matmul +1

plt.loglog(N,np.array(L[0]),linestyle='--',color='darkorange', label = '$O(N)$')
plt.loglog(N,np.array(L[1])**2,linestyle='--',color='limegreen', label = '$O(N{})$'.format(unicode_exp(2)))
plt.loglog(N,np.array(L[2])**3,linestyle='--',color='crimson', label = '$O(N{})$'.format(unicode_exp(3)))
plt.loglog(N,np.array(L[3])**4,linestyle='--',color='mediumpurple', label = '$O(N{})$'.format(unicode_exp(4)))

plt.legend(loc=2)

plt.xticks(ejex,ejex,rotation=45)
plt.yticks(ejey,ejey_labels)
plt.ylabel('Tiempo de solucion')
plt.xlabel('Tamaño de $N$')
plt.tight_layout()
plt.ylim(0.00001,600)

plt.savefig(f'{imagen}.png')
plt.show()