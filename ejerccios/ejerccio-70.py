"""
Desarrolla un programa en Python que nos permita conocer la cantidad de letras que posee una palabra o texto.

El usuario podrá ingresar, vía teclado, el texto del cual quiere conocer su longitud (Los espacios deben ser tomados en cuenta).
Ejemplos.
"""

def logit(value):
    count = 0
    for i in value:
        count+=1
    return count

def main():
    texto= input("ingrese un texto:")
    result = logit(texto)
    print(result)

if __name__ == '__main__':
    main()