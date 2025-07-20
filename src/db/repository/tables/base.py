from sqlalchemy.orm import Session
from sqlalchemy.orm.decl_api import declarative_base

Base = declarative_base()

class CRUDMixin:
    @classmethod
    def create(cls, session: Session, **kwargs):
        """
        Создаёт объект в БД. Возвращает объект.
        """
        obj = cls(**kwargs)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return obj

    @classmethod
    def get(cls, session: Session, pk):
        """
        Возвращает объекты модели по primary key.
        """
        return session.query(cls).get(pk)

    @classmethod
    def get_all(cls, session: Session):
        """
        Возвращает все объекты модели, отсортированные по primary key.
        """
        pk = list(cls.__mapper__.primary_key)[0]
        return session.query(cls).order_by(pk).all()

    def update(self, session: Session, **kwargs):
        """
        Обновляет поля объекта в БД. Возвращает обновлённый объект.

        Если поле None, то он обновится на Null.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)
        session.add(self)
        session.commit()
        return self

    def delete(self, session: Session):
        """
        Удаляет объект из БД.
        """
        session.delete(self)
        session.commit()