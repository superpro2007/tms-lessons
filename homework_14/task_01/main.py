from contact_list import ContactList

if __name__ == '__main__':
    contact_list = ContactList()
    while True:
        command = input('\n0. Выйти из программы\n'
                        '1. Добавить новый контакт\n'
                        '2. Вывести весь список контактов в алфавитном порядке\n'
                        '3. Обновить номер контакта\n\n')
        if command == '0':
            break
        elif command == '1':
            name = input('input name\n')
            number = input('input number\n')
            contact_list.add_contact(name, number)
            print('contact added\n')

        elif command == '2':
            contact_list.show_contacts()


        elif command == '3':
            name = input('input name\n')
            number = input('input number\n')
            contact_list.update_contact(name, number)
            print('contact updated')
