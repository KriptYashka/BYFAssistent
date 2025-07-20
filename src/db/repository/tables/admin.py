from sqlalchemy import Column, Integer, String, BigInteger

from src.db.repository.tables.base import Base, CRUDMixin


class Admin(Base, CRUDMixin):
    __tablename__ = 'admins'
    tg_id = Column(BigInteger, primary_key=True, nullable=False)

    def __repr__(self):
        return f"<Admin(tg_id: {self.tg_id})>"
