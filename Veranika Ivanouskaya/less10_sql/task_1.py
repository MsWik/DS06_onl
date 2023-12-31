from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    #один ко многим
    courses = relationship("Course", back_populates="student")

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    student_id = Column(Integer, ForeignKey('students.id'))
    #многие к одному
    student = relationship("Student", back_populates="courses")

# Задание: Допишите отношения между Student и Course