# Напишите функцию is_palindrome, которая принимает на вход строку,
# и возвращает True если это палиндром, иначе False.


def is_palindrome(stroka_dlia_proverki_palindrom_ili_net: str) -> bool:
    palin = stroka_dlia_proverki_palindrom_ili_net[::-1]
    return stroka_dlia_proverki_palindrom_ili_net == palin


stroka = "wwwww"
stroka2 = "eeeeee2"

print(is_palindrome(stroka))
print(is_palindrome(stroka2))