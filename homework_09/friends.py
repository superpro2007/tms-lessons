# 4.1.Создайте файл friends.py. Делайте задание в этом файле.
# 4.2.Импортируйте класс Person из первого задания
# from person import Person
# 4.3. Создайте переменную my_friends - список из объектов класса Person. Добавьте в него некоторое количество вымышленных друзей с разными именами, возрастом и полом.
# 4.4 Выведите информацию о каждом друге на экран.

from typing import List
from person import Person

my_friends = [
    Person("Andrew", 31, "M"),
    Person("Alex", 34, "M"),
    Person("Nina", 30, "F"),
    Person("Kate", 28, "F"),
]
for friend in my_friends:

    friend.print_person_info()

# 4.5 Найдите среди друзей самого старшего, выведите информацию о нём на экран.

oldest_friend = max(my_friends, key=lambda friend: friend.age)
print()
oldest_friend.print_person_info()

# 4.6 Выведите на экран информацию о всех друзьях мужского пола
# (можно использовать функцию filter, либо генератор списков).

man_friends = filter(lambda friend: friend.gender == "M", my_friends)

for friend in man_friends:
    friend.print_person_info()

# 4.7 Заверните код из пунктов 5 и 6 в функции get_oldest_person и filter_male_person соответственно.


def get_oldest_person(friends: List[Person]) -> Person:
    oldest_friend = max(friends, key=lambda friend: friend.age)
    return oldest_friend


print()
get_oldest_person(my_friends).print_person_info()


def filter_male_person(friends: List[Person]) -> List[Person]:
    man_friends = filter(lambda friend: friend.gender == "M", friends)
    return list(man_friends)


print()
x = filter_male_person(my_friends)
for friend in x:
    friend.print_person_info()
