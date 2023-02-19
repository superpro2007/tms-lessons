# Задача 5. Инкапсуляция
# 5.1 Скопируйте класс из предыдущего задания.
# 5.2 Давайте теперь хранить пароль в зашифрованном виде. Создайте новое поле __key = random.randint(1, 1000)
import random
class User:
    def __init__(self, login, __password):
        self.login = login
        self.__password = __password
        self.__key = random.randint(1, 1000)
        
# 5.3 Добавьте приватный метод __encode, шифрующий строку: def __encode(self, s):

        
    


