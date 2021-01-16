#!/bin/python3

""" 
En redes sociales un mensaje puede contener palabras etiquetadas, también conocidas como “hashtag” por iniciar con el símbolo ‘#’ para resaltar un tópico en particular.

a) Realice una función etiquetados(mensaje), que al recibir un mensaje, busque y retorne las palabras etiquetadas.
Considere que las etiquetadas terminan al encontrar un espacio o una coma, y que también encontrarse al último el mensaje.

Ejemplo:
>> mensaje='En la #ESPOL se usa aprendizaje por proyectos y entre pares, publicado #ELUNIVERSO el domingo 7 de febrero'
>> etiquetados(mensaje)
     ['#ESPOL', '#ELUNIVERSO']
>> mensaje='IX Semillero de Futuros Científicos e Ingenieros Inscripciones #AJA #FCNM #ESPOL'
>> etiquetados(mensaje)
     ['#AJA','#FCNM', '#ESPOL']


b) Elabore una función tabulando(palabras) que reciba una lista de palabras que pueden ser repetidas y genere una tabla con las palabras únicas junto al conteo de las veces que aparece cada una en la lista.

>>palabras=[‘#ESPOL’, ‘#ELUNIVERSO’, ‘#AJA’, ’#FCNM’, ‘#ESPOL’]
>>tabulando(palabras)
     [[#ESPOL,        2]
      [#AJA,          1]
      [#FCNM,         1]
      [#ELUNIVERSO,   1]]
"""



def tabulando(mensaje:list):
    a = [mensaje.count(i )for i in mensaje]
    return sorted(list(set(list((mensaje[x],a[x])for x in range(0,len(a))))))


def etiquetados(mensaje:str):
    return [i for i in mensaje.split(' ') if '#' in i ]

def main():
    #etiqueta = etiquetados(mensaje)
    palabras=['#ESPOL', '#ELUNIVERSO', '#AJA', '#FCNM', '#ESPOL']
    tabulado = tabulando(palabras)
    #print(etiqueta)
    print(tabulado)

if __name__ == "__main__":
    main()





