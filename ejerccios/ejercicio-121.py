#!/usr/bin/python3
"""
Dispone de tres vectores que contienen el nombre, 
el género y la edad de cada uno de los miembros de un club juvenil. Los valores de género: 
masculino y femenino se representan por su inicial mediante ‘M‘ y ‘F‘ respectivamente.

a) Ingrese el nombre, el género y la edad de cada uno 
de los miembros del club. El ingreso finaliza cuando el usuario ya no desea 
seguir ingresando más datos (se deberá hacer una pregunta pertinente luego
del ingreso de un miembro).
b) Genere dos nuevos vectores, denominados HOMBRES
y MUJERES, los cuales deberán contener los nombres de todos los varones 
y de todas las damas, respectivamente.
c) Muestre por pantalla los nombres de los integrantes con la menor edad en el club.


"""



def main():
    general = list()
    while True:
        name = input("Ingrese el nombre:")
        gen = input("ingrese genero:").upper()
        edad = int(input("ingrese edad:"))
        general.append([name,gen,edad])
        q = input("¿Desea agregar otro miembro al club:(y/n)").lower()
        if q == "n":
            break
    
    hombre,mujer = list(),list()
    print("Miembros con menor edad en el club")
    for n,g,e in general:
        if g == "M":
            hombre.append(n)
        else:
            mujer.append(n)

        if e <= 20:
            print(n,e)

    print(general)
    print(hombre,mujer)




if __name__ == "__main__":
    main()