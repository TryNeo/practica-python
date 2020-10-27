#!/usr/bin/env python
# -*- coding: utf-8 -*-


def common_keys(a,b):
    return tuple(set(a.keys()) & set(b.keys()))

def main():
    print("\tEjerccio 61")
    print("")
    a = {'a':10,'b':20,'c':30}
    b = {'a':10,'c':30,'d':40}
    resultado = common_keys(a,b)
    print(resultado)

if __name__ == '__main__':
    main()