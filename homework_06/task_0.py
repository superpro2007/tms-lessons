# 1. Дано: список студентов (скопируйте его в комментарии к слайду).
# Отсортируйте список по году рождения и выведите в консоль.
# Решите задачу сначала не используя lambda функцию, затем используя.

# students_list = [
#     ("Ivan", "Ivanov", 2003),
#     ("Petr", "Petrov", 2005),
#     ("Sidr", "Sidorov", 2004),
# ]
# # students_list.sort(key = lambda student: student[2] )

# # print(students_list)
# def get_year(student: tuple) -> int:
#     return student[2]

# sorted_list = sorted(students_list, key=get_year)
# print(sorted_list)

# 1. Дан список чисел с плавающей точкой.
# Преобразовать список, округлив каждое число до целых (функция round).
# Сделать задачу тремя способами, как на предыдущем слайде.

list_ = [2.3, 5.3, 1.6, 6.9]
# list_new = []
# for number in list_:
#     list_new.append(round(number))
# print(list_new)

# rounded_list = [round(number) for number in list_]
# print(rounded_list)
# rounded_list = list(map(round, list_))
# print(rounded_list)

# 3. Дан список целых чисел.
# Найти их сумму, сначала используя обычный подход, затем используя функцию reduce.
# list_ = [4, 6, 9, 3]
# num = 0
# for number in list_:
#     num += number
# print(num)

# from functools import reduce
# def sum(num: int, number: int) -> int:
#     return num + number

# num = reduce(sum, list_, 0)
# print(num)
# num = reduce(lambda num, number: num+number, list_, 0)
# print(num)

