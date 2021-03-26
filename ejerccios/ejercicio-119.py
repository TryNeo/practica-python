#!/usr/bin/env python



def vasos(n,x):
    cont = 0
    total = 0
    while cont < x:
        reciclado = n//x
        print(reciclado)
        sobra = n%x
        print(sobra)
        total = total + reciclado
        print(total)
        n = reciclado + sobra
        cont+=1
    print(total)

def main():
    n = int(input('Cuantos vasos usados:'))
    x = int(input('nuevos/reciclado:'))
    vasos(n,x)


if __name__ == '__main__':
    main()