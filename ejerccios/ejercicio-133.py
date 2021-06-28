#!/usr/bin/python3

import os





def main():
    usuario = input("ingresa la ruta del archivo:")
    if (os.path.isfile(usuario)):
        filecontent = usuario.split("/")
        try:
            cantidad = int(input("Cantidad de palabras por bloque:"))
            file = open(filecontent[-1],'r')
            content = file.read().rstrip().split()
            for i in content[0:cantidad]:
                print(i)
                print("\n\n\n")

        except FileNotFoundError as error:
            print('No fue posible obtener el archivo',error)

    else:
        print("No fue posible obtener el archivo")


if __name__ == '__main__':
    main()