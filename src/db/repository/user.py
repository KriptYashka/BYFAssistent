from sqlalchemy import Column, Integer, String

from src.db.repository.base import Base, CRUDMixin


class User(Base, CRUDMixin):
    __tablename__ = 'users'
    tg_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(64), nullable=True)
    phone = Column(String(20), unique=True, nullable=True)


    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"
