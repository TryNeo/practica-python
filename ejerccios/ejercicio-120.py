import os

""" 
Desarrolla un programa el cual nos permita conocer el contenido de un archivo .txt

Requerimientos del programa.

El usuarios podrá ingresar, vía teclado, la dirección absoluta del archivo del cual se desea leer.
El programa deberá mostrar en consola el contenido de dicho archivo.
En caso la dirección ingresada por el usuario sea incorrecta, o simplemente no sea posible leer el archivo, el programa mostrara en consola el siguiente mensaje No fue posible obtener el archivo.
Ejemplo.

Ingresa la dirección del archivo: 'Users/eduardo/documents/example.txt'
Hola, este es un archivo de prueba

Ingresa la dirección del archivo: 'Users/eduardo/documents/example2.txt'
Hola, este es un archivo de prueba
En esta ocasión el archivo posee más de una línea;
Es decir, existen saltos de línea.

Ingresa la dirección del archivo: 'Users/eduardos/documents/example2.txt'
No fue posible obtener el archivo

"""

if __name__ == "__main__":
    fileName = input("Ingresa la dirección del archivo:")
    if (os.path.isfile(fileName)):
        filecontent = fileName.split("/")
        try:
            file = open(filecontent[-1],'r')
            for i in file.readlines():
                print(i)
        except FileNotFoundError as error:
            print('No fue posible obtener el archivo')

    else:
        print("No fue posible obtener el archivo")