# Напишите функцию get_most_frequent_word, которая на вход принимает текст(только английские слова и пробелы),
# и возвращает самое часто встречающееся слово. Если таких слов несколько - верните любое.
def get_most_frequent_word(text: str) -> str:
    most_frequent_word = str()
    words = text.split()
    kolichestvo_slov = dict()

    for slovo in words:
        if slovo in kolichestvo_slov:
            kolichestvo_slov[slovo] += 1
        else:
            kolichestvo_slov[slovo] = 1

    for slovo in kolichestvo_slov:
        if kolichestvo_slov[slovo] > kolichestvo_slov.get(most_frequent_word, 0):
            most_frequent_word = slovo

    print(kolichestvo_slov)
    return most_frequent_word


print(get_most_frequent_word("idi na hui hui hui na na na na hui"))
