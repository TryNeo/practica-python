#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Escribir en Python un programa que haga lo siguiente:


1.Muestra un mensaje de bienvenida por pantalla.2.Le pide al usuario que introduzca dos números enteros n1 y n2.
3.Imprime el cuadrado de todos los números enteros del intervalo [n1, n2)
4.Muestra un mensaje de despedida por pantalla.

"""

#declarando la funcion para calcular el cuadrado, recibiendo como parametro a y b, que seran los numeros ingresados por el usuario

def cuadrado(a,b):
    #declarando un ciclo for para mejor comodidad 
    for x in range(0,b): # usamos range para darle un rango definido hasta donde deseemos llegar ,como por ejemplo: 1 hasta el 10
        #hacemos el calculo simple ,multiplicando x * x , que serian en contexto 2*2 etc
        cuad = x*a
        resultado = f"el cuadrado del numero {x} entre el {x} es : {cuad}"
        print(resultado)#e imprimos  el resultado obtenido  dandole un formato  de texto mejor para mejor visualizacion    
    return resultado # y retornamos el resultado que obtenemos
    
    
#declaramos la funcion que ejecutara mayor parte del script
def main():
    print("\tEjerccio 1")
    print()
    print("Bienvenido")
    print("Se calcularán cuadrados de números")
    print()
    a = int(input("ingrese un numero:"))
    b = int(input("ingrese el numero hasta donde desea llegar:"))
    #declaramos una variable que se llamara resultado , que recibe como  parametro la funcion cuadrado que habiamos creado con anterioridad
    resultado = cuadrado(a,b)
    return resultado # y retornamos el resultado que obtenemos
    
    
    

if __name__ == '__main__':
    main()

