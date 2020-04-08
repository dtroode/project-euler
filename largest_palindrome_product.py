palindromes = []


def is_palindrome(first_num, second_num):
    '''This function checks a product of numbers for being a palindrome.
    '''
    product = first_num * second_num
    if str(product) == str(product)[::-1]:
        palindromes.append(product)


def largest_palindrome_product(start, end):
    '''This function checks products of all numbers in range.
    '''
    for first_num in range(start, end + 1):
        for second_num in range(start, end + 1):
            is_palindrome(first_num, second_num)


largest_palindrome_product(100, 999)

# Find largest palindrome in list
max_palindrome = max(palindromes)
print(max_palindrome)
