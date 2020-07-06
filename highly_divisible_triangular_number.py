# Project Euler
# Problem 12
# Highly divisible triangular number


import math


def count_divs(x):
    n = 0
    for i in range(1, int(math.sqrt(x)) + 1):
        if i**2 == x:
            n += 1
        elif x % i == 0:
            n += 2
    return n


def highly_divisible_triangular_number(number_of_divisors):
    n = 1
    c = 1
    i = 1
    while True:
        c += 1
        n += c
        if (count_divs(n) > number_of_divisors):
            break
    return n


print(highly_divisible_triangular_number(500))
