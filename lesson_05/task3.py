# Создать функцию sum_and_max, которая принимает на вход неопределенное количество аргументов и
# возвращает их сумму и максимальное из них.
# Использовать встроенные sum и max разрешено.
from typing import Tuple


def sum_and_max(*args) -> Tuple[int, int]:
    summa = 0
    max = 0
    
    for element in args:
        summa += element
        
        if element > max:
            max = element
            
    return (summa, max)


print(sum_and_max(1, 3, 4, 5, 1, 9, 3))
