"""Desarrolla un programa el cual permita a un usuario ingresar, vía teclado, la siguiente información:

Nombre
Email
Edad
Código postal
A partir de estos datos el programa deberá crear un archivo .JSON El archivo deberá tener por nombre user.json

Nombre: 'Eduardo Ismael'
Email: 'eduardo78@gmail.com'
Edad: 27
Código Postal: 0001

Archivo .json creado exitosamente.

"""

import json

def main():
    
    print("\tEjerccio 69")
    nombre = input("Nombre:")
    email = input("Email:")
    edad = int(input("Edad:"))
    cod_post = input("Codigo Postal:")
    
    data_user = {
        'nombre' : nombre,
        'email': email,
        'edad':edad,
        'cod_post': cod_post,
    } 
    with open('user.json','w') as file:
        json.dump(data_user,file)
        print("Archivo .json creado exitosamente")
        file.close()

if __name__ == '__main__':
    main()