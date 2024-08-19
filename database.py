import sqlite3
import hashlib
from pprint import pprint

DB_PATH = "our_db_13052024.sqlite3"

word = "55"
hashed_2 = hashlib.md5(word.encode())
hashed = hashlib.md5(word.encode()).hexdigest()
print(hashed)

with sqlite3.connect(DB_PATH) as connection:
    cursor = connection.cursor()

    # query = """
    #     CREATE TABLE IF NOT EXISTS category(
    #         id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    #         name VARCHAR(20) NOT NULL,
    #         description TEXT,
    #         segment VARCHAR(20)
    #                )
    # """

    # cursor.execute(query)

    # query = """
    # ALTER TABLE category
    # ADD COLUMN segment VARCHAR(20)
    # """
    # cursor.execute(query)

    # do this way
    # name = "kinetic sand"
    # description = "15+"
    # segment = "kid stuff"
    # values = [name, description, segment]
    # query = """
    #     INSERT INTO category(name, description, segment)
    #     VALUES (?, ?, ?)
    # """
    # cursor.execute(query, values)
    # query = """
    #     CREATE TABLE IF NOT EXISTS products(
    #         id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    #         title TEXT NOT NULL UNIQUE,
    #         whole_price DECIMAL(10, 2) CHECK (whole_price > 0),
    #         price DECIMAL(10, 2) CHECK (price >= whole_price),
    #         category_id INTEGER,
    #         FOREIGN KEY (category_id) REFERENCES category(id)
    #     );
    #     CREATE TABLE IF NOT EXISTS products(
    #         id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    #         name TEXT NOT NULL,
    #         login TEXT NOT NULL CHECK (length(login) > 3) UNIQUE,
    #         password TEXT NOT NULL,
    #         address TEXT
    #     )
    # """
    # cursor.executescript(query)
    # name = "Max129"
    # login = "casper18"
    # password = "termos"
    # query = """
    #         INSERT INTO user(name, login, password)
    #         VALUES (?, ?, encode(?))
    #     """
    #
    # cursor.execute(query)

    query = """
        SELECT * , 2+2 as co
        FROM category
    """
    result = cursor.execute(query)
    pprint(result.fetchall(), width=20)
