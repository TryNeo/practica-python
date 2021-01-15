#!/usr/bin/python3

"""
Omirp se define como un número primo que al invertir sus dígitos da otro número primo.

Escriba un algoritmo para determinar si un número n tiene la característica de ser un número Omirp.
"""
def isPrime(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


def omirp(n):
    omirp = [i for i in n]
    omirp.reverse()
    new_omirp = ''.join(omirp)
    print(f"Se invierte sus digitos:{new_omirp}")
    resultado = isPrime(int(new_omirp))
    if resultado is True:
        print(f"{new_omirp} es Numero Primo")
        return True
    else:
        print(f"{new_omirp} no es Numero Primo entonces")
        return False

def main():
    n = input("ingrese numero:")
    resultado = isPrime(int(n))
    if resultado is True:
        print(f"{n} es un numero Primo")
        resultado = omirp(n)
        if resultado is True:
            print(f"Entonces el numero {n} es un numero omirp")
        else:
            print(f"Entonces el numero {n} no es numero omirp")
    else:
        print(f"{n} No es Primo")


if __name__ == "__main__":
    main()