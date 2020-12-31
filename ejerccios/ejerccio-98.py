#!/usr/bin/python3

"""
l proceso de registros de votantes en un padrón electoral requiere de las siguientes operaciones:

1. Registrar: cédula, nombre de un votante (3 puntos)
2. Mostrar nombres de personas con cédulas válidas (10 puntos)
3. Mostrar nombres de personas con cédulas no válidas (2 puntos)
4. Mostrar total de inscritos
5. Salir

Realice un programa que permita realizar las operaciones descritas, 
se permita registrar sin restricción a los votantes para luego para 
validar las cédulas; utilice la función validaid(cedula) descrita en el tema anterior.


"""
personas = list()

def menu():
    print("""
1. Registrar: cédula, nombre de un votante (3 puntos)
2. Mostrar nombres de personas con cédulas válidas (10 puntos)
3. Mostrar nombres de personas con cédulas no válidas (2 puntos)
4. Mostrar total de inscritos
5. Salir 
          """)


def registrarPersonas(cedula,nombre):
    verificado = verificadorCedula(cedula)
    if verificado:
        personas.append([cedula,nombre,verificado])
    else:
        personas.append([cedula,nombre,verificado])

def mostrarValidos(personas):
    return [i[1] for i in personas if i[2] == True]

def noValidos(personas):
    return [i[1] for i in personas if i[2] == False]

def inscritos(personas):
    return len(personas)

def verificadorCedula(cedula):
    contenido = [int(i) for i in cedula]
    ultimo_digito = contenido[-1]
    primeros_digito = contenido[:-1]
    a = [primeros_digito[i] for i in [i for i in range(0,len(primeros_digito))] if i %2 == 1]
    b = [i for i in [i+i for i in [primeros_digito[i] for i in [i for i in range(0,len(primeros_digito))] if i %2 == 0]] if i <= 9 ]\
        +[ i-9  for i in [i*2 for i in [primeros_digito[i] for i in [i for i in range(0,len(primeros_digito))] if i %2 == 0]] if i >= 9 ]
    digito = str(sum(a)+sum(b))
    total = (int(digito[0])+1)*10
    if total == 10:
        total = 0
    if total-(sum(a)+sum(b)) == ultimo_digito:
        return True
    else:
        return False
    
    
    
def main():
    while True:
        menu()
        op = int(input('opciones:'))
        print()
        if op == 1:
            nombre = input("nombre:")
            cedula = input("cedula:")
            registrarPersonas(cedula,nombre)
        elif op == 2:
            resultado = mostrarValidos(personas)
            if resultado == []:
                print("No hay Registros Validos")
            else:
                print(resultado)
        elif op == 3:
            resultado = noValidos(personas)
            if resultado == []:
                print("No hay Registros Validos")
            else:
                print(resultado)
        elif op == 4:
            print(f"Total inscritos: {inscritos(personas)}")
        else:
            break
        

if __name__ == "__main__":
    main()