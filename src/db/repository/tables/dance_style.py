from sqlalchemy import Column, Integer, String

from repository.tables.base import Base, CRUDMixin


class DanceStyle(Base, CRUDMixin):
    __tablename__ = 'styles'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
