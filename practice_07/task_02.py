# 1.1 Дан список чисел. Увеличьте каждый элемент в 100 раз.
# 1.2 Дан список чисел. Преобразуйте этот список в список строк.
# 1.3 Дан список чисел. Разделите каждый элемент на 100 и округлите до целого числа (функция round).
# 1.4 * Напишите свою реализацию функций my_map, возвращающую список.
# 1.5 ** Напишите свою реализацию функций my_map, которая вместо возвращения списка использует ключевое слово yield при генерации очередного элемента.

from typing import Callable, Iterable


def input_list(
    sep: str = " ", 
    prompt: str = "vvedi\n", 
    converter=int
) -> list:
    return list(map(lambda x: converter(x), input(prompt).split(sep)))

x = input_list()

#1.4
def my_map(func: Callable, list_: Iterable) -> list:
    spisok = list()
    for el in list_:
        x = func(el)
        spisok.append(x)
    return(spisok)

#1.1
new_spisok = list(my_map(lambda num: 100 * num, x))
print(new_spisok)

#1.2
new_spisok = list(my_map(lambda num: str(num), x))
print(new_spisok)

#1.3
new_spisok = list(my_map(lambda num: round(num / 100), x))
print(new_spisok)




        
