def sum_square_difference(range_number):
	'''Counting square of the sum of numbers in range\
	without sum of squares of numbers in range'''
	sum = 0
	for i in range(range_number + 1):
		for n in range(i+1, range_number + 1):
			sum += 2 * n * i
	return(sum)

print(sum_square_difference(10))
print(sum_square_difference(100)) # 25164150


# With arithmetic progression

def sum_square_difference(range_number):
	sum = 0
	for i in range(1, range_number):
		# arithmetic progression sum multiplied by two
		t = (i * (i + 1) + i * range_number) * (range_number - i)
		sum += t
	return(sum)

print(sum_square_difference(10))
print(sum_square_difference(100)) # 25164150


# Their version

def sum_square_difference(range_number):
	# Just an arithmetic progression sum
	sum = range_number * (range_number + 1) / 2 
	# Proven formula for sum of squares
	sum_squared = (2 * range_number + 1) * (range_number + 1) * range_number / 6 
	return(int(sum**2 - sum_squared))

print(sum_square_difference(10))
print(sum_square_difference(100)) # 25164150