#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

def icosaedros(value):



  nbr_1 = int(random.random()*5)+1
  nbr_2 = int(random.random()*5)+1
  
  cr_1 = int(random.random()*4)+1
  cr_2 = int(random.random()*4)+1

  lanzados, premio = 0, 0
  op = int()
  while op!=3:

    op = int(input("Presione 2 para lanzar, 3 para salir:"))
    if op == 2:
      if cr_1 == cr_2:
        print(f"Icosaedro 1: {nbr_1} \nIcosaedro 2: {nbr_2}")
        premio = premio +10
        print(f"Jugador GANO 10 centavos")

      if nbr_1 == nbr_2:
        print(f"Icosaedro 1: {nbr_1} \nIcosaedro 2: {nbr_2}")
        premio = premio +10
        print(f" Jugador GANO 10 centavos")

      if nbr_1 == nbr_2 and cr_1 == cr_2:
        print(f"Icosaedro 1: {nbr_1} \nIcosaedro 2: {nbr_2}")
        premio = premio +50
        print(f" Jugador GANO 50 centavos")
     
      suma = nbr_1 + nbr_2
      if suma %2 == 0:
        premio = premio + 5

      lanzados+=1
    elif op!=2:
      print(f"El jugador GANO {premio} centavos en {lanzados} Lanzamientos")
      break



def main():
  print("\tEjerccio 51")
  print()
  print("A continuación se muestra una ejecución en pantalla del algoritmo que se debe construir:")
  print()

  iniciar = int(input("Presione 1 para iniciar el juego:"))

  juego = icosaedros(iniciar)
  return juego


if __name__ == '__main__':
  main()