from sqlalchemy import Column, Date, Integer, String

from app.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    student_name = Column(String(100), nullable=False)
    student_dob = Column(Date, nullable=False)
    email = Column(String(150), unique=True, nullable=True)
    phone = Column(String(15), unique=True, nullable=True)
    student_class = Column(String(50), nullable=True)
    student_section = Column(String(20), nullable=True)
