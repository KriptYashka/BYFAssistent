import enum

from sqlalchemy import Column, Integer, Float, Boolean
from sqlalchemy.dialects.postgresql import ENUM

from repository.tables.base import Base, CRUDMixin


class SubscriptionType(enum.Enum):
    PROMO = "Пробное занятие"
    SINGLE = "Разовый"
    BASE = "Базовый"
    OPTIMAL = "Оптимальный"
    EXTENDED = "Расширенный"


class Price(Base, CRUDMixin):
    __tablename__ = 'prices'
    id = Column(Integer, primary_key=True)
    subscription_type = Column(ENUM(SubscriptionType, name="sub_enum", create_type=True))
    count = Column(Integer, nullable=True)
    lesson_duration = Column(Float, nullable=True)
    subscription_duration = Column(Integer, nullable=True)
    is_preferential = Column(Boolean, default=False)
    price = Column(Integer)

