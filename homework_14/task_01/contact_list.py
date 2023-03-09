import sqlite3


class ContactList():
    def __init__(self):
        self._contact_list = dict()

    def add_contact(self, name: str, number: str):
        with sqlite3.connect('db.sqlite') as connection:
            connection.execute("INSERT INTO contact(name, number) "
                               f"VALUES('{name}', '{number}')")
