#!/usr/bin/python3
"""
Menos es más, o bueno, eso dice un refrán muy conocido. 
Es por ello que para este ejercicio será necesario desarrolles un script, 
el cual nos permita eliminar palabras de un párrafo. Es algo bastante sencillo.

El script deberá cumplir con los siguientes puntos.

El script deberá leer todo el contenido de un archivo .txt
El usuario podrá ingresar por teclado la palabra, o palabras las cuales desea eliminar.
Todas las palabras que el usuario haya ingresado serán eliminadas del contenido del archivo.
El programa debe ser capaz de generar un nuevo archivo .txt con sin las palabras indicadas.
El archivo original no debe sufrir modificaciones.
Ayuda:

Puedes colocar en código duro (Directamente en el script) los archivos con los cuales deseas trabajar.
Regularmente para este tipo de ejercicios siempre me gusta apoyarme de la novela de frankenstein
Puedes pedir al usuario que separe mediante un espacio las palabras que desea eliminar.
Restricciones:

No podrás hacer uso del método replace.

"""


def main():
    delete = int(input("ingrese la cantidad de palabras a eliminar:"))
    lista = list()
    for i in range(delete):
        delete_two = input("ingrese palabra a eliminar:").lower()
        lista.append(delete_two)
    print(lista)
    f = open('prueba.txt', 'r')
    a = [ x.split(" ")+["\n"] for i in f.readlines() for x in i.split("\n") if x != '']
    f.close()
    file = open('prueba_w.txt','w')
    for x in a:
        for i in lista:
            if i in x:
                for j in range(0,len(x)-1):
                    if i == x[j]:
                        x.remove(x[j])
        file.write(" ".join(x))

if __name__ == '__main__':
    main()