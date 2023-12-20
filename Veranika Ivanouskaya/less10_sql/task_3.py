# Задание: Напишите код для обновления следующих данных

# 1. Изменение имени студента
student = session.query(Student).filter(Student.id == student_id).first()
student.name = new_name
session.commit()

# 2. Изменение названия курса
course = session.query(Course).filter(Course.id == course_id).first()
course.name = new_course_name
session.commit()

# 3. Удаление студента из базы данных
student = session.query(Student).filter(Student.id == student_id).first()
session.delete(student)
session.commit()

# 4. Удаление курса из базы данных
course = session.query(Course).filter(Course.id == course_id).first()
session.delete(course)
session.commit()