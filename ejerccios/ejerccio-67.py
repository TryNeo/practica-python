"""
Dado el siguiente archivo.txt, desarrolla un programa el cual nos permita validar direcciones IPs.

El programa de cumplir con los siguiente requerimientos.

El programa deberá mostrar en consola todas aquellas direcciones IPs validas.
Una dirección de IP valida será aquella que en su tercer y cuarto octeto posean valores menores a 100.
Ejemplo.

192.186.100.100
Dirección no valida ❌

192.186.80.100
Dirección no valida ❌

192.186.80.99
Dirección valida ✅

192.12.12.12
Dirección valida ✅
Ayuda: Es posible completar el ejercicio mediante una expresión regular.
"""

def validate_ips(ip):
    if int(ip[2]) >= 100 or int(ip[3]) >= 100:
        print("Dirección no valida ❌")
    else:
        print("Dirección valida ✅")


def main():
    print("\tEjerccio 67")
    print("")
    ips = input("ip:")
    if ' ' in ips:
        ips_new = ips.replace(' ', '.')
        ips_new = ips_new.split('.')
        if len(ips_new) == 4:
            validate_ips(ips_new)
        else:
            print("ingrese una ip valida")
    elif '.' in ips:
        ips_new = ips.split('.')
        if len(ips_new) == 4:
            validate_ips(ips_new)
        else:
            print("Ingresa una IP valida")
    else:
        print("Ingrese un IP valida")


if __name__ == '__main__':
    main()