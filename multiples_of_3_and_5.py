def multiplies(range_number):
	'''Эта функция находит сумму всех чисел в заданном пределе, которые кратны 3 и 5.'''
	sum = 0
	for n in range(range_number):
		if n % 3 == 0 or n % 5 == 0:
			sum += n
	return sum

print(multiplies(1000))