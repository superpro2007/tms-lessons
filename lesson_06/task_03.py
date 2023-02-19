# Напишите функцию my_sum, которая принимает два числа и возвращает их сумму. 
# Проверьте корректность её работы при разных значениях аргументов.
# Например my_sum(1, 2), my_sum(25, 75)
# def my_sum (a,b:int):
#     summa = a+b
#     return(summa)
# print (my_sum(1,2))
# print (my_sum(25,75))

# Напишите функцию simple_compare, которая принимает два числа и возвращает True, 
# если первое число меньше второго. Иначе возвращает False.
# def simple_compare(a,b: int) -> bool:
#     return a < b
#     # if a < b:
#     #     return (True)
#     # else:
#     #     return (False)
# x= simple_compare(10,21)
# print(x) 

# Напишите функцию compare, которая принимает два числа и возвращает -1 если первое число меньше второго, 
# 1 если первое больше второго, и 0 если они равны. Примеры:
# compare(100, 200) -> -1
# compare(200, 100) -> 1
# compare(10, 10) -> 0

# def compare(a,b: int) -> bool:
#     if a < b:
#         return(-1)
#     elif a > b:
#         return(1)
#     else:
#         return(0)
    
# x = compare(100,30)
# print (x)
        
# Напишите функцию filter_negative_numbers, которая принимает список чисел, 
# и возвращает новый список, составленный из элементов первого без отрицательных чисел, 
# Пример: filter_negative_numbers([6, -5, 0, -1, 100]) -> [5, 0, 100]

def filter_negative_numbers(numbers: list) -> list:
    new_spisok = []
    for num in numbers:
        if num >= 0:
            new_spisok.append(num)
    return(new_spisok)


x = filter_negative_numbers([0, -1, 4])
print(x)
            

        
    