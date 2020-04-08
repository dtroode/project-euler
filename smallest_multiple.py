# Brutforce method

from math import sqrt, floor, log
a = []


def smallest_multiple(range_number):
    for n in range(1, range_number + 1):
        a.append(n)
    while True:
        if all(n % i == 0 for i in a) == True:
            return n
        n += 1


print(smallest_multiple(20))


# Optimized method


def list_all_numbers(range_number):
    all_numbers_list = []
    for i in range(2, range_number):
        all_numbers_list.append(i)
    return all_numbers_list


def primes(range_number):
    all_numbers_in_range = list_all_numbers(range_number)
    for i in all_numbers_in_range:
        for n in all_numbers_in_range:
            if n != i and n % i == 0:
                all_numbers_in_range.remove(n)
    return(all_numbers_in_range)


def smallest_multiple(range):
    multiple = 1
    primes_list = primes(range)
    check = True
    limit = sqrt(range)

    for prime in primes_list:
        if prime <= range:
            degree = 1
            if check:
                if prime <= limit:
                    degree = floor(log(range)/log(prime))
                else:
                    check = False
            multiple *= prime**degree
    return(multiple)


print(smallest_multiple(20))
