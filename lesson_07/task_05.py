# Во всех задачах, где дан массив чисел - используйте функцию input_list чтобы получить этот массив от пользователя.
# Для тренировки предлагается сделать каждую задачу тремя способами: с помощью обычного цикла for,
# с помощью генератора списков, с помощью функции map.
# 2.1 Дан список чисел. Увеличьте каждый элемент в 100 раз.

# print(list(map(lambda x: x * 100, my_list)))????

# 2.3 Дан список чисел. Разделите каждый элемент на 100 и округлите до целого числа (функция round).
printlist((map(lambda x: round(x / 100), my_list)))