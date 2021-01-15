#!/usr/bin/env python


"""
Arbol de navidad
By Josue Lopez
"""

if __name__ == "__main__":
    base = "*"

         
    print("\t\t\t🌟")
    time.sleep(1)
    for x in range(10,11):
        for i in range(1, x+1):
            for j in range(x -i):
                print(" ", end=" ")
                
            for d in range(x+i-5):
                print("",end=" ")
            for z in range(1, 2 * i):
                print(base, end="")
            time.sleep(1)
            print()

    for i in range(1,5+1):
        for x in range(10- i):
            print("", end="  ")
            
        for x in range(10+ i-9):
            print("", end="  ")
        for j in range(2):
            print("#   ",end="")
        time.sleep(1)
        print()
        

    print(30*"___")
    time.sleep(1)
    
