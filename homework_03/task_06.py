# Пользователь вводит месяц и число. Выведите True, если такой день есть в году.
months = {
    "january": 31,
    "february": 28,
    "march": 31,
    "april": 30,
    "may": 31,
    "june": 30,
    "july": 31,
    "august": 31,
    "september": 30,
    "october": 31,
    "november": 30,
    "december": 31,
}
month = input("enter month\n")
day = int(input("enter day\n"))
number = months.get(month, False)

if number:
    print(day >= 0 and day <= number)
else:
    print(False)