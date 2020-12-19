#!/usr/bin/env python

"""
 SUBASTA INVERSA es un tipo de subasta en la que se invierte el papel 
 de comprador y vendedor, con el objetivo principal de impulsar los
  precios de compra a la baja
  
Una vez que el comprador plantea el requerimiento, los vendedores registran el valor de su oferta y se selecciona la de menor precio; si más de un vendedor iguala el menor precio se selecciona aleatoriamente uno.

Elabore un algoritmo que, siguiendo las reglas descritas, permita:

a) Ingresar las ofertas económicas para los n vendedores.

b) Identificar el monto correspondiente a la mejor oferta.

c) Determinar y mostrar cuántos vendedores cumplen con la mejor oferta y al vendedor seleccionado.

Ejemplo:
 ¿Cuántos vendedores?: 8
 ¿valor oferta [1]?: 700
 ¿valor oferta [2]?: 400
 ¿valor oferta [3]?: 400    
 ¿valor oferta [4]?: 500
 ¿valor oferta [5]?: 400
 ¿valor oferta [6]?: 500
 ¿valor oferta [7]?: 600
 ¿valor oferta [8]?: 700
 - El menor valor es: 400
 - Cumplen mejor oferta: 3
 - El vendedor seleccionado es: 5
"""
import random
def subastaInversa(vendedores):
    subasta = list()
    vendedorSelecionado = list()
    vendedoresOferta = 0
    for i in range(1,vendedores+1):
        oferta = int(input(f"¿Valor oferta [{i}]?:"))
        subasta.append([i,oferta])
        
    mejorOferta = min([x for i,x in subasta])

    for j,y in subasta:
        if mejorOferta == y:
            vendedoresOferta+=1
            vendedorSelecionado.append(j)

    print(f"- El mejor valor es: {mejorOferta}")
    print(f"- Cumple mejor oferta: {vendedoresOferta}")
    print(f"- El vendor Selecionado es: {random.choice(vendedorSelecionado)}")
    
def main():
    vendedores = int(input("¿Cuantos vendedores?:"))
    resultado = subastaInversa(vendedores)

if __name__ == "__main__":
    main()