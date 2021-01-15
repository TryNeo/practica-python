#!/usr/bin/python3

"""
Diez perros se encuentran participando en una carrera, el recorrido que
 deben realizar es de un total de 100 metros con obstáculos, bajo las siguientes reglas:carreraperros

Todos avanzan al mismo tiempo.
Cada perro realiza aleatoriamente una de las 4 acciones siguientes:
salta 1 metro, o derribando o sorteando apropiadamente el obstáculo,
salta 2 metros, o derribando o sorteando apropiadamente el obstáculo.
Cuando el perro derriba un obstáculo, usted debe considerar que no puede avanzar 
en el siguiente instante de tiempo, porque tiene que recuperarse para el siguiente salto.
Elabore un programa que simule el recorrido de los perros y muestre:

a) El avance de los perros en la carrera, en cada instante de tiempo, hasta que terminó.
b) El perro que ganó la carrera y la cantidad de saltos que necesitó para lograrlo (suponga que fue un solo perro).
"""

import random


def carreraPerros(perros,acciones):
    metros = 0
    salto = 0
    no_salto = 0
    derribado = 0
    saltos = [1,2,3,4,5, 6, 7, 8,9,10]
    while metros < 100:
        for i in perros:
            ra = str(random.randint(1,10))
            if i == 'perro_'+ra:
                for key,value in acciones.items():
                    if key == random.randint(1,2):
                        if random.choice(value) == 'sorteando':
                            salto += 1
                            saltos[random.randint(0,9)] = salto
                            metros+=1
                            print(f"perro_{ra} | salto:{salto} | {key} metro - {value[1]}")

                        if random.choice(value) == 'derribado':
                            no_salto = saltos[random.randint(0,9)] - salto
                            saltos[random.randint(0,9)] = no_salto
                            metros+=1
                            derribado+=1
                            print(f"perro_{ra}  | salto:{salto} | {key} metro- {value[0]} {derribado}")
    print()
    print("Perros - Saltos Totales")
    for i,x in enumerate(saltos,1):
        print(f"{i}.{x} ")

    print(f"Perro con mayor salto {max(saltos)} derribos {derribado} ")

def main():
    perros = ['perro_'+str(i) for i in range(1,10+1)]
    acciones = {
        1:[
            'derribado',
            'sorteando',
        ],
        2:[
            'derribado',
            'sorteando',
        ]
    }
    carreraPerros(perros,acciones)
    
    
if __name__ == "__main__":
    main()