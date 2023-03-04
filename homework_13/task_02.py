# Напишите функцию is_float_number, которая принимает строку и возвращает bool.
# Функция должна вернуть True если переданная строка
# это корректное число с плавающей точкой. Например "1.0", "20.45"
import re


def is_float_number(number: str) -> bool:
    if re.fullmatch(r'\d+\.\d+', number) is None:
        return False
    else:
        return True

if __name__ == "__main__":
    print(is_float_number('21.234-'))
    print(is_float_number('21.33'))
    print(is_float_number('12-34'))


