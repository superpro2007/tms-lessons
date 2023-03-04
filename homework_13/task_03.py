class WordIterable:
    def __init__(self, text: str) -> None:
        self.text = text

    def __iter__(self):
        self.words = text.split()
        self.index = 0
        return self

    def __next__(self):
        self.index += 1
        if self.index > len(self.words):
            raise StopIteration()
        return self.words[self.index - 1]


if __name__ == '__main__':
    text = 'в понедельник на работу'
    for word in WordIterable(text):
        print(word)
