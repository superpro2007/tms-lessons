from math import gcd


def lcm(a, b):

    return (a * b) // gcd(a, b)


class Rational:
    def __init__(self, __numerator, __denomenator):
        self.__numerator: int = __numerator
        self.__denomenator: int = __denomenator
        self.__normalize()

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denomenator(self):
        return self.__denomenator

    # 3. Добавьте в класс магически метод __str__, который должен возвращать строку в формате "{nominator} / {denominator}".
    # Теперь вы можете передавать объект Rational в функцию print и он будет напечатан так, как вы определили это.
    def __str__(self) -> str:
        return f"{self.numerator}/{self.denomenator}"

    # 4. Переопределите магические методы умножения и деления. Они должны принимать второй объект типа Rational и возвращать новый объект того же типа.
    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denomenator = self.denomenator * other.denomenator
        return Rational(new_numerator, new_denomenator)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denomenator
        new_denomenator = self.denomenator * other.numerator
        return Rational(new_numerator, new_denomenator)

    # 5. Переопределите магические методы сложения и вычитания.
    def __add__(self, other):
        new_denomenator = lcm(self.denomenator, other.denomenator)
        new_numerator = int(
            self.numerator * new_denomenator / self.denomenator
            + other.numerator * new_denomenator / other.denomenator
        )

        return Rational(new_numerator, new_denomenator)
    
    # 7. Напишите метод __normalise, который ничего не принимает (кроме self), и сокращает дробь. 
    
    def __normalize(self):
        a = gcd(self.numerator, self.denomenator)
        self.__numerator = int(self.numerator / a)
        self.__denomenator = int(self.denomenator / a)
        if self.__denomenator < 0:
            self.__numerator *= -1
            self.__denomenator *= -1
        
        
if __name__ == "__main__":
    rational = Rational(10, 5)
    rational_2 = Rational(2, -10)
    
    print(rational * rational_2)
    print(rational / rational_2)
    print(rational + rational_2)

    rational_3 = Rational (1,4)
    rational_4 = Rational (3,2)
    rational_5 = Rational (1,8)
    rational_6 = Rational (156,100)
    print(rational_3 * (rational_4 + rational_5) + rational_6)
    