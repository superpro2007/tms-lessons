# Дан список целых чисел.
# Найти их сумму, сначала используя обычный подход, затем используя функцию reduce.

numbers = [1, 2, 3, 4, 5]
x = 0
for num in numbers:
    x += num
print(x)

from functools import reduce
print(reduce(lambda x, y: x + y, numbers, 0))
