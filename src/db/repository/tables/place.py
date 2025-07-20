from sqlalchemy import Column, Integer, String

from src.db.repository.tables.base import Base, CRUDMixin


class Place(Base, CRUDMixin):
    __tablename__ = 'places'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=True)
    address = Column(String(128), nullable=False)
