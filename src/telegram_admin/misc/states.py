from aiogram.fsm.state import StatesGroup, State


class AddTeacher(StatesGroup):
    waiting_for_name = State()
    waiting_for_description = State()
    waiting_for_photo_url = State()
