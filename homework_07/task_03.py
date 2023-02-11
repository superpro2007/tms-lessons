# Решите прошлую задачу, в которой теперь пользователь может вводить буквы в любом регистре. 
# Вам по прежнему нужно удалить все гласные. При этом вывести результат нужно вывести сохранив изначальный регистр.

def remove_vowels(spisok_bukv: list) -> list:
    spisok_vowels = ["a", "e", "o", "i", "u"]
    new_spisok = list(filter(lambda bukva: bukva.lower() not in spisok_vowels, spisok_bukv))
    return new_spisok


spisok_bukv = input("vvedite spisok\n").split()
print(remove_vowels(spisok_bukv))