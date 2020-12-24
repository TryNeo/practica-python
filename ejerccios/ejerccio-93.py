#!/usr/bin/python3

import random
"""
Generar una lista de 50 números aleatorios.

Dada la lista, mostrar en pantalla todos los números pares mayores a 50.
"""

def main():
    return [i for i in [random.randint(1,100) for i in range(1,50)] if i >= 50 if i%2==0]
    
if __name__ == "__main__":
    print(main())