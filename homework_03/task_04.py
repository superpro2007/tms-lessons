# Пользователь вводит произвольную строку. Выведите кортеж из уникальных символов введённой строки.

string = input('enter string\n')
string = set(string)
string = tuple(string)
print(string)