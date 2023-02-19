# 5.1 Создайте файл university.py. Делайте задание в этом файле.
# 5.2 Импортируйте класс Student из первого задания
# from student import Student

from typing import List
from student import Student
from functools import reduce

# 5.3 Создайте переменную students - список объектов класса Student, с разными именами и средней оценкой.

students = [
    Student("Andrew", 7),
    Student("Eugene", 4),
    Student("Max", 10),
    Student("Kolyan", 9),
    Student("Alex", 6),
]

# 5.4 Посчитайте суммарную стипендию для всех студентов.

scholarship_sum = reduce(
    lambda sum_, student: sum_ + student.get_scholarship(), students, 0
)
print(scholarship_sum)

# 5.5 Посчитайте количество отличников (используйте метод is_excellent).

amount_students = 0
for student in students:
    if student.is_excellent():
        amount_students += 1

print(amount_students)

# 5.6 Заверните код для пунктов 4 и 5 к функции calc_sum_scholarship и get_excellent_student_count


def calc_sum_scholarship(students: List[Student]) -> int:
    scholarship_sum = reduce(
        lambda sum_, student: sum_ + student.get_scholarship(), students, 0
    )
    return scholarship_sum


print(calc_sum_scholarship(students))


def get_excellent_student_count(students: List[Student]) -> int:

    amount_students = 0

    for student in students:
        if student.is_excellent():
            amount_students += 1

    return amount_students


print(get_excellent_student_count(students))
