# Напишите функцию is_year_leap, которая принимает число (год) и
# возвращает True если год високосный (см. комментарий к слайда), False если нет.

# Если год делится на 4 без остатка, то переходите к следующему шагу. 
# Если он не делится на 4, это не високосный год. Например: 1997 год не високосный.
# Если год делится на 4, но не на 100. Например: 2012 год високосный. 
# Если год делится и на 4, и на 100, перейдите к следующему шагу.
# Если год делится на 100, но не на 400. Например: 1900 год,
# то это не високосный год. Если год делится на оба, то это високосный год. Итак, 2000 год високосный.

def is_year_leap(year: int) -> bool:
    if year %4 != 0:
        return (False)
    if year %100 != 0:
        return (True)
    if year %400 != 0:
        return(False)
    return(True)
print(is_year_leap(1997))
print(is_year_leap(2012))
print(is_year_leap(1900))
print(is_year_leap(2000))