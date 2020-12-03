"""
Desarrolla un generador que nos permita obtener todos lo números pares en un rango.

El generador debe cumplir con los siguientes requerimientos.

El generador debe tener por nombre pares.
El generador debe recibir como argumento n y m. Donde n >0 y n < m, así como m > 0 y m > n
El generador debe retornar todos los números pares que se encuentren entre n y m.
En caso alguno de los argumentos no cumplan con lo previamente indicado, la generador debe lanzar una excepción.
El mensaje de la excepción debe ser el siguiente: No es posible continuar con la operación.

Ejemplo.

>>> for numero in pares(5, 10):
    print(numero)
6
8
>>> for numero in pares(11, 18):
12
14
16
for numero in pares(0, -1):
Exception: No es posible continuar con la operación.
"""


def pares(n,m):
    lista = []
    if n > 0 and n <m and m > 0 and m > n:
        for i in range(n,m):
            if i%2 == 0:
                lista.append(i)
        return lista if lista else  "Exception: No es posible Continuar con la operacion"


def main():
    print("\tEjerccio 70")
    par = pares(100,200)
    print(par)

if __name__ == '__main__':
    main()