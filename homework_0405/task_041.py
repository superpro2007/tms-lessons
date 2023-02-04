# Вывести на экран числа кратные 5 от 0 до 100 включительно. 
# Сделать это с помощью функции range с шагом 5
# Сделать это с помощью функции range c шагом 1 и вложенным if

for number in range(0,101,5):
    print(number)
    
for number in range(101):
    if number %5 ==0:
        print(number)       
    
