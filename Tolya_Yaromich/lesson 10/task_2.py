from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Создаем соединение к базе данных
engine = create_engine('sqlite:///:memory:', echo=True)

# Создаем сессию
Session = sessionmaker(bind=engine)
session = Session()

# Создаем базовый класс моделей
Base = declarative_base()

# Определяем модель для студентов
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    course_id = Column(Integer, ForeignKey('courses.id'))

# Определяем модель для курсов
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)

# Создаем таблицы в базе данных
Base.metadata.create_all(engine)

# Выполняем запросы

# 1. Добавление студента в базу данных
new_student = Student(first_name='Иван', last_name='Иванов')
session.add(new_student)
session.commit()

# 2. Добавление курса в базу данных
new_course = Course(name='Математика')
session.add(new_course)
session.commit()

# 3. Привязка студента к курсу
new_student.course_id = new_course.id
session.commit()

# 4. Получение списка всех студентов
all_students = session.query(Student).all()
for student in all_students:
    print(f"Студент: {student.first_name} {student.last_name}")

# 5. Получение списка всех курсов для конкретного студента
student_name = 'Иван Иванов'
student_courses = session.query(Course).join(Student).filter(Student.first_name == student_name.split()[0], Student.last_name == student_name.split()[1]).all()
for course in student_courses:
    print(f"Студент {student_name} записан на курс: {course.name}")