# Дано: список студентов (скопируйте его в комментарии к слайду).
# Отсортируйте список по году рождения и выведите в консоль.
# Решите задачу сначала не используя lambda функцию, затем используя.

students_list = [
    ("Ivan", "Ivanov", 2003),
    ("Petr", "Petrov", 2005),
    ("Sidr", "Sidorov", 2004),
]


def get_year(student: tuple) -> int:
    return student[2]


print(sorted(students_list, key=get_year))
print(sorted(students_list, key=lambda student: student[2]))
