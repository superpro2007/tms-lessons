import random
import json
import os

# 1. Создайте функцию get_random_digits, которое принимает целое число count (количество цифр),
# и возвращает строку, сгенерированную из count рандомных цифр от нуля до девяти


def get_random_digits(count: int) -> str:
    result = ""
    for _ in range(count):
        result = result + str(random.randint(0, 9))
    return result


# Создайте класс BankAccount
# Создайте в классе конструктор, который принимает одно значение: card_holder (строка с именем держателя карты).
# В конструкторе должны создаваться следующие поля:
# card_holder - поле равное аргументу конструктора card_holder, но в верхнем регистре (исп. функцию upper).
# money - количество денег на счету. Выставьте в 0 (счёт только открыли, на нём пока нет денег).
# account_number - номер счёта, строка из 20 рандомных чисел.
# card_number - номер карты, строка из 16 рандомных чисел.


class BankAccount:
    def __init__(
        self, card_holder: str, money=0, account_number=None, card_number=None
    ) -> None:
        self.card_holder = card_holder.upper()
        self.money = money
        if account_number is None:
            self.account_number = get_random_digits(20)
        else:
            self.account_number = account_number

        if card_number is None:
            self.card_number = get_random_digits(16)
        else:
            self.card_number = card_number

    # 4. СЕРИАЛИЗАЦИЯ ДАННЫХ. 4.1. Создайте функцию convert_bank_account_to_dict, которая принимает объект класса BankAccount,
    # и возвращает dict, в котором будут все данные этого счёта.
    def convert_to_dict(self):
        return {
            "card_holder": self.card_holder,
            "money": self.money,
            "card_number": self.card_number,
            "account_number": self.account_number,
        }


# 1.1 Создайте класс Bank.
class Bank:
    # 1.2 Добавьте в класс конструктор без аргументов. Создайте в конструкторе поле bank_accounts c
    # типом dict[str, BankAccount] (словарь, где ключом является номер счёта, а значением - объект BankAccount).
    # # Изначально данное поле - пустой словарь.
    def __init__(self) -> None:
        self.__bank_accounts: dict[str, BankAccount] = dict()
        self.load_accounts()
        
    # 1.3 Добавьте метод open_account:Метод принимает один аргумент - card_holder
    # Создаёт новый банковский счёт и сохраняет его в поле bank_accounts
    # Возвращает (return) созданный счёт.
    def open_account(self, card_holder: str) -> str:
        account = BankAccount(card_holder)
        self.__bank_accounts[account.account_number] = account
        return account.account_number

    # 1.4 Добавьте метод add_money:
    # Метод принимает два аргумента: account_number и money
    # Находит счёт в поле bank_accounts и прибавляет к деньгам на счету соответствующее количество денег (money).

    def add_money(self, account_number: str, money: int) -> None:
        account: BankAccount = self.__bank_accounts[account_number]
        account.money = account.money + money
        self.__bank_accounts[account.account_number] = account
        self.save_accounts()

    # 1.5 Добавьте метод transfer_money:
    # Метод принимает три аргумента:  from_account_number (номер счёта-отправителя),
    # to_account_number (номер счёта-получателя), money. Снимает деньги со счёта-отправителя.
    # Добавляет деньги на счёт-получателя.
    def transfer_money(
        self, from_account_number: str, to_account_number: str, money: int
    ) -> None:
        from_account: BankAccount = self.__bank_accounts[from_account_number]
        to_account: BankAccount = self.__bank_accounts[to_account_number]
        from_account.money = from_account.money - money
        to_account.money = to_account.money + money
        self.__bank_accounts[from_account.account_number] = from_account
        self.__bank_accounts[to_account.account_number] = to_account
        self.save_accounts()

    # 1.6 Добавьте метод external_transfer:
    # Метод принимает три аргумента: from_account_number (номер счёта-отправителя), to_external_number (внешний номер счёта-получателя), money.
    # Снимает деньги со счёта-отправител. Мы не настоящий банк, поэтому просто пишем в консоль
    # "Банк перевёл xxx$ с вашего счёта XXXX на внешний счёт YYYY"
    def external_transfer(
        self, from_account_number: str, to_external_number: str, money: int
    ):
        self.add_money(from_account_number, money * -1)
        print(
            f"Банк перевёл {money} с вашего счёта {from_account_number} на внешний счёт {to_external_number}"
        )
        self.save_accounts()

    def __str__(self) -> str:
        result = ""

        for account_number in self.__bank_accounts:
            result = (
                result
                + account_number
                + " - "
                + str(self.__bank_accounts[account_number].money)
                + "\n"
            )

        return result

    # 4.4.2 Создайте функцию save_accounts, которая принимает данные об акаунтах из банка (то есть dict[str, BankAccount]),
    # а также строку file_name (название файла), и сохраняет все данные в файл.
    def save_accounts(self, file_name: str = "data.json"):
        accounts = []

        for account_number in self.__bank_accounts:
            account = self.__bank_accounts[account_number]
            accounts.append(account.convert_to_dict())

        with open(file_name, "w") as file:
            json.dump(accounts, file)

    # 4.4.4 Создайте функцию load_accounts, которая принимает аргумент file_name (название файла)
    # и возвращает dict[str, BankAccount], загруженный из файла с помощью библиотеки json.
    def load_accounts(self, file_name: str = "data.json") -> dict[str, BankAccount]:
        if os.path.exists(file_name) == False:
            return {}
            
        with open(file_name, "r") as file:
            accounts = json.load(file)
            for account in accounts:
                bank_account = BankAccount(
                    account["card_holder"],
                    account["money"],
                    account["card_number"],
                    account["account_number"],
                )
                self.__bank_accounts[bank_account.account_number] = bank_account


# 2.1 Создайте класс Controller
# Добавьте в класс конструктор без аргументов. В конструкторе должно создаваться одно поле bank (объект класса Bank).
class Controller:
    def __init__(self):
        self.__bank = Bank()

    # 2.2 Добавьте в класс метод run, который пока будет просто выводить на экран "Здравствуйте, наш банк открылся!"
    def run(self):
        print("Здравствуйте, наш банк открылся")

        # 2.5 Добавьте в метод run бесконечный цикл (while True), который на каждой итерации выводит следующий текст:

        while True:
            print("0. Завершить программу")
            print("1. Открыть новый счёт")
            print("2. Просмотреть открытые счета")
            print("3. Положить деньги на счёт")
            print("4. Перевести деньги между счетами")
            print("5. Совершить платёж")

            user_input = int(input())

            if user_input == 0:
                print("До свидания")
                break

            elif user_input == 1:
                fio = input("ФИО")
                account_number = self.__bank.open_account(fio)
                print("Счет {} создан".format(account_number))

            elif user_input == 2:
                print(self.__bank)

            elif user_input == 3:
                self.add_money()

            elif user_input == 4:
                self.transfer_money()

            elif user_input == 5:
                self.transfer_external()

    def transfer_external(self):
        a = input("vvedite schet otpravitelya")
        b = input("vvedite vneshnii schet")
        c = input("vvedite symmu perevoda")
        self.__bank.external_transfer(a, b, c)
        print("perevod yspeh")

    def transfer_money(self):
        a = input("vvedite vash schet")
        b = input("vvedite schet kyda perevodit money")
        c = int(input("skoljo deneg perevesti"))
        self.__bank.transfer_money(a, b, c)
        print("yspeshnii perevod")

    def add_money(self):
        a = int(input("dobavte money"))
        b = input("vvedite nomer scheta")
        self.__bank.add_money(b, a)
        print("yspeh")


# if __name__ == "__main__":
#     alfabank = Bank()
#     moi_acc = alfabank.open_account("Yauheni")
#     tvoi_acc = alfabank.open_account("Andrei")
#     alfabank.add_money(moi_acc, 100)
#     alfabank.add_money(tvoi_acc, 50)
#     alfabank.transfer_money(moi_acc, tvoi_acc, 30)
#     alfabank.external_transfer(moi_acc, "gaben", 50)
#     print("Koniec")
if __name__ == "__main__":
    controller = Controller()
    controller.run()
