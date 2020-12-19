#!/usr/bin/python3

"""
Un almacén de ventas de productos por catálogos 
dispone de n vendedores asignados
 mensualmente de forma aleatoria a 4 regiones.ventascatalogo

El gerente de ventas mensualmente registra 
los montos de las ventas por cada vendedor
para luego determinar el total de ventas en dólares por región.

Elabore un algoritmo, para un mes cualquiera, que permita ingresar
los datos requeridos, asigne aleatoriamente el vendedor a una región,
finalmente determine y muestre la información solicitada por el gerente 
de ventas.



Ejemplo: n=7
vendedor	región[vendedor]	monto[vendedor]
1	            3	                50
2	            2	                70
3           	1	                90
4           	1	                20
5           	2	                10
6           	3	                80
7           	3	                40

Total Región 1: 110
Total Región 2: 80
Total Región 3: 170
Total Región 4: 0
 
"""


import random

def ventasRegion(region_monto):
    region_1 = list()
    region_2 = list()
    region_3 = list()
    region_4 = list()
    for i,x in  region_monto:
        if i == 1:
            region_1.append(x)
        if i == 2:
            region_2.append(x)
        if i == 3:
            region_3.append(x)
        if i == 4:
            region_4.append(x)
    print(f"Total region 1:{sum(region_1)}")
    print(f"Total region 2:{sum(region_2)}")
    print(f"Total region 3:{sum(region_3)}")
    print(f"Total region 4:{sum(region_4)}")

def main():
    n = int(input("ingrese un numero:"))
    region_monto = list()
    for i in range(1,n+1):
        monto = int(input(f"ingrese monto vendor {i}:"))
        region_monto.append([random.randint(1,4),monto])
    resultado = ventasRegion(region_monto)

if __name__ == '__main__':
    main()