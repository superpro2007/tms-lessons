import sqlite3


with sqlite3.connect('db.sqlite') as connection:
    users = connection.execute('select * from user;')
    for user in users.fetchall():
        print(user)