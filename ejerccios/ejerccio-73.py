#!/usr/bin/env python

import time 

def date_is_valid(str_date):
    try:
        resultado = time.strptime(str_date,'%Y-%m-%d')
        return True
    except:
        return False
    
            
def main():
    print("\tEjerccio73")
    value = x = input(':')
    resultado = date_is_valid(value)
    print(resultado)

if __name__ == '__main__':
    main()