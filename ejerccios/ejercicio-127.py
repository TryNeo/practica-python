#!/usr/bin/python3
""" 
Define una función que nos permita conocer si una lista posee, o no elementos duplicados. La función debe cumplir con los siguientes requerimientos.

La función debe tener por nombre _items_duplicados_.
Al función debe recibir como argumento una lista de números enteros.
La función debe mostrar en consola todos los números duplicados y la cantidad de veces que se repiten en la lista.
Ejemplo.

>>> items_duplicate([1, 2, 3, 4, 5, 5])
El número 5 se encuentra repetido 2 veces

>>> items_duplicate([10, 10, 20, 30, 10, 10, 20, 50, 60, 10, 20])
El número 10 se encuentra repetido 5 veces
El número 20 se encuentra repetido 3 veces
"""

def items_duplicate(lista : list):
    duplicados  = {i:lista.count(i) for i in lista if lista.count(i) > 1}
    for key,value in duplicados.items():
        print(f"El número {key} se encuentra repetido {value} veces")
        
if __name__ == "__main__":
    items_duplicate([1, 2, 3, 4, 5, 5])
    items_duplicate([10, 10, 20, 30, 10, 10, 20, 50, 60, 10, 20])