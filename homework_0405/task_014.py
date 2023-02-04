# Программа загадывает случайное число от 0 до 100.
# Пользователь пытается угадать, вводя числа.
# Если пользователь угадал - выведите поздравление и завершите программу.
# Если пользователь не угадал, подскажите ему в в какую сторону идти.
# То есть, если число пользователя слишком большое - выведите “не угадал, ваше число больше загаданного”.
# Если меньше - выведите “не угадал, ваше число меньше загаданного”.

import random

number = input("vvedite number\n")
random_number = str(random.randint(0, 100))

while number != random_number:
    if number > random_number:
        text = "sliwkom bolshoe davai ewe\n"
    elif number < random_number:
        text = "sliwkom malenkoe\n"
        
    number = input(text)

print("molodec")
