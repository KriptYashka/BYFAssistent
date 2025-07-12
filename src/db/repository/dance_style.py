from sqlalchemy import Column, Integer, String

from src.db.repository.base import Base, CRUDMixin


class DanceStyle(Base, CRUDMixin):
    __tablename__ = 'styles'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))


    def __repr__(self):
        return f""
