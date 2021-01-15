#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Una nave extraterrestre tiene una capacidad disponible de K Kg (K es una constante real de 150 Kg) y disponen de una lista del peso en Kg de n seres humanos diferentes.


RULES :
Ingresar en un arreglo los pesos de n personas.
Presentar todas las parejas tal que la suma de sus pesos sea menor que una constante K=150.
Presente también la suma mas grande encontrada.
"""
#constante de kg 150
K = 150

def mensaje(func):
  def mostrar():
    print("""\tEjerccio 53\n\nIngresa la cantidad de Humanos a entrar a la nave
    """)
    func()
  return mostrar

def nave(value):
  for i in value:
    i = i+i
    if i <= 150:
      print(f'Subete a la nave Campeon , tu peso es el correcto {i}')

    if i >= 150:
      print(f'Rebasas el Peso:{K} con tu peso excedido {i}')

@mensaje
def main():
  humanos = int(input("cantidad de humanos:"))
  lista = []
  for i in range(1,humanos+1):
    peso = int(input(f"Humano N|{i} - > peso kg:"))
    lista.append(peso)
  extraterrestre = nave(lista)
  return extraterrestre


if __name__ == '__main__':
  main()
