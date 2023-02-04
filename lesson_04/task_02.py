#Пользователь вводит число. Посчитайте сумму цифр этого числа.
#Количество цифр числа может быть произвольными

number = input('Vvedite number\n')
summa = 0
for i in number:
    summa += int(i)
print(summa)