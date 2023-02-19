# sum = 0
# for i in range(11):
#     sum += i
# print(sum)

# Дан список чисел. Найти их сумму.

# s = list(input().split())
# summa = 0
# for el in s:
#     summa +=int(el)
# print(sum([int(el) for el in input().split()]))
# # summa = 0
# for i in new_s:
#     summa += i
# print(summa)

# Дан список чисел. Найти их максимальное среди них.

# s = [int(el) for el in input().split()]
# max_el = s[0]
# for el in s:
#     if el > max_el:
#         max_el = el
# print(max_el)


# Дан список чисел. Если среди них есть ноль - вывести yes, иначе no.
s = [int(el) for el in input().split()]
number = 0
for el in s:
    if el == number:
        print ('yes')
    else:
        print('no')
    break