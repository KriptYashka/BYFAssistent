from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from filters.common import TextEqualsFilter
from keyboards.common import cancel_or_pass_kb, cancel_kb
from keyboards.navigate import add_or_edit_menu_kb
from misc.states import TeacherAddStates, MenuStates, PlaceAddStates
from routers.manage import router

@router.message(MenuStates.teacher, TextEqualsFilter("Добавить"))
async def add_place_start(message: Message, state: FSMContext):
    await message.answer("Название студии:", reply_markup=cancel_kb)
    await state.set_state(PlaceAddStates.waiting_for_name)

@router.message(PlaceAddStates.waiting_for_name)
async def add_place_start(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Адрес студии:", reply_markup=cancel_kb)
    await state.set_state(PlaceAddStates.waiting_for_address)

@router.message(PlaceAddStates.waiting_for_address)
async def add_place_start(message: Message, state: FSMContext):
    address = message.text
    name = await state.get_value("name")
    # TODO: Handler place add
    await state.clear()
    text = f"Студия '{name}' зарегистрирована по адресу: {address}"
    await message.answer(text, reply_markup=add_or_edit_menu_kb)