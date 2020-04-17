from math import sqrt
from itertools import count, islice


def is_prime(number):
    if number != 2 and number % 2 == 0:
        return False
    return (number > 1 and
            all(number % i for i in islice(count(2), int(sqrt(number)-1))))


def summation_of_primes(range_number):
    """This function cycle through all numbers in givien range
    and check if number is prime. If so — add to sum variable.
    In the end sum is the sum of all primes.
    """
    sum = 0
    for i in range(range_number):
        if is_prime(i):
            sum += i
    return sum

# Check


print(summation_of_primes(10))
print(summation_of_primes(2000000))
