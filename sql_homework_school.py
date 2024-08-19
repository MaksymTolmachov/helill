import sqlite3

DB_PATH = "our_db_homework_school_.sqlite3"

with sqlite3.connect(DB_PATH) as connection:
    cursor = connection.cursor()

    query1 = """
    CREATE TABLE IF NOT EXISTS schools(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        number_of_this_school VARCHAR(20),
        address TEXT,
        number_of_floors INTEGER CHECK (number_of_floors > 1)  NOT NULL
                )
    """
    cursor.execute(query1)

    query2 = """
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
        name VARCHAR(20),
        surname VARCHAR(20),
        specialization TEXT,
        schools INTEGER,
        FOREIGN KEY (schools) REFERENCES schools(number_of_this_school)
                )
    """
    cursor.execute(query2)
    # number_of_this_school = "664"
    # address = "Kharkiv"
    # number_of_floors = "3"
    # values = [number_of_this_school, address, number_of_floors]
    # query3w = """
    #     INSERT INTO schools(number_of_this_school, address, number_of_floors )
    #     VALUES (?, ?, ?)
    # """
    # cursor.execute(query3w, values)

    # number_of_this_school = "591"
    # address = "Kyiv"
    # number_of_floors = "3"
    # values = [number_of_this_school, address, number_of_floors]
    # query4w = """
    #         INSERT INTO schools(number_of_this_school, address, number_of_floors )
    #         VALUES (?, ?, ?)
    #     """
    # cursor.execute(query4w, values)
    # number_of_this_school = "112"
    # address = "Odesa"
    # number_of_floors = "2"
    # values = [number_of_this_school, address, number_of_floors]
    # query5w = """
    #             INSERT INTO schools(number_of_this_school, address, number_of_floors )
    #             VALUES (?, ?, ?)
    #         """
    # cursor.execute(query5w, values)
    name = "Dima"
    surname = "kovalchuk"
    specialization = "PE"
    schools = "664"
    values = [name, surname, specialization, schools]
    query10w = """
        INSERT INTO students(name, surname, specialization, schools)
        VALUES (?, ?, ?, ?)      
    """
    cursor.execute(query10w, values)


