from numpy import matrix
from matplotlib import pyplot as plt

names = ['A_invB_inv.txt', 'A_invB_npSolve.txt']

def plotting(names):
    
    plt.figure()
    
    for name in names:
        data = np.loadtxt(name)
        Ns = data[:,0]
        dts = data[:,1] 
        
        plt.loglog(Ns,dts, '-o', label=name)
    
        ejex=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
        ejey=[0.0001,0.001,0.01,0.1,1,10,60,600]
        ejey_labels=['0.1 ms','1 ms','10 ms','0.1 s','1 s','10 s','1 min','10 min']
        plt.xticks(ejex,ejex,rotation=45) #tamanos de matriz
        plt.yticks(ejey,ejey_labels) #tiempo en segundos
        plt.ylabel('Tiempo transcurrido')
        plt.grid()
        
    plt.tight_layout()
    plt.legend()
    plt.savefig('Entrega_5.jpg')
    plt.show()
    
plotting(names)