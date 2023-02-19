# Напишите функцию get_natural_numbers, которое принимает целое число n и
# возвращает список натуральных чисел от 1 до n включительно. Используйте генераторы списков.
def get_natural_numbers(chislo: int) -> list:
    a = [i for i in range(1, chislo+1)]
   
    return(a)

print(get_natural_numbers(2))
