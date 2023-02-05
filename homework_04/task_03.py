# Сделайте предыдущую задачу, добавив проверку на корректность ответа пользователя.
# Если он ответил “yes” - завершите программу.
# Если он ответил “no” - продолжайте - продолжайте вывод чисел.
# Если что-то другое - напечатайте "Don't understand you" и продолжайте спрашивать до тех пор,
# пока ответ не будет корректным.


for number in range(101):
    print(number)
    while True:
        n = input("should we break\n")
        if n == "no" or n == "yes":
            break
        else:
            print("Dont understand you")
    if n == 'yes':
        break