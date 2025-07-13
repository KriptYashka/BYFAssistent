from sqlalchemy.orm import Session
from sqlalchemy.orm.decl_api import declarative_base

Base = declarative_base()

class CRUDMixin:
    @classmethod
    def create(cls, session: Session, **kwargs):
        obj = cls(**kwargs)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return obj

    @classmethod
    def get(cls, session: Session, pk):
        return session.query(cls).get(pk)

    @classmethod
    def get_all(cls, session: Session):
        return session.query(cls).all()

    def update(self, session: Session, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        session.commit()
        return self

    def delete(self, session: Session):
        session.delete(self)
        session.commit()