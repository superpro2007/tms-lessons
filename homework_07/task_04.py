# Пользователь вводит произвольное количество слов через пробел.
# Затем (на следующей строке) вводит один символ (разделитель).
# Вам нужно написать функцию my_join, которая принимает список из строк и символ-разделить, и возвращает строку,
# в которой все слова из списка соединены через символ разделитель. Используйте функцию reduce.

from functools import reduce
from typing import List


vvod_slovo = input("vvedite slova").split()
vvod_razdelitel = input("vvedite skleivatel")


def my_join(slova: List[str], razdelitel: str) -> str:
    new_slovo = reduce(
        lambda skleenie_slova, slovo: skleenie_slova + razdelitel + slovo, slova
    )
    return new_slovo


print(my_join(vvod_slovo, vvod_razdelitel))
