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
  + Caso 3: scipy.linalg.inv con overwrite_a=True
    + En este caso en particular se observó un porcentaje de ~90% por parte de los procesadores, atribuible a overwrite_a=True ya que en el caso 2 esto no sucedía.
    + Se podría concluir que este es el caso más eficiente, en donde más porcentaje de los procesadores es ocupado y donde el tiempo de ejecución es menor.
    + En los gráficos se puede ver, no tan claro debido a que la diferencia en segundos es mínima, que el caso 3 es el óptimo. Considerando lo anterior, en caso de necesitar realizar operaciones que requieran más tiempo y memoria, obviamente el caso 3 sería el preferible para utilizar.
    + En la siguiente captura se puede observar el desempeño en el caso 3 half.
    <img width="1440" alt="Captura de Pantalla 2020-08-11 a la(s) 11 24 53" src="https://user-images.githubusercontent.com/69161061/90038016-e398cf80-dc92-11ea-8222-3d6a44530e28.png">


+ ¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)?
  + numpy.linalg.inv:
  + scipy.linalg.inv:
  
+ ¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? (Ver clase 10 Agosto)

