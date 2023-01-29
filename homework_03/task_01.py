# Пользователь вводит одно число, сторона квардата.
# Вывести кортеж из трёх чисел: периметр квадрата, площадь квадрата, диагональ квадрата.

side_size = input("Enter side size \n")
side_size = int(side_size)
p = side_size * 4
s = side_size**2
d = side_size * 2**0.5
print(f"p={p} s={s} d={d}")
