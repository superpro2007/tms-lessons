# Дан список чисел с плавающей точкой.
# Преобразовать список, округлив каждое число до целых (функция round).
# Сделать задачу тремя способами, как на предыдущем слайде. 

my_list = [1.2, 3.5, 5.2]
rounded_list = []
for num in my_list:
    rounded_list.append(round(num))
print(rounded_list)
    
print([round(num) for num in my_list])

print(list(map(round, my_list)))