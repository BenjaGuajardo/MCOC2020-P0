from matplotlib import pyplot as plt
import numpy as np

def unicode_exp(exp):
    if exp == 1:
       return chr(0xB9)
    if exp == 2 or exp == 3:
       return chr(0xB0 + exp)
    else:
       return chr(0x2070 + exp)

imagen = 'matmul_matriz_dispersa'
titulo = 'MATAMUL MATRIZ DISPERSA'
names = ['matmul_matriz_dispersa_0.txt',
         'matmul_matriz_dispersa_1.txt',
         'matmul_matriz_dispersa_2.txt',
         'matmul_matriz_dispersa_3.txt']

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
    
a1 = dts1[13]/(16000)#13 Y 16000 para los otros casos
a2 = dts1[13]/(16000**2)#13 Y 16000 para los otros casos
a3 = dts1[13]/(16000**3)#13 Y 16000 para los otros casos
a4 = dts1[13]/(16000**4)#13 Y 16000 para los otros casos

plt.loglog(N,a1*N,'--',color='darkorange')
plt.loglog(N,a2*N**2,'--',color='limegreen')
plt.loglog(N,a3*N**3,'--',color='crimson')
plt.loglog(N,a4*N**4,'--',color='mediumpurple')

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

plt.hlines(dts2[12],0,8000,colors='b',linestyle='--', color='dodgerblue', label = 'Constante')#cambiar numero por matmul +1 y 16000

b1 = dts2[13]/(16000)#13 Y 16000 para los otros casos
b2 = dts2[13]/(16000**2)#13 Y 16000 para los otros casos
b3 = dts2[13]/(16000**3)#13 Y 16000 para los otros casos
b4 = dts2[13]/(16000**4)#13 Y 16000 para los otros casos

plt.loglog(N,b1*N,linestyle='--',color='darkorange', label = '$O(N)$')
plt.loglog(N,b2*N**2,linestyle='--',color='limegreen', label = '$O(N{})$'.format(unicode_exp(2)))
plt.loglog(N,b3*N**3,linestyle='--',color='crimson', label = '$O(N{})$'.format(unicode_exp(3)))
plt.loglog(N,b4*N**4,linestyle='--',color='mediumpurple', label = '$O(N{})$'.format(unicode_exp(4)))

plt.legend(loc=2)

plt.xticks(ejex,ejex,rotation=45)
plt.yticks(ejey,ejey_labels)
plt.ylabel('Tiempo de solucion')
plt.xlabel('Tamaño de $N$')
plt.tight_layout()
plt.ylim(0.00001,600)

plt.savefig(f'{imagen}.png')
plt.show()