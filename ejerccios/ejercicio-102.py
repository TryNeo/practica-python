#!/bi/python3

"""
¿Acaso es un cuento? 🤔

Desarrolla una expresión regular que nos permita conocer si un string es o no un cuento, y para ello debemos validar que este comience con la famosa frase: Había una vez.


"""

import re


def main():
    cuento = input("ingrese el cuento:")
    buscar = re.search("^Había una vez.", cuento)
    if buscar:
        print("Es un cuento")
    else:
        print("No es un cuento")

if __name__ == "__main__":
    main()