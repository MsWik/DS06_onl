from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from task_1 import Student, Course

# Создаем соединение к базе данных
engine = create_engine('sqlite:///:memory:', echo=True)

# Создаем сессию
Session = sessionmaker(bind=engine)
session = Session()

# 1. Добавление студента в базу данных
new_student = Student(name='Veronika Iv')
session.add(new_student)
session.commit()

# 2. Добавление курса в базу данных
new_course = Course(name='Matematika')
session.add(new_course)
session.commit()

# 3. Привязка студента к курсу
new_course.student_id = new_student.id
session.commit()

# 4. Получение списка всех студентов
students = session.query(Student).all()

# 5. Получение списка всех курсов для конкретного студента
student_id = 1
student = session.query(Student).filter(Student.id == student_id).first()