from sqlalchemy import func
from sqlalchemy.orm import session
from task_1 import Student, Course

# Задание: Напишите сложные запросы к базе данных
# 1. Получение списка студентов, у которых больше двух курсов
students_with_more_than_two_courses = session.query(
    Student.name, func.count(Course.id).label("num_courses")
).join(Student.courses).group_by(Student.id).having(func.count(Course.id) > 2).all()

for student, num_courses in students_with_more_than_two_courses:
    print(f"{student} - {num_courses} ")

# 2. Получение списка курсов, на которые записано более трех студентов
courses_with_more_than_three_students = session.query(
    Course.name, func.count(Student.id).label("num_students")
).join(Course.student).group_by(Course.id).having(func.count(Student.id) > 3).all()

for course, num_students in courses_with_more_than_three_students:
    print(f"{course} - {num_students}")

# 3. Получение списка студентов, записанных на конкретный курс
course_id = 1
students_on_specific_course = session.query(
    Student.name
).join(Student.courses).filter(Course.id == course_id).all()

for student in students_on_specific_course:
    print(student.name)