import sqlite3

connection = sqlite3.connect("lasthr.db")
cursor = connection.cursor()

create_students_table = """
CREATE TABLE IF NOT EXISTS
Students(id_student INTEGER PRIMARY KEY, student_name TEXT, github TEXT);
"""

create_courses_table = """
CREATE TABLE IF NOT EXISTS
Courses(id_courses INTEGER PRIMARY KEY, course_name TEXT)
"""

create_students_to_courses_table = """
CREATE TABLE IF NOT EXISTS
Students_to_courses(id_student INTEGER, id_courses INTEGER,
    FOREIGN KEY (id_student) REFERENCES Students,
    FOREIGN KEY (id_courses) REFERENCES Courses
    )
"""

tables_to_create = [create_students_table, create_courses_table, create_students_to_courses_table]

for table in tables_to_create:
    cursor.execute(table)

connection.commit()
