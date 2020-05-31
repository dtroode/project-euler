# First, first number of divisors
# over 5000 is 5001 — odd number.
# Only squares have odd numbers of divisors,
# because we can divide number on
# it's divisor and get new divisor —
# pairs, but with square, if we
# divide it by it's root, we get
# it's root again — so it's not pair.

# Also we have a sequence of oddness
# and eveness: two odd and two even
# numbers.

# This number must be even.

# Distance between two neighbour
# squares is a summ of their roots.

# Or not. We can jump over even
# number of divisors.

# 1
# 1 3
# 1 2 3 6
# 1 2 5 10
# 1 3 5 15
# 1 3 7 21
# 1 2 4 7 14 28
# 1 2 3 4 6 9 12 18 36
# 1 3 5 9 15 45
# 1 5 11 55
# 1 2 3 6 11 22 33 66
# 1 2 3 6 13 26 39 78

# 36 — 9
# 1 2 3 4 6 9 12 18 36

# 49 — 3
# 1 7 49

# 64 — 7
# 1 2 4 8 16 32 64

# 81 - 5
# 1 3 9 27 1

# 100
# 1 2 4 5 10 20 25 50 100

# 121
# 1 11 121

# 144
# 1 2 3 4 6 8 9 12 16 18 24 36 48 72 144

# 144 - 100 = (12 - 10)(12 + 10) = 2 * 22

# 1
# 4
# 9
# 16