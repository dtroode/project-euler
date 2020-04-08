from math import sqrt
from itertools import count, islice


def is_prime(number):
    return (number > 1 and
            all(number % i for i in islice(count(2), int(sqrt(number)))))


def largest_prime_factor(number):
    primes_factors = []
    for i in range(1, int(sqrt(number)), 2):
        if is_prime(i) and number % i == 0:
            primes_factors.append(i)
        if is_prime(int(number / i)) and number % i == 0:
            k = int(number / i)
            primes_factors.append(k)
    max_prime_factor = max(primes_factors)
    return(max_prime_factor)

# Check


print(largest_prime_factor(93))
print(largest_prime_factor(155))
print(largest_prime_factor(13195))
print(largest_prime_factor(600851475143))
