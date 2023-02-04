# Пользователь вводит произвольное число.
# Посчитайте сумму цифр этого числа используя операторы % и //

number = int(input("vvedite number"))
summa = 0
while number > 0:
    summa += number % 10
    number = number // 10
print(summa)