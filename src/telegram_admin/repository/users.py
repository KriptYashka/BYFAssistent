from typing import Optional

from repository.base import TableDB
from src.db.repository.tables.user import User

def is_exist(tg_id):
    return get_user(tg_id) is not None

def create_user(tg_id, name, phone):
    data = {
        "tg_id": tg_id,
        "name": name,
        "phone": phone
    }
    return TableDB(User).create(**data)

def get_user(tg_id) -> Optional[User]:
    return TableDB(User).get(tg_id)

def get_all_users():
    return TableDB(User).get_all()

def update_user(tg_id, name, phone):
    data = {
        "name": name,
        "phone": phone,
    }
    updated_user = TableDB(User).update(tg_id, **data)
    return updated_user

def delete_user(tg_id):
    TableDB(User).delete(tg_id)
