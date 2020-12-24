#!/usr/bin/python3

import random

"""
El programa “Conoce Guayaquil” le ayudará a escoger una opción para recorrer los principales atractivos turísticos de la ciudad durante un día.

Hay 8 actividades disponibles, pero solo es posible realizar 4 de ellas durante el día.


Código	Actividad	Tiempo requerido en horas	Costo en $
1	Malecón 2000	2	6.50
2	Las Peñas	3	6
3	BarcoPirata Morgan	2	12.25
4	Recorrido Panorámico	2	12
5	Museos	3	10
6	Parque Histórico	4	10
7	Mall del Sol	3	6
8	IMAX	3	8.15


Para iniciar el programa se debe especificar una colección de listas llamada catalogo, que contenga la información de cada actividad: nombre, tiempo y costo.

Luego, el programadebe seleccionar aleatoriamente 4 actividades para formar un tour, que es una lista con los códigos de 4 actividades diferentes a realizarse.

El tour debe satisfacer las siguientes especificaciones:

El recorrido deberá empezar exactamente a las 10:00
El tiempo total no debe ser mayor a 12 horas
La visita al Parque Histórico debe iniciarse máximo a las 14:00 porque cierran a las 18:00
El recorrido por el Río Guayas en el Pirata Morgan debe iniciarse a partir de las 14:00
La función de cine en el IMAX puede ser a las 12:00, 15:00 ó 18:00
Al museo se puede entrar hasta las 18:00
Las demás actividades pueden realizarse en cualquier horario

Se requiere implementar:

La función generarCatalogo() que llena una lista con el nombre, tiempo y costo de todas las actividades disponibles, y la retorna.
La función generarTour() que llena una lista con 4 números aleatorios diferentes entre 1 y 8, correspondientes a las actividades a realizarse.
La función duracionActividad() que recibe el catalogo y el código que se desea consultar, devolviendo la duración de la actividad a la que pertenece el código dado.
La función inicioActividad() que recibe el código de la actividad y la hora actual (en formato hh) y devuelva la hora de inicio más cercana para la actividad especificada. Si dado el código y la horaactual no es posible iniciar la actividad requerida,retorne -1.
La función verificarTour() que recibe el catálogo y el tour generado y determina si es posible realizar esa combinación de actividadesde acuerdo a las condiciones explicadas arriba.
La función calcularCostoTotal() que recibe el catálogo y el tour generado, y devuelve el costo total de las actividades a realizar.
La función calcularTiempoTotal() que recibe el catálogo, el tour generado y devuelve la cantidad de horas utilizadas para las 4 actividades.
Un programa que use las funciones implementadas anteriormente para:
a. Generar el catálogo
b. Generar un tour válido
c. Mostrarpor pantalla el tour generado: sus actividades, horarios, tiempo total de recorrido y costo total, por ejemplo:
10:00 Visita a Museos
14:00 Río Guayas en el Pirata Morgan
16:00 Recorrido Panorámico
18:00 Compras en Mall del Sol

El tour comenzaráa las 10:00 horas y 
terminará a las 21:00 horas.
Tiempo total de recorrido: 11 horas
Costo total: $ 40.25
"""

def generarCatalogo():
    return [
        [1,'Malecon 2000',*[str(i)+":00" for i in [random.randint(10,21)]],6.50],
        [2,'Las Peñas',*[str(i)+":00" for i in [random.randint(10,21)]],6],
        [3,'Barco Pirata',*[str(i)+":00" for i in [random.randint(10,21)]],12.25],
        [4,'Recorrido Panoramico',*[str(i)+":00" for i in [random.randint(10,22)]],12],
        [5,'Museos',*[str(i)+":00" for i in [random.randint(10,18)]],12],
        [6,'Parque Historico',*[str(i)+":00" for i in [random.randint(10,21)]],10],
        [7,'Mall del Sol',*[str(i)+":00" for i in [random.randint(10,21)]],6],
        [8,'IMAX',*[str(i)+":00" for i in [random.randint(10,21)]],8.15],
        
    ]

def generarTour():
    return [random.randint(1,8) for i in range(1,4+1)]


def duracionActividad(catalogo,codigo):
    duracion_actividad = [[i[0],i[1],i[2],i[3]] for i in catalogo]
    return [[i[0],i[1],i[2],i[3]] for i in duracion_actividad for j in codigo if i[0] == j]

def inicioActividad(duracion):
    if duracion == []:
        return -1
    else:
        return sorted([ [i[2],i[1]] for i in duracion])
    

def calcularCostoTotal(duracion):
    return sum([ i[3] for i in duracion])

def main():
    catalogo = generarCatalogo()
    codigo = generarTour()
    duracion = duracionActividad(catalogo,codigo)
    inicio = inicioActividad(duracion)
    costoTotal = calcularCostoTotal(duracion)
    for i in inicio:
        print(*i)
    print()
    print(f"El tour comenzara las 10:00 horas y terminará a las 21:00 horas.")
    print(f"Costo total: ${costoTotal}")

if __name__ == "__main__":
    main()
