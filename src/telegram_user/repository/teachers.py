import logging
from typing import Optional

from sqlalchemy.exc import IntegrityError

from src.db.session import SessionDB
from src.db.repository.tables.user import User


def create_teacher(name, description=None, photo_url=None):
    data = {
        "name": name,
        "description": description,
        "photo_url": photo_url
    }
    with SessionDB().get_session() as session:
        try:
            user = User.create(session, **data)
        except IntegrityError as e:
            logging.error(e)
            return None
        return user

def get_user(tg_id) -> Optional[User]:
    with SessionDB().get_session() as session:
        user = User.get(session, tg_id)
        return user

def get_all_users():
    with SessionDB().get_session() as session:
        user = User.get_all(session)
        return user

def update_user(tg_id, name, phone):
    with SessionDB().get_session() as session:
        if not (user := get_user(tg_id)):
            return None
        data = {
            "name": name,
            "phone": phone,
        }
        updated_user = user.update(session, **data)
        return updated_user

def delete_user(tg_id):
    with SessionDB().get_session() as session:
        user = get_user(tg_id)
        if user:
            user.delete(session)