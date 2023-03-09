import sqlite3


class ContactList():
    def __init__(self):
        self._contact_list = dict()

    def add_contact(self, name: str, number: str):
        with sqlite3.connect('db.sqlite') as connection:
            connection.execute("INSERT INTO contact(name, number) "
                               f"VALUES('{name}', '{number}')")

    def show_contacts(self):
        with sqlite3.connect('db.sqlite') as connection:
            result = connection.execute("SELECT name, number FROM contact ORDER BY name")
            for contact in result.fetchall():
                print(f'{contact[0]} - {contact[1]}')

    def update_contact(self, name: str, number: str):
        with sqlite3.connect('db.sqlite') as connection:
            connection.execute(f"Update contact SET number = '{number}' WHERE name = '{name}'")
