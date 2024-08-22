import sqlite3
from pprint import pprint

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
    # name = "Dima"
    # surname = "Kovaluk"
    # specialization = "Pe"
    # schools = "664"
    # values = [name, surname, specialization, schools]
    # query1w = """
    #     INSERT INTO students(name, surname, specialization, schools)
    #     VALUES (?, ?, ?, ?)
    # """
    # cursor.execute(query1w, values)

    # HOMWORK NUMBER TWO

    query = """
        SELECT students.name, students.surname, students.schools, students.specialization
        FROM students
        LEFT JOIN schools
        ON students.schools = schools.number_of_this_school

    """
    result1 = cursor.execute(query)
    pprint(result1.fetchall(), width=80)

    # query_add_column = """
    #     ALTER TABLE students
    #     ADD COLUMN phone_number VARCHAR(20)
    # """
    # cursor.execute(query_add_column)

    query_update = """
        UPDATE students
        SET 
            phone_number = "38099659418"
        WHERE id = 5    
    """
    cursor.execute(query_update)

    query_delete = """
        DELETE FROM students
        WHERE id BETWEEN 2 AND 4
    """

    cursor.execute(query_delete)

    query_hw = """
            SELECT students.id, students.name, students.surname, students.schools, students.specialization
            FROM students
            ORDER BY id DESC 
            LIMIT 3
            OFFSET 2
            
        """

    result = cursor.execute(query_hw)
    pprint(result.fetchall(), width=80)




