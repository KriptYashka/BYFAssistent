import enum

from sqlalchemy import Column, Integer, ForeignKey, Time
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ENUM
from repository.tables.base import Base

from repository.tables.hall import Hall
from repository.tables.lesson import Lesson


class Week(enum.Enum):
    MONDAY = "Понедельник"
    TUESDAY = "Вторник"
    WEDNESDAY = "Среда"
    THURSDAY = "Четверг"
    FRIDAY = "Пятница"
    SATURDAY = "Суббота"
    SUNDAY = "Воскресенье"

class Timeslot(Base):
    __tablename__ = 'timeslots'

    id = Column(Integer, primary_key=True)
    start = Column(Time, nullable=False)
    end = Column(Time, nullable=False)
    week = Column(ENUM(Week, name="week_enum", create_type=True), nullable=False)
    hall_id = Column(Integer, ForeignKey('halls.id'), nullable=True)
    lesson_id = Column(Integer, ForeignKey('lessons.id'), nullable=False)

    hall = relationship("Hall", back_populates="timeslots")
    lesson = relationship("Lesson", back_populates="timeslots")
