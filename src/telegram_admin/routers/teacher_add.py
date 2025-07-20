from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from filters.common import TextEqualsFilter
from handlers.teachers import create_teacher
from keyboards.common import cancel_or_pass_kb, cancel_kb
from keyboards.navigate import add_or_edit_menu_kb
from misc.states import TeacherAddStates, MenuStates
from routers.manage import router

@router.message(MenuStates.teacher, TextEqualsFilter("Добавить"))
async def add_teacher_start(message: Message, state: FSMContext):
    await message.answer("Введите имя преподавателя или нажмите Отмена:", reply_markup=cancel_kb)
    await state.set_state(TeacherAddStates.waiting_for_name)

@router.message(TeacherAddStates.waiting_for_name)
async def add_teacher_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите описание преподавателя (можно пропустить):", reply_markup=cancel_or_pass_kb)
    await state.set_state(TeacherAddStates.waiting_for_description)


@router.message(TeacherAddStates.waiting_for_description)
async def add_teacher_description(message: Message, state: FSMContext):
    if message.text.lower() == "пропустить":
        message.text = None

    description = message.text if message.text.strip() else None
    await state.update_data(description=description)
    await message.answer("Введите ссылку на фото преподавателя (можно пропустить):", reply_markup=cancel_or_pass_kb)
    await state.set_state(TeacherAddStates.waiting_for_photo_url)


@router.message(TeacherAddStates.waiting_for_photo_url)
async def add_teacher_photo(message: Message, state: FSMContext):
    if message.text.lower() == "пропустить":
        message.text = None

    photo_url = message.text if message.text.strip() else None
    data = await state.get_data()
    name = data.get("name")
    description = data.get("description")

    teacher = create_teacher(name=name, description=description, photo_url=photo_url)

    if teacher:
        await message.answer(f"Преподаватель '{name}' успешно добавлен!", reply_markup=add_or_edit_menu_kb)
    else:
        await message.answer("Ошибка при добавлении преподавателя. Попробуйте ещё раз.", reply_markup=add_or_edit_menu_kb)

    await state.clear()

