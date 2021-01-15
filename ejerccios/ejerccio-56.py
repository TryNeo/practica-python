#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

"""
Generar un archivo .txt que tenga por nombre la siguiente estructura.

<año>_<mes>_<dia>_pywombat.txt
El año, mes y día deben pertenecer a la fecha actual en la cual se ejecuta el script.
"""

def main():
    print("Ejerccio 56")
    today = datetime.datetime.now()
    f = open (str(today.year)+'_'+str(today.month)+'_'+str(today.day)+'_'+'pywombat.txt','w')
    f.write(str(today))
    f.close()

if __name__ == '__main__':
    main()