#!/usr/bin/python3
"""
Bob is preparing to pass IQ test. The most frequent task in this
test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

Keep in mind that your task is to help Bob solve a real IQ test,
which means indexes of the elements start from 1 (not 0)

"""

def iq_test(numbers):
    nums = [int(i) for i in numbers.split(" ")]
    lista = list()
    cont=0
    for i in nums:
        cont+=1
        lista.append([i,cont])
    cont_im = 0
    cont_par = 0
    
    for x,y in lista:
        if x%2==0:
            cont_par+=1

        if x%2!=0:
            cont_im+=1
    
    if cont_par!=cont_im and cont_par >= cont_im:
        for x,y in lista:
            if x%2!=0:
                return y
    if cont_im!=cont_par and cont_im >= cont_par:
        for x,y in lista:
            if x%2==0:
                return y

if __name__ == '__main__':
    iq_test("2 4 7 8 10")
    """
    test.assert_equals(iq_test("2 4 7 8 10"),3)
    test.assert_equals(iq_test("1 2 2"), 1)
    test.assert_equals(iq_test("1 2 1 1"),2)
    """