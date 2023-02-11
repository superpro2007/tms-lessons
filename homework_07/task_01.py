# Пользователь вводит произвольное количество латинских букв через пробел. Буквы могут быть как в верхнем, 
# так и в нижнем регистре (на результат работы это влиять не должно).
# Напишите функцию map_to_tuples, которая принимает список из этих букв и
# возвращает список из кортежей. В каждом кортеже первой должна идти буква в верхнем регистре, 
# а второй эта же буква в нижнем.

from typing import List


def map_tuples(spisok_bukv:list) -> List[tuple]:
    new_spisok = list(map(lambda bukva: (bukva.upper(), bukva.lower()), spisok_bukv))
    return(new_spisok)

spisok_bukv = input('vvedite bykvi\n').split()
print(map_tuples(spisok_bukv))

