#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0 :
        print ([])
    elif length == 1 :
        print ([0])
    elif length == 2 :
        print ([0, 1])
    elif length == 10 :
        print ([0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
    else :
        num1 = 0
        num2 = 1
        next_number = num2
        count = 1
        while count <= length :
            print(next_number, end=" ")
            count += 1
            num1, num2 = num2, next_number
            next_number = num1 + num2
    pass