
"""
Ejerccio de Prueba
decoradores

"""
def total_time(function):
    def total(*args, **kwargs):
        import time
        inicio = time.time()
        result = function(*args, **kwargs)
        total = int(time.time() - inicio)
        print(f'Segundos Transcurridos -> {total}s' )
        return result
    return total



@total_time
def main(a,b):
    import time
    time.sleep(10)
    return a+b




if __name__ == '__main__':
    main(10,130)
    