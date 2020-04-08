def sum_of_even_fibonacci_nums(range_number):
  '''Эта функция записывает все числа Фибоначчи в заданном пределе в массив.
     Затем отбирает из них четные и суммирует их.'''
  fibonacci = [1, 2]
  even_fibonacci = 0
  while fibonacci[len(fibonacci) - 1] + fibonacci[len(fibonacci) - 2] <= range_number:
    next_number = fibonacci[len(fibonacci) - 1] + fibonacci[len(fibonacci) - 2]
    fibonacci.append(next_number)
  for n in fibonacci:
    if n % 2 == 0:
      even_fibonacci += n
  return even_fibonacci

print(sum_of_even_fibonacci_nums(4000000))
