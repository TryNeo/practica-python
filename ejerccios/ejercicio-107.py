#!/bin/python3

"""
Habrá ocasiones en la cuales deseemos conocer el tiempo exacto que le toma a una tarea finalizar. Es por ello que en esta ocasión será necesario crees un decorador el cual nos permita conocer esta información.

El decorador tendrá por nombre _execution_time_.
El decorador debe funcionar para cualquier función.
El decorador debe imprimir en consola, mediante el siguiente formato: - Tiempo de ejecución: x ms, el tiempo que le tomo a la función decorada finalizar.
Ejemplo.

@execution_time
def super_task():
    import time

    time.sleep(1)
    return 10


>>> super_task()
- Tiempo de ejecución: 1.0038602352142334 ms
Ayuda:

Será necesario utilices el módulo time.
La forma más sencilla de conocer el momento exacto es a travez de la función time. time.time()

"""





def execution_time(function):
    def total(*args, **kwargs):
        import time
        inicio = time.time()
        result = function(*args, **kwargs)
        total = float(time.time() - inicio)
        print(f'Tiempo de ejecución: {total} ms' )
        return result
    return total



@execution_time
def main(a,b):
    import time
    time.sleep(1)
    return a+b



if __name__ == '__main__':
    main(10,130)