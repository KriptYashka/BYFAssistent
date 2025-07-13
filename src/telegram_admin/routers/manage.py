from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command, Filter
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from repository.teachers import create_teacher

router = Router()

# --- FSM для добавления преподавателя ---
class AddTeacher(StatesGroup):
    waiting_for_name = State()
    waiting_for_description = State()
    waiting_for_photo_url = State()

# --- Клавиатуры ---
main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Заявки"), KeyboardButton(text="Управление")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

management_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Группы"), KeyboardButton(text="Расписание")],
        [KeyboardButton(text="Прочее")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

misc_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Преподаватели"), KeyboardButton(text="Студии")],
        [KeyboardButton(text="Залы")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

teachers_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Добавить"), KeyboardButton(text="Редактировать")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

cancel_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Пропустить")],
        [KeyboardButton(text="Отмена")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

# --- Хендлеры ---


class TextEqualsFilter(Filter):
    def __init__(self, text: str):
        self.text = text.lower()

    async def __call__(self, message: Message) -> bool:
        return message.text and message.text.lower() == self.text

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Выберите действие:", reply_markup=main_menu_kb)


@router.message(TextEqualsFilter("Управление"))
async def management_menu(message: Message):
    await message.answer("Выберите раздел управления:", reply_markup=management_menu_kb)

@router.message(TextEqualsFilter("Прочее"))
async def misc_menu(message: Message):
    await message.answer("Выберите пункт:", reply_markup=misc_menu_kb)

@router.message(TextEqualsFilter("Преподаватели"))
async def teachers_menu(message: Message):
    await message.answer("Выберите действие с преподавателями:", reply_markup=teachers_menu_kb)

@router.message(TextEqualsFilter("Добавить"))
async def add_teacher_start(message: Message, state: FSMContext):
    await message.answer("Введите имя преподавателя или нажмите Отмена:", reply_markup=cancel_kb)
    await state.set_state(AddTeacher.waiting_for_name)

@router.message(AddTeacher.waiting_for_name)
async def add_teacher_name(message: Message, state: FSMContext):
    if message.text.lower() == "отмена":
        await message.answer("Добавление отменено.", reply_markup=teachers_menu_kb)
        await state.clear()
        return

    await state.update_data(name=message.text)
    await message.answer("Введите описание преподавателя (можно пропустить):", reply_markup=cancel_kb)
    await state.set_state(AddTeacher.waiting_for_description)

@router.message(AddTeacher.waiting_for_description)
async def add_teacher_description(message: Message, state: FSMContext):
    if message.text.lower() == "отмена":
        await message.answer("Добавление отменено.", reply_markup=teachers_menu_kb)
        await state.clear()
        return
    if message.text.lower() == "пропустить":
        message.text = None

    description = message.text if message.text.strip() else None
    await state.update_data(description=description)
    await message.answer("Введите ссылку на фото преподавателя (можно пропустить):", reply_markup=cancel_kb)
    await state.set_state(AddTeacher.waiting_for_photo_url)

@router.message(AddTeacher.waiting_for_photo_url)
async def add_teacher_photo(message: Message, state: FSMContext):
    if message.text.lower() == "отмена":
        await message.answer("Добавление отменено.", reply_markup=teachers_menu_kb)
        await state.clear()
        return
    if message.text.lower() == "пропустить":
        message.text = None

    photo_url = message.text if message.text.strip() else None
    data = await state.get_data()
    name = data.get("name")
    description = data.get("description")

    teacher = create_teacher(name=name, description=description, photo_url=photo_url)

    if teacher:
        await message.answer(f"Преподаватель '{name}' успешно добавлен!", reply_markup=teachers_menu_kb)
    else:
        await message.answer("Ошибка при добавлении преподавателя. Попробуйте ещё раз.", reply_markup=teachers_menu_kb)

    await state.clear()

@router.message(TextEqualsFilter("Назад"))
async def back_to_previous_menu(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state:
        await state.clear()
    await message.answer("Выберите действие:", reply_markup=main_menu_kb)
