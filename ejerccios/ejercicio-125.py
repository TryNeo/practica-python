#!/usr/bin/python3

"""
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.

"""

def expanded_form(num):
    try:
        expanded_list = [1]+[10**power for power in range (1,100)]
        nums_list = [int(str(num)[i]) for i in range(0,len(str(num)))][::-1]
        return " + ".join([str(nums_list[i]*expanded_list[i]) for i in range(0,len(nums_list)) if nums_list[i]!=0][::-1])
    except:
        pass


if __name__ == "__main__":
    print(expanded_form(12))

    """
    test.assert_equals(expanded_form(12), '10 + 2');
    test.assert_equals(expanded_form(42), '40 + 2');
    test.assert_equals(expanded_form(70304), '70000 + 300 + 4');
    """
