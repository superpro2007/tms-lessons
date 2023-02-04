# Программа загадывает случайное число от 1 до 5.
# Пользователь пытается угадать, вводя числа.
# Если пользователь угадал - выведите поздравление и завершите программу.
# Если не угадал - программа предлагает попробовать ещё раз до тех пор, пока пользователь не угадает.

import random

number = input("vvedi chislo\n")
random_number = str(random.randint(1, 5))

# if number == random_number:
#     print("ygadal")
# else:
#     print("ne ygadal, vvedi chislo")

while number != random_number:
    number = input('ne ygadal lalka, davai ewe raz\n')
print('ny ti paren krasava')    