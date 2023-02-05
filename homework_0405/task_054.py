# Напишите функцию get_longest_word, которая на вход принимает текст (только английские слова и пробелы),
# и возвращает самое длинное слово из этого текста.
# Для разбиения строки на слова используйте функцию split.


def get_longest_word(text: str) -> str:
    dlinnoe_word = ""
    slova = text.split()
    for slovo in slova:
        if len(slovo) > len(dlinnoe_word):
            dlinnoe_word = slovo
    return dlinnoe_word


print(get_longest_word("kak eto poniat"))
