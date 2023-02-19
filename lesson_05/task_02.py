# Напишите функцию list_sum, которая принимает на вход список и возвращает сумму элементов списка.
# Использование встроенной функции sum запрещено.


def list_sum(spisok_kotorii_summiruem: list) -> int:
    summa  = 0
    for element in spisok_kotorii_summiruem:
        summa += element
    return summa


print(list_sum([1, 4, 2]))
