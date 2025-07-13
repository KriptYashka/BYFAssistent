import logging
from abc import ABC
from typing import Optional

from sqlalchemy.exc import IntegrityError

from src.db.repository.tables.base import CRUDMixin
from src.db.session import SessionDB

class TableDB:
    def __init__(self, model: type[CRUDMixin]):
        self.Model = model
        self.session = SessionDB()

    def create(self, **data):
        with self.session.get_session() as session:
            try:
                obj = self.Model.create(session, **data)
            except IntegrityError as e:
                logging.error(e)
                return None
            return obj

    def get(self, pk) -> Optional[CRUDMixin]:
        with self.session.get_session() as session:
            obj = self.Model.get(session, pk)
            return obj

    def get_all(self) -> list[CRUDMixin]:
        with self.session.get_session() as session:
            obj = self.Model.get_all(session)
            return obj

    def update(self, pk, **data) -> Optional[CRUDMixin]:
        if not (obj := self.get(pk)):
            return None
        with self.session.get_session() as session:
            obj.update(session, **data)
            return obj

    def delete(self, pk):
        obj = self.get(pk)
        with self.session.get_session() as session:
            if obj:
                obj.delete(session)
