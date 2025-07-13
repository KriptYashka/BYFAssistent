from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import re

from repository.users import create_user, update_user, is_exist

router = Router()

class Registration(StatesGroup):
    name = State()
    phone = State()

phone_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Отправить номер", request_contact=True)]],
    resize_keyboard=True,
    one_time_keyboard=True
)

@router.message(Command("register"))
async def start_registration(message: Message, state: FSMContext):
    await message.answer("[Приветствие]. Введите ваше имя:")
    await state.set_state(Registration.name)

@router.message(Registration.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(
        "Пожалуйста, отправьте свой номер телефона, нажав кнопку ниже или введите номер:",
        reply_markup=phone_kb
    )
    await state.set_state(Registration.phone)

@router.message(Registration.phone, F.contact)
async def get_phone_contact(message: Message, state: FSMContext):
    phone = message.contact.phone_number
    data = await state.get_data()
    name = data.get("name")

    await create_and_answer(message, name, phone)
    await state.clear()

async def create_and_answer(message, name, phone):
    tg_id = message.from_user.id
    if not is_exist(tg_id):
        user = create_user(tg_id, name, phone)
        text = f"Спасибо, {name}! Вы успешно зарегистрированы."
    else:
        user = update_user(tg_id, name, phone)
        text = f"Данные обновлены."
    await message.answer(text, reply_markup=None)


@router.message(Registration.phone, F.text)
async def get_phone_text(message: Message, state: FSMContext):
    phone = message.text.strip()
    if not re.match(r"^\+?\d{10,15}$", phone):
        await message.answer("Пожалуйста, введите корректный номер телефона (от 10 до 15 цифр).")
        return

    data = await state.get_data()
    name = data.get("name")

    await create_and_answer(message, name, phone)
    await state.clear()

