# 1. Напишите функцию input_list, которая не принимает входных аргументов,
# в просто читает строку, которую ввёл пользователь (вызывая функцию input),
# разбивает её по пробелам (с помощью функции split), и возвращает список целых чисел.

# 1.1 Модернизируйте функцию из первой задачи дополнительными опциональными входными параметрами:
# prompt - сообщение, которое увидит пользователь при введении данных. Значение по умолчанию - "" (пустая строка).
# sep - разделитель, по которому разбивается строка. Значение по умолчанию - " " (пробел)
# element_type - тип элементов (int, float или str), которые будут в возвращаемом списке. По умолчанию - int.

def input_list(sep: str = ' ', prompt: str = '', converter = int) -> list:
    return list(map(lambda x: converter(x), input(prompt).split(sep)))


print(input_list(converter=str))