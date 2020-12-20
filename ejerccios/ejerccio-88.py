#!/bin/python

"""
os motores de cohete sólido constan de tres etapas.

coheteEspacial

Una vez que la primera etapa se quema, se separa del cohete y la segunda etapa se enciende.

Luego, la segunda etapa se quema y separa, y la tercera etapa se enciende. Finalmente, una vez que la tercera etapa se quema, también se separa del cohete.

Suponga que los datos mostrados en la figura representan aproximadamente los tiempos durante los que cada etapa se quema.

Elabore un algoritmo para:
a) Generar m=100 números aleatorios entre 0 y 260, los cuales representarán la cantidad de tiempo transcurridos en segundos, medidos luego de haber sido lanzado un cohete.
b) Determinar cuál es la etapa de vuelo para cada tiempo y cuál es la más repetida.
"""

import random



def main():
    m = 100
    count_1 = 0
    count_2 = 0
    count_3 = 0
    etapas_cohete = list()
    for i in range(1,m+1):
        tiempo = random.randint(0,260)
        if tiempo > 0 and tiempo < 100:
            etapas_cohete.append([i,tiempo,1])
        if tiempo > 100 and tiempo < 170:
            etapas_cohete.append([i,tiempo,2])
        if tiempo >170 and tiempo < 260:
            etapas_cohete.append([i,tiempo,3])

    print(f"k","Tiempo[k]","etapa[k]")    
    for i,x,j in etapas_cohete:
        if j == 3:
            count_3+=1
        if j == 2:
            count_2+=1
        if j == 1:
            count_1+=1
        print(i,x,j)

    if count_1 > count_2 and count_1 > count_3:
        print(f"Etapa 1 mas repetida :{count_1} ")
    elif count_2 > count_1 and count_2 > count_3:
        print(f"Etapa 2 mas repetida:{count_2}")
    elif count_3 > count_1 and count_3 > count_2:
        print(f"Etapa 3 mas repetida:{count_3}")
    
if __name__ == "__main__":
    main()