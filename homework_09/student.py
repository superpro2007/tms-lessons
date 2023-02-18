# 4.1 Создайте файл student.py. Делайте задание в этом файле.
# 4.2 Создайте класс Student, с полями full_name, average_mark (средняя оценка).

class Student:
    def __init__(self, full_name, average_mark):
        self.full_name = full_name
        self.average_mark = average_mark
        
# 4.3 Добавьте в класс метод get_scholarship, который подсчитывает и возвращает стипендию данного студента 
# по следующему алгоритму:
# Если средняя оценка < 6 - вернуть 60 (рублей)
# Если средняя оценка >= 6, но < 8 - вернуть 80 (рублей)
# Если средняя оценка >= 8 - вернуть 100 (рублей)

    def get_scholarship(self):
        if self.average_mark < 6:
            return (60)
        elif self.average_mark >= 6 and self.average_mark < 8:
            return (80)
        elif self.average_mark >= 8:
            return (100)
# 4.4 Добавить в класс метод is_excellent, который возвращает bool:
# True, если средняя оценка >= 9
# False, иначе

    def is_excellent(self):
        return self.average_mark >= 9
        

student = Student('Andrew', 4)
scholarship = student.get_scholarship()
y = student.is_excellent()
print(scholarship)
print(y)

print(Student('Andrew', 4).get_scholarship())