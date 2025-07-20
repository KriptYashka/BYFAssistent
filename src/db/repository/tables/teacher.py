from typing import List

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Mapped

from src.db.repository.tables.base import Base, CRUDMixin


class Teacher(Base, CRUDMixin):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String(1000))
    photo_url = Column(String, nullable=True)

    lessons = relationship("src.db.repository.tables.lesson.Lesson", back_populates="teacher")
