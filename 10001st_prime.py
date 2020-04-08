from math import sqrt
from itertools import count, islice


def is_prime(number):
    return (number > 1 and
            all(number % i for i in islice(count(2), int(sqrt(number)))))

def prime_by_index(range_number):
	primes = [2]
	i = 3
	while len(primes) < range_number:
		if is_prime(i):
			primes.append(i)
		i += 2
	return(primes[len(primes)-1])

print(prime_by_index(10001))