from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    tg_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(64), nullable=True)
    phone = Column(String(20), unique=True, nullable=True)


    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"
