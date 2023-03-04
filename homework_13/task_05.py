from task_04 import WordIterable


def generate_words(text: str) -> str:
    words = WordIterable.my_split(text)
    for word in words:
        yield word


if __name__ == '__main__':
    text = 'в. понедельник? на работу!'
    for word in generate_words(text):
        print(word)
