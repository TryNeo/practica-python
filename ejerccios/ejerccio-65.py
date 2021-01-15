import click
import os
import time
import datetime

"""
Desarrolla un programa el cual nos permita monitorear un directorio dentro de nuestro sistema. 🥳

El programa debe cumplir con los siguiente requerimientos.

El usuario deberá ingresar, mediante un argumento, el directorio a monitorear.
El programa mostrará en consola la fecha exacta en la que el directorio fue modificado.
Ejemplo: >>> Los archivos dentro del directorio han sido modificados. - 2020-09-20 11:35:34.886407
Se considera que un directorio fue modificando cuando ocurre alguna de estas acciones.
Se crea un nuevo archivo en el directorio.
Se modifica un archivo en el directorio.
Se elimina un nuevo archivo en el directorio.
Todos los sub documentos serán tomados en cuenta para validar si el directorio sufrió o no una modificación.
El programa deberá ejecutarse de forma indefinida, hasta que el usuario así lo indique.
A validar:

Será necesario validar que el directorio ingresado por el usuario sea valido, es decir, que exista en el sistema.
El directorio ingresado deberá ser, de forma obligatoria, un directorio para un folder (Carpeta), y no para algún tipo de archivo o link.
Ejemplo.

$ python main.py /Users/eduardo/Documents/tutorials/project
>>> Los archivos dentro del directorio han sido modificados. - 2020-09-20 11:59:23.559344
>>> Los archivos dentro del directorio han sido modificados. - 2020-09-20 11:59:30.583607

Deseado:

El programa deberá ser capaz de indicar si el directorio es valido o no (Si existe y es un folder).
Mediate una bandera (--save -s) el usuario podrá crear un log con todas las fechas en las cuales el directorio sufrió modificaciones.
El log tendrá por nombre changes.txt y será creado al mismo nivel que nuestro script

"""


@click.command()
@click.argument('ruta')
@click.option('--save', '-s', is_flag=True, default=False)
def main(ruta, save):
    if os.path.isdir(ruta):
        stat_info = os.stat(ruta)
        #last_accesd = time.ctime(stat_info.st_atime)
        #modified_accesd = time.ctime(stat_info.st_atime)
        modified_time = time.localtime(stat_info.st_mtime)
        var = ">>> Los archivos dentro del directorio ha sido modificados. - {}-{}-{} {}:{}:{}".format(
            modified_time.tm_year, modified_time.tm_mon, modified_time.tm_mday,
            modified_time.tm_hour, modified_time.tm_min, modified_time.tm_sec)
        print(var)
        if save:
            file = open("changes.txt", 'a')
            file.write(var)
            file.write("\n")
            file.close()
        else:
            pass
    else:
        print("Error! ingrese una ruta valida o existente")


if __name__ == '__main__':
    main()
