#!/bin/venv python


import logging
import threading
import random
from random import sample

"""
Se tiene una lista de códigos de 25 personas de género
masculino numerados del 1 al 25 y otra lista de códigos de
25 personas
de género femenino numerados del 26 al 50.tenisjuego

a) Escriba un algoritmo para sortear parejas 
mixtas de tenis, tal que a cada persona de género 
masculino le asigne aleatoriamente una persona de 
género femenino. Muestre las parejas resultantes.
"""

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(message)s'
)

def main():
    masculino = [i for i in range(1,25+1)]
    femenino  = [i for i in range(26,50+1)]
    sorteo = []
    for i in masculino:
        sorteo.append([i,random.choice(femenino)])
 
    count=0
    print("Sorteo Mixto de Tenis [Hombres,Mujeres]")
    for i in sorteo:
        count=count+1
        print(f'Sorteo {count} : {i}')
    
            



if __name__ == '__main__':
    thread = threading.Thread(target=main)
    thread.start()