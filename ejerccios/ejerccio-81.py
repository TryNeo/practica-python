#!/usr/bin/env python


"""
En el control de INVENTARIO DE PRODUCTOS 
que se lleva en una bodega, se tiene un modelo donde se
 determina la cantidad máxima y mínima de stock por producto.

Considerando el siguiente modelo:


Escriba un ALGORITMO que permita:

a) Registrar los datos de Consumo Máximo (Cmax), Consumo Mínimo (Cmin), Existencia actual (E) y Tiempo de reposición (Tr) de inventario para un listado de Nproductos.
b) Luego aplicando el modelo mostrado, determine la Cantidad de Pedido (CP) para cada producto.
c) Muestre aquellos productos donde la cantidad de pedido (CP) supere en un 70% la existencia actual.


"""
import random


def inventarioEspol(productos):
    tr = random.randint(1,30)
    listado_productos = [x for i,x in productos.items()]
    cmax = max(listado_productos)
    cmin = min(listado_productos)
    emin = cmin*tr
    emax = (cmax*tr)+emin
    for i,e in productos.items():
        cp = emax - e
        print(f'Producto:{i}\ncantidad de pedido:{cp}')
        if cp >= int(round(70*e/100,2)):
            print(f'{i}')


def main():
    productos = {
        'lacteos':random.randint(0,10),
        'carnes':random.randint(0,10),
        'dulces':random.randint(0,10),
        'manzanas':random.randint(0,10),
        'peras':random.randint(0,10),
        'mangos':random.randint(0,10),
        'juguetes':random.randint(0,10),
    }
    inventarioEspol(productos)
    

if __name__ == "__main__":
    main()
    