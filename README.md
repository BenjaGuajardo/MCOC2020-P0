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
  + En mi caso, sólo grafiqué hasta N=500, debido al tiempo que tomaba utilizando mayores N (tiempos sobre los 2 minutos).
+ Diferencias con MATMUL.
  + Diferencias en el desempeño se deben a la función mimatmul. Al estar multiplicando mediante MIMATMUL, el proceso se hace mucho mas lento...
  + Diferencias en el desempeño se deben a la función mimatmul. Al estar multiplicando mediante MIMATMUL, el proceso se hace mucho mas lento...
  + Como se puede observar en el gráfico, el comportamiento es más lineal ya que al estarse usando "mimatmul", el cálculo es mucho más lento y se rpodría decir que el computador hace un menor esfuerzo.
+ Uso de procesadores
<img width="1440" alt="Captura de Pantalla 2020-08-10 a la(s) 11 30 07" src="https://user-images.githubusercontent.com/69161061/89800628-0a250200-dafd-11ea-9b02-0fe516c36c82.png">

  + En este caso, el programa utiliza un menor porcentaje debido a MIMATMUl. Como se puede ver en el desempeño MATMUL, se utilizan la totalidad de procesadores. Al implementar MIMATMUL, ya no se utilizan todos debido a...
