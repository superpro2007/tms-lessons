# Пользователь вводит название месяца на английском.
# Выведите количество дней в этом месяце (не учитывая високосный год).
# Подсказка: понадобится создать dict: название месяца -> количество дней.

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
print(months[month])
