import sqlite3


def initiate_db():
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER
    )
    ''')
    connection.commit()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')
    connection.commit()
    connection.close()


def add_user(username, email, age):  # Добавим пользователей
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM Users")
    id = cursor.fetchone()[0] + 1
    cursor.execute(f'''
       INSERT INTO Users VALUES('{id}', '{username}', '{email}', '{age}', '1000')
       ''')

    connection.commit()
    connection.close()

def is_included(username):
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()

    us = True
    check_username = cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
    if check_username.fetchone() is None:
        us = False
    return us
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    all_product = cursor.fetchall()
    connection.commit()
    connection.close()
    return all_product


