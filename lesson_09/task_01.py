# Задача 1. Создание класса

# 1.1 Создайте класс Person. У класса должно быть три поля: name, surname, age.
# Все поля должны заполняться в конструкторе класса (метод __init__).

class Person:
    def __init__ (self, person_name, person_surname, person_age):
        self.name = person_name
        self.surname = person_surname
        self.age = person_age
        
# 1.2 Добавьте в класс метод get_full_name, который должен возвращать полное имя в формате "{name} {surname}"

    def get_full_name(self):
        return f"{self.name}, {self.surname}"
    
# 1.3 Добавьте в класс метод become_older, который печатает в консоль "Happy birthday, {name}!" 
# и прибавляет к возрасту человека единицу.
    def become_older(self):
        print(f"Happy birthday {self.name}!")
        self.age += 1
        
        
# создание объекта
p = Person('Ivan', 'Ivanov', 20)

# обращение к полям класса
print(p.name)
print(p.surname)
print(p.age)

# вызов метода класса и вывод результата на экран
print(p.get_full_name())

# вызов метода класса + вывод изменившегося поля
p.become_older()
print(p.age)