from sqlalchemy import Column, Integer, String

from repository.tables.base import Base, CRUDMixin


class Place(Base, CRUDMixin):
    __tablename__ = 'places'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=True)
    address = Column(String(128), nullable=False)


    def __repr__(self):
        return f""
