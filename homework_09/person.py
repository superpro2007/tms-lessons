# Задача 1. Класс Person

# 1.1 Создайте файл person.py, делайте задание в этом файле.
# 1.2 Создайте класс Person. У класса должно быть три поля: full_name, age, gender, которые
# должны заполняться в конструкторе. Будем считать что поле gender имеет тип str и может быть
# либо 'M' (male), либо 'F' (female).

import datetime


class Person:
    def __init__(self, full_name, age, gender):
        self.full_name = full_name
        self.age = age
        self.gender = gender

    # 1.3 Добавьте в класс метод print_person_info, который печатает на экран строку:
    # "Person: {full_name} ({gender}), {age} years old"

    def print_person_info(self) -> None:
        print(f"Person: {self.full_name} ({self.gender}), {self.age} years old")
        return None

    # 1.4 Добавьте метод get_birth_year, которая возвращает год рождения человека (рассчитанное как 2023 - age)
    # 1.5 Замените цифру 2023 на текущий год (чтобы ваша программа работала правильно даже через год).
    # Текущий год можно взять с помощью модуля datetime

    def get_birth_year(self) -> int:
        now = datetime.datetime.now()
        birthday_year = now.year - self.age
        return birthday_year
