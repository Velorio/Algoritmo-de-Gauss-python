# Gauss con intercambio de filas

Este programa resuelve sistemas de ecuaciones lineales utilizando el método de eliminación gaussiana.

# Uso del programa

1. Ejecuta el programa gauss.py

2. **Ingresa las ecuaciones lineales:** El programa solicitará ingresar ecuaciones lineales en el formato estándar. Por ejemplo: **-3x+y+z=-2**. También se admite **-3x1+x2+x3=-2**. **Las variables del sistema deben ser consistentes**

3. **Finalización del ingreso de ecuaciones:** Una vez que hayas ingresado todas las ecuaciones que conforman el sistema, responde  **n** cuando el programa pregunte "Quiere ingresar otra ecuación? (s/n):".

4. **Visualización de la solución:** El programa mostrará la solución del sistema de ecuaciones, si es que existe, o indicará si el sistema es incompatible.

# Ejemplo de uso

``` Ingrese una ecuación lineal: -3x+y+z=-2
Ingrese una ecuación lineal: -3x+y+z=-2
{'coeficientes': [-3, 1, 1], 'variables': ['x', 'y', 'z'], 'termino_independiente': '-2'}
Quiere ingresar otra ecuación? (s/n): s
Ingrese una ecuación lineal: -6x+2y+2z+2w=-4
{'coeficientes': [-6, 2, 2, 2], 'variables': ['x', 'y', 'z', 'w'], 'termino_independiente': '-4'}
Quiere ingresar otra ecuación? (s/n): s
Ingrese una ecuación lineal: 3x+3y+2z-w=7
{'coeficientes': [3, 3, 2, -1], 'variables': ['x', 'y', 'z', 'w'], 'termino_independiente': '7'}
Quiere ingresar otra ecuación? (s/n): s
Ingrese una ecuación lineal: 3x+7y+2z=15
{'coeficientes': [3, 7, 2, 0], 'variables': ['x', 'y', 'z', 'w'], 'termino_independiente': '15'}
Quiere ingresar otra ecuación? (s/n): n

Hay igual cantidad de ecuaciones y variables
[[-3  1  1  0]
 [-6  2  2  2]
 [ 3  3  2 -1]
 [ 3  7  2  0]]
la determinante del sistema es:  72.0

Iteración 1

--> [-3, 1, 1, 0]  = -2.0
    [-6, 2, 2, 2]  = -4.0
    [3, 3, 2, -1]  = 7.0
    [3, 7, 2, 0]  = 15.0

...

Iteración 4

    [-3, 1, 1, 0]  = -2.0
    [0.0, 4.0, 3.0, -1.0]  = 5.0
    [0.0, 0.0, -3.0, 2.0]  = 3.0
--> [0.0, 0.0, 0.0, 2.0]  = 0.0

Solución:
x  =  1.0
y  =  2.0
z  =  -1.0
w  =  0.0

```

