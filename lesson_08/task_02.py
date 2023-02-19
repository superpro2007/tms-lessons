# from homework_05.task_07 import generate_natural_cubes
# print(generate_natural_cubes(3))

# Создайте словарь с вашими данными (имя, фамилия, и т.д), запишите его в файл file_03.json в формате JSON.
# import json
# data = {'name' : 'Yauhen', 'surname' : 'Zhur'}
# with open ('file_03.json', 'w') as file:
#     json.dump(data,file)


# import json

# data = {'name' : input('name'), 'surname' : input('surname'), 'age' : input('age')}
# with open ('file_04.json', 'w') as file:
#     json.dump(data,file)

# Запишите свои данные в файл file_06.csv в формате CSV. 
# Пример:
# name,surname,gender
# Dmitry,Buevich,M

import csv
header = ('name', 'surname', 'gender')
student = ('Yauhen', 'Zhur', 'man')
with open ('file_06.csv', 'w') as file:
    writer = csv.writer(file, delimiter = ',')
    writer.writerow(header)
    for me in student:
        writer.writerow(me)
