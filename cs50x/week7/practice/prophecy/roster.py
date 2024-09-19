import csv
from cs50 import SQL

#open("shows.db", "w").close()
# Open database
db = SQL("sqlite:///new.db")

db.execute("CREATE TABLE students (id INTEGER, student_name TEXT, PRIMARY KEY(id))")
db.execute("CREATE TABLE houses (id INTEGER, house TEXT, head TEXT, PRIMARY KEY(id))")
db.execute("CREATE TABLE relationships (id INTEGER, student_name TEXT, house TEXT, PRIMARY KEY(id))")

def create_houses(house, houses):
    count = 0
    for h in houses:
        if h == house:
            count += 1
    if count == 0:
        houses.append({"house": house, "head": head})

def create_student(name, students):
    students.append({"student_name": name})

def create_relationship(name, house, relationships):
    relationships.append({"student_name": name, "house": house})

students = []
houses = []
relationships = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row['student_name']
        house = row['house']
        head = row['head']

        create_houses(house, houses)
        create_student(name, students)
        create_relationship(name, house, relationships)


for i in range(len(students)):
    db.execute("INSERT INTO students (student_name) VALUES(?)", students[i]['student_name'])
for i in range(len(houses)):
    db.execute("INSERT INTO houses (house, head) VALUES(?, ?)", houses[i]['house'], houses[i]['head'])
for i in range(len(relationships)):
    db.execute("INSERT INTO relationships (student_name, house) VALUES(?, ?)", relationships[i]['student_name'], relationships[i]['house'])

#test
student = 'Vincent Crabbe'
students_names = db.execute("SELECT student_name FROM students")

students = []
for row in students_names:
    name = row['student_name']
    students.append(name)

print(students_names)