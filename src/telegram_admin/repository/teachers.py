from typing import Optional

from repository.base import TableDB
from src.db.repository.tables.teacher import Teacher

def prepare_data(name, description, photo_url):
    data = {
        "name": name,
        "description": description,
        "photo_url": photo_url
    }
    for key in data:
        if data[key] is None:
            del data[key]
    return data

def create_teacher(name, description=None, photo_url=None):
    data = prepare_data(name, description, photo_url)
    return TableDB(Teacher).create(**data)

def get_teacher(pk) -> Optional[Teacher]:
    return TableDB(Teacher).get(pk)

def get_all_teachers():
    return TableDB(Teacher).get_all()

def is_exist(tg_id):
    return get_teacher(tg_id) is not None

def update_teacher_name(pk, name):
    data = {"name": name}
    updated_obj = TableDB(Teacher).update(pk, **data)
    return updated_obj

def update_teacher_description(pk, description):
    data = {"description": description}
    updated_obj = TableDB(Teacher).update(pk, **data)
    return updated_obj

def update_teacher_photo_url(pk, photo_url):
    data = {"photo_url": photo_url}
    updated_obj = TableDB(Teacher).update(pk, **data)
    return updated_obj

def update_teacher(pk, name=None, description=None, photo_url=None):
    data = prepare_data(name, description, photo_url)
    updated_obj = TableDB(Teacher).update(pk, **data)
    return updated_obj

def delete_teacher(tg_id):
    TableDB(Teacher).delete(tg_id)
