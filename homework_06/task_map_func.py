# 1. Дан список чисел. Увеличьте каждый элемент в 100 раз.

def input_list(sep: str = ' ', prompt: str = '', converter: callable = int) -> list:
    return list(map(lambda x: converter(x), input(prompt).split(sep)))


spisok = input_list()
new_list = list(map(lambda n: n * 100, spisok))
print(new_list)

