# MCOC2020-P0
## Mi Computador

+ Marca/modelo: Apple/MacBook Pro (13-inch, 2017, Two Thunderbolt 3 ports)

+ Tipo: Notebook

+ Año adquisición: 2019

+ Procesador
  + Marca/Modelo: Intel Core i5
  + Velocidad Base: 2,3 GHz
  + Velocidad Máxima: 3,6 GHz
  + Numero de núcleos: 2
  + Numero de núcles lógicos: 4

+ Memoria

  + Total: 8 GB
  + Tipo memoria: LPDDR3
  + Velocidad 2133 MHz

+ Gráficas
  + Intel Iris Plus Graphics 640
+ Disco
  + Tipo: SSD
  + Tamaño: 256 GB
  + Particiones: 2

+ Dirección MAC de la tarjeta wifi: 38:f9:d3:48:d4:09

+ Dirección IP Interna: 192.168.1.103

+ Dirección IP Externa: 181.43.73.95
 
+ Proveedor internet: Entel Chile S.A.

## Desempeño MATMUL

![timing_matmul](https://user-images.githubusercontent.com/69161061/89593349-ef147280-d81c-11ea-9cca-c903c8dc7210.png)

+ ¿Como difiere del gráfico del profesor/ayudante?
  + El primer calculo de 'C', cuando N = 3, en mi caso demora aproximadamente 1 s, mientras que en el caso del profesor demora menos de 0.1 ms.
  + Al teminar, N = 10000, mi grafico se acerca mas al minuto, mientras que en el ejemplo del profesor esta mas cerca de los 10 s.
+ ¿A qué se pueden deber las diferencias?
  + Podría deberse a la cantidad de núcleos que tiene el procesador y la cantidad que se utilizan durante la ejecución del programa.
+ El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
  + El uso de memoria es lineal porque este depende solamente de las dimensiones de la matriz, por lo que a medida que aumenta, también lo hace la memoria.
  + El tiempo no es lineal ya que depende de la cantidad de procesadores que se estan usando, por ejemplo, inicialmente el tiempo comienza a disminuir debido a que se comienzan a utilizar más procesadores. Entonces, a esto se deben los picks del gráfico ya que va aumentando el uso de los procesadores. Finalmente, el tiempo tiene un comportamiento más lineal porque ya se están utilizando todos los núcleos disponibles.
+ ¿Qué versión de python está usando?
  + 3.7.3
+ ¿Qué versión de numpy está usando?
  + 1.16.4
+ Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar. 
  + Durante la ejecución se utilizan los 2 núcleos disponibles y los 4 núcleos lógicos del procesador (hilos), tal como se puede ver en la siguiente captura.
  <img width="1440" alt="Captura de Pantalla 2020-08-07 a la(s) 11 44 47" src="https://user-images.githubusercontent.com/69161061/89664055-91c40400-d8a4-11ea-8231-b9b517e88284.png">

## Desempeño MIMATMUL

![timing_mimatmul](https://user-images.githubusercontent.com/69161061/89792966-40f61a80-daf3-11ea-8de9-ab41c550cce7.png)

+ ¿Como difiere del gráfico del profesor/ayudante?

  + Los gráficos son bastante similares, tienen un crecimiento continuo a medida que aumenta N.
  + En mi caso, sólo grafiqué hasta N=500, debido al tiempo que demoraba utilizando mayores N (tiempos sobre los 2 minutos).
  
+ Diferencias con MATMUL.

  + Diferencias en el desempeño se deben a la función mimatmul. Al estar multiplicando mediante el código puro de python, el proceso se hace mucho mas lento porque se programó la multiplicación en un nivel alto (python). En adición a lo anterior, no operan todos los procesadores, lo cual implica una baja en el rendimiento.
  
  + Como se puede observar en el gráfico, el comportamiento es más lineal ya que al estarse usando "mimatmul", se trabaja solo con 2 núcleos lo cual hace todo el proceso más lento y sin picks.
  
+ Uso de procesadores

  + En este caso, el programa utiliza un menor porcentaje. Como se puede ver, no se utilizan la totalidad de procesadores y esta es una de las razones del por qué de la lentitud del programa. Comparando con el desempeño MIMATMUL, la forma de operar es óptima en ese caso ya que por ejemplo, numpy, está escrito en un nivel bajo.
  
<img width="1440" alt="Captura de Pantalla 2020-08-10 a la(s) 11 30 07" src="https://user-images.githubusercontent.com/69161061/89800628-0a250200-dafd-11ea-9b02-0fe516c36c82.png">

## Desempeño de INV

+ Tamaño en memoria de cada tipo de dato
  + np.half = 2 Bytes
  + np.single = 4 Bytes
  + np.double = 8 Bytes
  + np. londouble = 16 Bytes
+ Análisis de desempeño INV
  + Caso 1: numpy.linalg.inv
    + Para el primer caso, en cuanto a procesadores, durante la corrida del programa se pudo observar que 2 de los 4 núcleos estaban trabajando (siendo esto menos del 50%). 
    + En cuanto a memoria, se calculó que para el caso N = 10.000 en particular se utilizaban más o menos 3,8 GB lo cual equivalía a 4 matrices.
    + El desempeño es similar para el caso np.single y np.double. Para np.half y np.double, resultó que no eran compatibles con numpy.linalg.
    +  En el caso 1 se encuentra el rendimiento más bajo y menos óptimo, lo cual se evidencia en los tiempos de ejecución.
    
    ![Caso 1 np double](https://user-images.githubusercontent.com/69161061/90050504-48105a80-dca4-11ea-89e3-52cb9ff126ca.jpg) ![Caso 1 np single](https://user-images.githubusercontent.com/69161061/90050507-49418780-dca4-11ea-8eeb-c57ed51355cc.jpg)
  + Caso 2: scipy.linalg.inv con overwrite_a=False
    + El porcentaje en los procesadores fue ~55%, siendo este valor más alto que para en el caso 1, haciéndose uso de los 4 núcleos.
    + En cuanto a memoria, se calculó que para el caso N = 10.000 en particular se utilizaban más o menos 2,5 GB lo cual equivalía a 2 matrices.
    
    ![Caso 2 np double](https://user-images.githubusercontent.com/69161061/90050509-4a72b480-dca4-11ea-9216-edf4c820c676.jpg) ![Caso 2 np half](https://user-images.githubusercontent.com/69161061/90050510-4b0b4b00-dca4-11ea-80d4-e949283b7b73.jpg) ![Caso 2 np longdouble](https://user-images.githubusercontent.com/69161061/90050512-4ba3e180-dca4-11ea-8095-8546515e675c.jpg) ![Caso 2 np single](https://user-images.githubusercontent.com/69161061/90050514-4ba3e180-dca4-11ea-8aa2-3cc057173c64.jpg)
  + Caso 3: scipy.linalg.inv con overwrite_a=True
    + En este caso en particular se observó un porcentaje de ~90% por parte de los procesadores, atribuible a overwrite_a=True ya que en el caso 2 esto no sucedía.
    + Se podría concluir que este es el caso más eficiente, en donde más porcentaje de los procesadores es ocupado y donde el tiempo de ejecución es menor.
    + En los gráficos se puede ver, no tan claro debido a que la diferencia en segundos es mínima, que el caso 3 es el óptimo. Considerando lo anterior, en caso de necesitar realizar operaciones que requieran más tiempo y memoria, obviamente el caso 3 sería el preferible para utilizar.
    + En la siguiente captura se puede observar el desempeño en el caso 3 half.
    <img width="1440" alt="Captura de Pantalla 2020-08-11 a la(s) 11 24 53" src="https://user-images.githubusercontent.com/69161061/90038016-e398cf80-dc92-11ea-8222-3d6a44530e28.png">
    
    ![Caso 3 np double](https://user-images.githubusercontent.com/69161061/90050516-4c3c7800-dca4-11ea-92d5-8163f7c5fa07.jpg) ![Caso 3 np half](https://user-images.githubusercontent.com/69161061/90050519-4cd50e80-dca4-11ea-9d51-53a018b836f9.jpg) ![Caso 3 np longdouble](https://user-images.githubusercontent.com/69161061/90050521-4cd50e80-dca4-11ea-9bfb-644748cc71b3.jpg) ![Caso 3 np single](https://user-images.githubusercontent.com/69161061/90050523-4cd50e80-dca4-11ea-8933-6aef64ab8836.jpg)

+ Análisis de datos
  + Analizando brevemente el desempeño según el tipo de datos, el mejor se encuentra para np.half, donde los tiempos de ejecución son considerablemente más bajos, siendo aproximadamente 0,15 segundos, cuando N = 2000. Para los demás el tiempo aumenta y está dentro de un rango de 0,40 y 0,50 segundos, para el N = 2000.

+ ¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)?
  + numpy.linalg.inv: por lo visto, creo que podría utilizar Cholesky debido a que es un poco más lento que con scipy y necesita de más memoria.
  + scipy.linalg.inv: creo que podría utilizar Cailey-Hamilton, porque con la misma matriz 'A' se realizan las operaciones para el cálculo.
  
+ ¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? (Ver clase 10 Agosto)
  + En cuanto a los gráficos de desempeño el comportamiento de las curvas para los tres casos es bastante similar. Lo que sí se puede notar es que en el caso 2 es donde menos lineal es el comportamiento, existiendo un par de picks dentro del proceso.Viéndolo por la estructura de caché, pareciera ser que la memoria requerida para el segundo caso se alcanza más rápido y por eso se generan los picks, es decir, se comenzarían a ocupar los distintos niveles de caché antes que en los otros casos. Un punto de análisis sería ver por qué si en el caso 1 se ocupaba más memoria, entonces no tiene un comportamiento similar al visto en el caso 2. Probablemente el algoritmo o la función inv() de numpy se aleja más del bajo nivel y el desempeño no es óptimo, pero aún así no sabría decir realmente por qué si requiere de más memoria, entonces no presenta picks en los puntos en que se alcanza la memoria de los distintos niveles de caché. Algo tendrá relacionado el uso de los procesadores, ya que como mencioné en puntos anteriores, para el caso 1 es donde menor porcentaje se utilizó. El caso 3 es el que mejor comportamiento tiene y en esto podría estar más visible el paralelismo. Como se mostró anteriormente, para el caso 3 los 4 núcleos se encuentran trabajando, lo cual mejora mucho el desempeño del programa.

## Desempeño Ax = b

![Entrega_6](https://user-images.githubusercontent.com/69161061/90338054-e0645300-dfb4-11ea-8794-2aa200ed9495.png)

  + Para medir el desempeño se realizaron 5 corridas para distintos N (desde 2 a 10000), donde se midió el tiempo que demoraba cada solver.
  + Los solver utilizados para resolver el sistema A x = B son los siguientes:
    + A_invB_inv: Invierte A mediante inv() y luego calcula x.
    + npSolve: Solver de numpy.
    + spSolve: Solver de scipy que además presenta opciones para utilizar un solver específico.
      + spSolve_sym: Para matrices simétricas.
      + spSolve_pos: Para definidas positivas.
      + spsolve_pos_overwrite: Permite sobrescribir la matriz para una mejor performance.
+ Análisis
  + Inicialmente, para N = 2, se puede observar que el solver mas rapido es el de numpy, mientras que los otros metodos se encuentran relativamente cercanos en tiempo.
  + A medida que aumenta el N, entre N=10 y N=100, se puede notar que existen ciertos peaks. Lo anterior se puede asociar a que comienza a usarse un mayor porcentaje de  procesadores, lo cual explicaría las mejoras en el desempeño, disminuyendo los tiempos de ejecución.
  + Ya para los N más grandes, se puede notar de mejor manera cual es el solver más eficiente y rápido. Como era de esperarse, A_invB_inv es por lejos el más lento, ya que no se está utilizando un solver sino que se utiliza el método de la invertida. Para el resto de los solvers, se puede notar que npSolve no sigue siendo el más rápido, como en un comienzo, pero presenta un desempeño similar a spSolve. En cuanto a los solvers de scipy, el desempeño también es el esperado, spSolve es el más lento, y cuando especificamos que A es simétrica y definida positiva, el rendimiento mejora. Lo anterior era lo esperado ya que al agregar estas especificaciones se optimiza el calculo, por ejemplo, cuando se señalamos que A es simetrica, el solver toma los valores del triangulo superior puesto que la matriz es simetrica. El solver más rápido es pos_overwrite, ya que con esto mejoramos la performance al permitir sobrescribir la matriz A.

## Matrices dispersas y complejidad computacional

+ Complejidad algoritmica de MATMUL

![matmul_matriz_dispersa](https://user-images.githubusercontent.com/69161061/90911063-6bbf5900-e3a6-11ea-8830-baabb35babf5.png)![matmul_matriz_llena](https://user-images.githubusercontent.com/69161061/90911077-6f52e000-e3a6-11ea-974b-850558f104ec.png)
  
  + Ensamblado
    + Complejidad asintótica
      + Matriz llena = N2
      + Matriz dispersa = N2
    + El tiempo de ensamblado no varía notoriamente para cada caso, pero en los primeros N se puede notar una mayor estabilidad en el caso de las matrices dispersas. Para el caso "MATMUL" el N máximo fue 8000 debido a que con N = 16000 se superaba la memoria RAM. Otra observación es que el comportamiento asintótico que tienen ambas matrices con "O(N2)", lo cual significa que si aumentamos el N de la matriz, el ensamblaje demorará el cuadrado de tiempo.
    
  + Solución
      + Complejidad asintótica
        + Matriz llena = N
        + Matriz dispersa = N3
      + Para la solución, en matrices dispersas la multiplicacion es mas rápida y la diferencia es notoria. Lo anterior es porque cuando la matriz presenta una gran cantidad de ceros, como es el caso de las matrices lagrangianas, el tiempo de solución en matrices dispersas disminuye drásticamente en comparación al de una matriz llena, lo cual se debe a que al utilizar matrices dispersas, se evitan los cáclulos que involucran los ceros.
      + En cuanto al uso de memoria, las matrices dispersas permiten realizar cálculos con N mucho mayores gracias a que no ocupa la memoria en guardar la matriz NxN, como es el caso de las matrices llenas, por esto mismo es que en el caso de la matriz llena sólo pude realizar el cálculo hasta N = 8000.
      + El comportamiento asintótico N que tiene el caso disperso, refleja la complejidad del algoritmo que sólo multiplica los valores que no son 0, además gracias a esto  es posible realizar el cálculo en matrices de dimensiones mucho mayores. El caso de matriz llena, multiplica las matrices coeficiente por coeficiente, lo cual claramente requiere más memoria y tiempo, y esto se ve reflejado en la comlpejidad asintótica O(N3)
  
+ Complejidad algoritmica de INV

![inv_matriz_dispersa](https://user-images.githubusercontent.com/69161061/90800463-b8d9f700-e2e2-11ea-8307-faa3e37f9a2f.png)![inv_matriz_llena](https://user-images.githubusercontent.com/69161061/90800468-bbd4e780-e2e2-11ea-9a71-d2203f8e53c3.png)

  + Ensamblado
    + Complejidad asintótica
      + Matriz llena = N2
      + Matriz dispersa = N2
    + El tiempo de ensamblado es similar para ambos casos, la única diferencia que se puede notar es que el comportamiento asintótico ocurre primero en el caso de la matriz llena, es decir, para la matriz dispersa el tiempo de ensamblado es más bien lineal para los primeros valores de N, no así la matriz llena ya que su comportamiento es asintótico a O(N2) desde un principio.
    
  + Solución
      + Complejidad asintótica
        + Matriz llena = N3
        + Matriz dispersa = N3
      + Para la solución, en matrices dispersas el cálculo de la inversa es mas rápido. Además, la complejidad asintótica en matrices dispersas es más bien lineal hasta aproximadamente el N = 5000. Lo anterior significa que, a medida que duplicamos el tamaño de la matriz, el tiempo de solución se comporta de manera lineal, mientras que para las matrices llenas, el tiempo se cuadruplica.
      + Tambien se puede observar que las corridas son más estables en matrices dispersas y se parecen entre sí. En matrices llenas, en el rango N(2,100), las corridas son inestables y con muchas variaciones.
      + En cuanto a la complejidad, en dispersas se puede notar un comportamiento lineal durante la mayor parte de la corrida, que cercana al N = 5000 comienza a acercarse asintóticamente al O(N2). Lo anterior refleja que el caso de matrices dispersas tiene un mejor desempeño, y es básicamente porque al invertir matrices con tantos ceros, la matriz dispersa se evita todos esos cálculos innecesesarios que el caso de matriz llena sí realiza. Por el otro lado, la matriz llena se acerca a la complejidad N2 desde un principio, llegando finalmente a un tiempo final mucho mayor que en el caso de las dispersas.
      + Cabe destacar que para el cálculo de la inversa en matrices dispersas, se utilizó csc_matrix para un mejor desempeño.

+ Complejidad algoritmica de SOLVE

![solver_matriz_dispersa](https://user-images.githubusercontent.com/69161061/90800477-bd9eab00-e2e2-11ea-944a-36c01952daa5.png)![solver_matriz_llena](https://user-images.githubusercontent.com/69161061/90800479-becfd800-e2e2-11ea-9b07-2c2e906ccd42.png)

+ Ensamblado
  + Complejidad asintótica
    + Matriz llena = N2
    + Matriz dispersa = N2
  + El desempeño es prácticamente el mismo para ambos casos, tanto en complejidad asintótica, tiempo de ensamblado y estabilidad de las corridas. Existen pequeñas diferencias entre ambos casos para los primeros N en cuanto a estabilidad y tiempo, pero ya pasado el N = 50, el desempeño es similar.
    
+ Solución
  + Complejidad asintótica
    + Matriz llena = N
    + Matriz dispersa = N3
  + Inmediatamente se puede observar que el tiempo de solución es demasiado inferior para matrices dispersas (~10 ms para dispersas y ~1 min en llenas) en el caso mas extremo (N = 16000). Este resultado es esperable ya que al ser matrices lagrangianas, la cantidad de ceros que hay en las matrices es muy grande, y las matrices dispersas evitan todos los cálculos que involucran estos ceros.
  + Tambien se puede observar que las corridas son más estables en matrices dispersas y se parecen entre sí, mientras que las matrices llenas presentan inestabilidad en los N < 500.
  + En cuanto a la comlejidad, en dispersas se puede notar un comportamiento casi constante en la mayor parte de la corrida, tendiendo finalmente a una complejidad lineal. Lo anterior significa que el tiempo de solución, en gran parte de la corrida no se ve afectado por el tamaño de la matriz y que gracias a las matrices dispersas se podría continuar realizando sistemas con N mucho mayores, que en caso de matrices llenas, probablemente no serían factibles y sobrepasarían la memoria.
  + Cabe destacar que para el cálculo de la inversa en matrices dispersas, se utilizó csr_matrix para un mejor desempeño.

+ Conclusión
  + Parece ser que el ensamblado de las martices no depende del tipo de matriz, sino que es atribuible al código de ensamblaje.
  + En cuanto a las soluciones, claramente el tamaño de la matriz afecta el comportamiento en el caso de matriz llena, puesto que las corridas tienen una complejidad asintótica muy marcada desde un principio, a diferencia de las matrices dispersas, que por gran parte de la corrida tienen una complejidad de un orden menor, respecto de las matrices llenas, por lo que el tamaño de la matriz no afecta de gran manera y es posible hacer cálculos con Ns superiores, en menos tiempo.
  + Se pudo observar que en los casos 'MATMUL' y 'SOLVER', las diferencias son muy grandes entre matrices dispersas y llenas, pero en el caso 'INV' podría decirse que se parecen un poco más, aunque las dispersas siguen teniendo un mejor desempeño. Lo anterior se puede deber a que para invertit matrices, independiente de la cantidad de ceros, el algoritmo requiere más tiempo y presenta una mayor complejidad.
  + Finalmente, habiendo analizado los casos, es claro que el mejor desempeño se obtiene al utilizar matrices dispersas.

+ Matriz Laplaciana

  + El código de ensamblaje de matri laplaciana, para el caso de matriz llena y dispersa, es el siguiente:
```
from numpy import zeros,double
from scipy.sparse import lil_matrix, csr_matrix, csc_matrix

def matriz_laplaciana_llena(N):
    A = zeros((N,N),dtype=double)
    for i in range(N):
        for j in range(N):
            if i==j:
                A[i,j]=2
            if i+1==j:
                A[i,j]=-1
            if i-1==j:
                A[i,j]=-1       
    return A

def matriz_laplaciana_dispersa(N):
    A_lil = lil_matrix((N,N),dtype=double) 
    for i in range(N):
        for j in range(N):
            if i==j:
                A_lil[i,j]=2
            if i+1==j:
                A_lil[i,j]=-1
            if i-1==j:
                A_lil[i,j]=-1
    A = csr_matrix(A_lil)
    return A
```
  + Cómo se vio en clases, esta forma no es la con mejor desempeño ya que el tiempo de ensamblaje depende directamente de estas funciones. Para matrices llenas y dispersas los tiempos fueron similares y probablemente con otro código más eficiente, los tiempos se verían reducidos. El hecho de tener ciclos 'for' indentados y que se recorra toda la matriz para formarla, hace que el ensamblado sea más lento. Una opción sería ocupar la función eye() para así evitar recorrer completamente las matrices.
