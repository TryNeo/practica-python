
"""
Ejerccio de Prueba
decoradores

"""
def total_time(function):
    def total(*args, **kwargs):
        import time
        inicio = time.time()
        print(kwargs)
        for i in args:
            print(i)
        result = function(*args, **kwargs)
        print(result)
        total = int(time.time() - inicio)
        print(f'Segundos Transcurridos -> {total}s' )
        return result
    return total



@total_time
def main(lista,a = 'd'):
    import time
    for i in lista:
        if i > 5:
            lista.pop(2)
    return lista,a




if __name__ == '__main__':
    main([1, 2, 3, 4, 5, 6, 7, 8],a='2332')
    