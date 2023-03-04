# Напишите функцию is_date, которая принимает строку и возвращает
# bool. Функция должна вернуть True если переданная строка это дата в формате "DD-MM-YYYY",
# например "01-12-2022".
import re

def is_date(maybe_date:str)->bool:

   if re.fullmatch(r"\d{2}-\d{2}-\d{4}", maybe_date) is None:
       return False
   else:
       return True

if __name__ == '__main__':
    print(is_date('25-0-2032'))
    print(is_date('25-01-2032'))
