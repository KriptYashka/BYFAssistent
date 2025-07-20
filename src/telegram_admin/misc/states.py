from aiogram.fsm.state import StatesGroup, State

class MenuStates(StatesGroup):
    teacher = State()
    place = State()
    hall = State()

class TeacherAddStates(StatesGroup):
    waiting_for_name = State()
    waiting_for_description = State()
    waiting_for_photo_url = State()

class TeacherEditStates(StatesGroup):
    edit_name = State()
    edit_description = State()
    edit_photo = State()
    confirm_delete = State()

class PlaceAddStates(StatesGroup):
    waiting_for_name = State()
    waiting_for_address = State()