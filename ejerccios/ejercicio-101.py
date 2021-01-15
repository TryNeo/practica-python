#!/usr/bin/python3
"""
Dado el siguiente endpoint.

https://pokeapi.co/api/v2/pokemon/1/
Mostrar en consola el nombre del Pokemon.

Ejemplo

El nombre del pokemon es: bulbasaur
Ayuda:

Una muy buena idea es utilizar la librería requests para realizar peticiones HTTP.
JSONView es una extensión de Chrome que nos permite visualizar los objetos JSON de una manera mucho más legible.
"""
import requests

def pokemon(URL):
    response = requests.get(URL)
    if response.status_code == 200:
        return f'El nombre del pokemon es: {response.json().get("name")}'
    else:
        return 'Error | Conexion'


def main():
    id_pokemon = int(input("id de pokemon:"))
    URL = "https://pokeapi.co/api/v2/pokemon/"+str(id_pokemon)
    resultado = pokemon(URL)
    print(resultado)


if __name__ == "__main__":
    main()