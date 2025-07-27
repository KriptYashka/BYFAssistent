from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from filters.common import TextEqualsFilter
from keyboards.navigate import main_menu_kb, manage_menu_kb, manage_other_menu_kb, add_or_edit_menu_kb, \
    add_or_delete_menu_kb
from misc.states import MenuStates

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Выберите действие:", reply_markup=main_menu_kb)

@router.message(TextEqualsFilter("Назад"))
async def back_to_previous_menu(message: Message, state: FSMContext):
    """
    Вызов функции вне зависимости от места
    """
    current_state = await state.get_state()
    if current_state:
        await state.clear()
    await message.answer("Выберите действие:", reply_markup=main_menu_kb)

@router.message(TextEqualsFilter("Управление"))
async def management_menu(message: Message):
    await message.answer("Выберите раздел управления:", reply_markup=manage_menu_kb)

@router.message(TextEqualsFilter("Прочее"))
async def misc_menu(message: Message):
    await message.answer("Выберите пункт:", reply_markup=manage_other_menu_kb)

@router.message(TextEqualsFilter("Преподаватели"))
async def teachers_menu(message: Message, state: FSMContext):
    await state.set_state(MenuStates.teacher)
    await message.answer("Выберите действие с преподавателями:", reply_markup=add_or_edit_menu_kb)

@router.message(TextEqualsFilter("Студии"))
async def places_menu(message: Message, state: FSMContext):
    await state.set_state(MenuStates.place)
    await message.answer("Выберите действие со студиями:", reply_markup=add_or_delete_menu_kb)

@router.message(TextEqualsFilter("Залы"))
async def halls_menu(message: Message, state: FSMContext):
    await state.set_state(MenuStates.hall)
    await message.answer("Выберите действие с залами:", reply_markup=add_or_delete_menu_kb)