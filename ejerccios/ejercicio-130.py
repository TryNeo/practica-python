#!/usr/bin/python3
import random
    """
    Dada una matriz de n x n.

# Ejemplo matriz 3 x 4

matriz = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 200, 300],
]
Desarrolla un script el cumpla con los siguientes requerimientos.

Mostrar en consola la suma de cada una de las columnas de la matriz.
Mostrar en consola la suma de cada una de las filas de la matriz.
Los resultados deben estar separados mediante un guión (-)
El script debe funcionar para cualquier matriz (n x n).
Ejemplo.

La suma de las columnas es: 150 - 180 - 300 - 420
La suma de las filas es: 100 - 260 - 690
Ayuda:

Si así lo deseas puedes definir la matriz directamente desde el script.
Puedes almacenar los resultados dentro de listas.
La mejor forma de convertir una lista a un string es mediante el método join.

    """

aleatorios = [i for i in range(random.randint(0,100))]


def crear_matriz(fila,columna):
    matriz = []
    for i in range(fila):
        matriz.append(random.sample(aleatorios, columna))
    return matriz


if __name__ == "__main__":
    matriz = crear_matriz(3,4)
    filas = len(matriz)
    columnas = len(matriz[0])
    fila = [str(sum(matriz[i])) for i in range(filas)]
    columna = [ str(sum(fila[i] for fila in matriz)) for i in range(columnas)]
    print("La suma de las filas es:"," - ".join(fila))
    print("La suma de las columnas es:"," - ".join(columna))