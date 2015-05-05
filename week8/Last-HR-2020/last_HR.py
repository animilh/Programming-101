import requests
import sqlite3
import json

url = 'https://hackbulgaria.com/api/students/'
content = requests.get(url).json()

students =[(str(user['name']), str(user['github'])) for user in content]

students_courses = {user['name'] : user['courses'] for user in content}

courses = set()

for key in students_courses.keys():
    for i in range(len(students_courses[key])):
        courses.add(students_courses[key][i]['name'])


connection = sqlite3.connect("lasthr.db")
cursor = connection.cursor()


insert_students = """
    INSERT INTO Students (student_name, github) values (?, ?)
"""
cursor.executemany(insert_students, students)

insert_courses = """
    INSERT INTO Courses (course_name) values ('Frontend JavaScript');
    INSERT INTO Courses (course_name) values ('Angular JS');
    INSERT INTO Courses (course_name) values ('Програмиране 0');
    INSERT INTO Courses (course_name) values ('Core Java v2');
    INSERT INTO Courses (course_name) values ('Frontend JavaScript v2');
    INSERT INTO Courses (course_name) values ('Programming 101  v2');
    INSERT INTO Courses (course_name) values ('NodeJS');
    INSERT INTO Courses (course_name) values ('Programming 101 v3');
    INSERT INTO Courses (course_name) values ('Ruby on Rails');
    INSERT INTO Courses (course_name) values ('Core Java');
    INSERT INTO Courses (course_name) values ('System C');
    INSERT INTO Courses (course_name) values ('Android');
    INSERT INTO Courses (course_name) values ('Core Ruby');
"""
cursor.executescript(insert_courses)

# insert_courses = """ INSERT INTO Courses(
# course_name) VALUES(?, )"""

# cursor.executemany(insert_courses, (courses, ))

connection.commit()

def id_student (cursor, connection, name):
    connection = sqlite3.connect("lasthr.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    result = cursor.execute("""
        SELECT id_student FROM Students WHERE student_name = '%s'
        """ % name)
    row = result.fetchone()
    return row['id_student']

def id_course(cursor, connection, name):
    connection = sqlite3.connect("lasthr.db")
    connection.row_factory = sqlite3.Row
    cursor =connection.cursor()
    result = cursor.execute("""
        SELECT id_courses FROM Courses WHERE course_name = '%s'
        """ % name)
    row = result.fetchone()
    return row['id_courses']

students_to_courses = []
for key in students_courses.keys():
    for i in range(len(students_courses[key])):
        students_to_courses.append((id_student(cursor, connection, key), id_course(cursor, connection, students_courses[key][i]['name'])))

insert_students_courses = """
    INSERT INTO Students_to_courses(id_student, id_courses) values (?, ?)
"""
cursor.executemany(insert_students_courses, students_to_courses)

connection.commit()
