# Пользователь вводит число, выведите True если оно простое, иначе False.

num = int(input("Enter a number: "))
is_prime_number = True

if num == 1:
    print(False)
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            is_prime_number = False
            break

print(is_prime_number)
