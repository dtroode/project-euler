from math import sqrt
from itertools import count, islice

def is_prime(number):
    if number != 2 and number % 2 == 0:
        return False
    return (number > 1 and
            all(number % i for i in islice(count(2), int(sqrt(number)-1))))


def largest_prime_factor(number):
    primes_factors_below_square = [x for x in range(1, int(sqrt(number)), 2)\
                                if (is_prime(x) and number % x == 0)]
    primes_factors_above_square = [int(number / x)\
                                for x in range(1, int(sqrt(number)), 2)\
                                if (is_prime(int(number / x))\
                                    and number % x == 0)]
    primes_factors = primes_factors_below_square + primes_factors_above_square
    max_prime_factor = max(primes_factors)
    return(max_prime_factor)

# Check


print(largest_prime_factor(93))
print(largest_prime_factor(155))
print(largest_prime_factor(13195))
print(largest_prime_factor(600851475143))