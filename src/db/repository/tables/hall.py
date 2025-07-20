from sqlalchemy import Column, Integer, String, ForeignKey

from src.db.repository.tables.base import Base, CRUDMixin


class Hall(Base, CRUDMixin):
    __tablename__ = 'halls'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    place_id = Column(Integer, ForeignKey("places.id"), nullable=False)
