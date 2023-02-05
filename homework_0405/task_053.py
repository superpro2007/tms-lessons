# Напишите функцию generate_squares, которая принимает произвольное количество аргументов
# и возвращает список, состоящий из их квадратов.
# То есть generate_squares(1, 2, 3) -> [1, 4, 9].


def generate_squares(*args) -> list:
    spisok = [i**2 for i in (args)]
    return spisok


def generate_squares2(*args) -> list:
    spisok = list()
    for i in args:
        spisok.append(i**2)
    return spisok
    

print(generate_squares(1, 2, 3))

print(generate_squares2(1, 2, 3))
