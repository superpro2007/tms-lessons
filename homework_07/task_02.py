# Пользователь вводит произвольное количество маленьких латинских букв через пробел.
# Напишите функцию remove_vowels, которая принимает список из этих букв и удаляет из него все гласные буквы.
# Выведите результат работы на экран.


def remove_vowels(spisok_bukv: list) -> list:
    spisok_vowels = ["a", "e", "o", "i", "u"]
    new_spisok = list(filter(lambda bukva: bukva not in spisok_vowels, spisok_bukv))
    return new_spisok


spisok_bukv = input("vvedite spisok\n").split()
print(remove_vowels(spisok_bukv))
