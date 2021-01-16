#!/bin/python3


def separador(lista : list):
    tendencia = [lista.count(i) for i in lista]
    total = sorted(list(set(list((lista[x],tendencia[x])for x in range(0,len(tendencia))))))
    general = max([x for i,x in total])
    if general  > 1:
        return [i for i in total if general in i]
    else:
        return general

def tabulando(txt:list):
    mensaje =[ j for i in [ x for i,x in txt] for j in i.split(' ') if '#' in j]
    if separador(mensaje) == 1:
        return [['No hay Tendencia']]
    else:
        return separador(mensaje)


def usuarioFrecuente(usuarios:list):
    usuario = [i for i,x in usuarios]
    if separador(usuario) == 1:
        return ["No hay usuario frecuente"]
    else:
         return separador(usuario)


def usuarioMensaje(cant):
    return [[input("usuario:"),input("mensaje:")] for i in range(1,cant+1)]
    

def menu():
    print("""
    1.Ingrese Mensaje
    2.Usuario Frecuente
    3.Tendencias
    4.Salir
    """)


def main():
    while True:
        menu()
        op = input("ingrese una opcion:")
        if op == "1":
            cantidad = int(input("¿Cuantos usuarios va agregar?:"))
            resultado = usuarioMensaje(cantidad)
        elif op =="2":
            resultado_2 = usuarioFrecuente(resultado)
            print(f"Usuario Frecuente:{resultado_2[0]}")
        elif op =="3":
            resultado_3 = tabulando(resultado)
            print(f"La tendencia es: {resultado_3[0][0]}")
        elif op == "4":
            break

if __name__ == "__main__":
    main()