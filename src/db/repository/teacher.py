from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from src.db.repository.base import Base, CRUDMixin

class Teacher(Base, CRUDMixin):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String(1000))
    photo_url = Column(String, nullable=True)

    lessons = relationship("Lesson", back_populates="teacher")
