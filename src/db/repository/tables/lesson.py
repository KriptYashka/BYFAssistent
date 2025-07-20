from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.db.repository.tables.base import Base, CRUDMixin

class Lesson(Base, CRUDMixin):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)
    dance_type_id = Column(Integer, ForeignKey('styles.id'), nullable=True)
    experience_type = Column(String(64))

    teacher = relationship("src.db.repository.tables.teacher.Teacher", back_populates="lessons")
    # timeslots = relationship("src.db.repository.tables.timeslot.Timeslot", back_populates="lesson", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Lesson(id={self.id}, dance_type='{self.dance_type}', teacher_id={self.teacher_id})>"
