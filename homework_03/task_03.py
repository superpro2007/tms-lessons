# Пользователь вводит два числа: x, y, где x - сумма рублей, 
# которую он кладёт на депозит под 10% годовых,y - количество лет. 
# Каждый год вклад увеличивает на 10%. Эти деньги прибавляются к сумме 
# вклада, и на них в следующем году тоже будут проценты
# Вывести конечную сумму на счету по прошествии y лет.

sum_rub = int(input('Enter sum\n'))
years_num = int(input('Enter years\n'))

for year in range(1, years_num + 1):
    sum_rub = sum_rub * 1.1
   
print(int(sum_rub))