#!/usr/bin/python3
def max_integer(my_list=[]):
    maxi = 0
    if len(my_list) == 0:
        return None
    for num in my_list:
        if num > maxi:
            maxi = num
    return(maxi)
