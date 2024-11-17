#!/usr/bin/env python3

def print_fibonacci(length):
    pass
    if length <= 0:
        print ([])
        return 
        
    fibonacci = [0, 1]

    for i in range(2, length):
        next_value = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_value)
    
    if length == 1:
        fibonacci = [0]

    print(fibonacci)