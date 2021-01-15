#!/usr/bin/python3

"""
 Para miles de ciudadanos uruguayos la clasificación de su selección a semifinales en el mundial de fútbol 2010 representó una alegría doble, pues la empresa que les vendió sus televisores les devolverá la mitad del valor de la compra, como había prometido si su equipo llegaba a semifinales.

Realice un algoritmo para la empresa que reciba para n modelos de televisores: la cantidad vendida y el precio; para luego calcular el valor total y por tipo que tiene que devolver a sus clientes para cumplir con lo prometido.

Ejemplo:
Modelo	Cantidad	Precio	Devolver
LCD	250	400	50.000
Plasma	120	1000	60.000
LED	80	3000	120.000
…	…	…	…
Total a Devolver: 230.000

"""    
def bonoUruguay(cantidad,precio):
    return round(cantidad*precio/2,2)

def main():
    n = int(input("¿Cuantos modelos ingresara?:"))
    bono = list()
    for i in range(1,n+1):
        modelo = input(f"Modelo {i}:")
        cantidad = float(input("Cantidad:"))
        precio = float(input("precio:"))
        total = bonoUruguay(cantidad,precio)
        bono.append([modelo,cantidad,precio,total])
        
    print(f"Total a devolver:{sum(list(y for i,j,z,y in bono))}")
        
if __name__ == "__main__":
    main()