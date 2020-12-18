#!/usr/bin/env python


import random
import time
from os import system, name 

"""
 “Carreras” es un juego de tablero para dos jugadores. En cada turno el 
 jugador lanza dos dados y se usan los números obtenidos en las caras superiores.
 
Para iniciar el juego, el jugador debe obtener las mismas caras de los dados en el lanzamiento.
Para avanzar casillas, se usa la suma de las caras de los dados, con el objetivo de llegar a la casilla final del tablero numeradas desde 1 al 50.
Existen casillas de premio (2, 17, 30, 42), en donde el jugador gana un lanzamiento adicional.

Elabore un ALGORITMO que simule este juego y muestre cuál jugador ganó.
"""

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

def dados(tablero_1):
    dado_1 = random.randint(1,6)
    dado_2 = random.randint(1,6)
    tablero_1+=(dado_1+dado_2)
    if tablero_1 == 2 or tablero_1 == 17 or tablero_1 == 30 or tablero_1 == 42:
        press_enter = input("tiro adicional - dale enter")
        if press_enter == "":
            dado_1 = random.randint(1,6)
            dado_2 = random.randint(1,6)
            tablero_1+=(dado_1+dado_2)
    return tablero_1


def carreras(jugador_1,jugador_2):
    print(f"\t {jugador_1} Lanza los Dados para comenzar")
    press_enter = input("presiona enter")
    if press_enter == "":
            dado_1 = random.randint(1,6)
            dado_2 = random.randint(1,6)
            if dado_1== dado_2:
                tablero_1 = 0
                tablero_2 = 0
                clear()
                print("\t Juego Inicia llega a la meta | casilla 50")
                while tablero_1 < 50 or tablero_2 < 50:
                    print("\tJugador 1 tira")
                    press_enter = input("presiona 1:")
                    if press_enter == "1":
                        tablero_1 = dados(tablero_1)
                        print(f"Avanza {tablero_1}")
                        if tablero_1 > 50:
                            print(f"Jugador {jugador_1} Gano")
                            break
                       time.sleep(2)
                        clear()
                    
                    print("\tJugador 2 tira")                                                
                    press_enter = input("presiona 2:")
                    if press_enter == "2":
                        tablero_2 = dados(tablero_2)
                        print(f"Avanza {tablero_2}")
                        if tablero_2 > 50:
                            print(f"Jugador {jugador_2} Gano")
                            break
                        time.sleep(2)
                        clear()
            else:
                print("Vuelve a Intentarlo")
    else:
        print("Ops Error")

def main():
    jugador_2 = random.randint(0,6) == random.randint(0,6)
    print("\tCarreras  | Juego del Año")
    print("\tJugador 1 | Jugador 2")
    print("")
    jugador_1 = input("ingrese nombre jugador 1:")
    jugador_2 = input("ingrese nombre jugador 2:") 
    if jugador_2 == "" or jugador_1 == "":
        jugador_1 = "BOT_1"
        jugador_2 = "BOT_2"
        carreras(jugador_1,jugador_2)
    else:
        carreras(jugador_1,jugador_2)



if __name__ == "__main__":
    main()