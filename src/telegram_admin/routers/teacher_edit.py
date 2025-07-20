from logging import Filter

from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from handlers.teachers import get_all_teachers

router = Router()

# Ключи callback_data для кнопок
PREV_CB = "teacher_prev"
NEXT_CB = "teacher_next"
EDIT_NAME_CB = "teacher_edit_name"
EDIT_DESC_CB = "teacher_edit_description"
EDIT_PHOTO_CB = "teacher_edit_photo"
DELETE_CB = "teacher_delete"

# Хранение текущего индекса пользователя — для упрощения примера используем FSMContext
# В реальном проекте можно хранить в БД или Redis

@router.message(F.text.lower() == "редактировать")
async def show_teacher_edit_start(message: Message, state: FSMContext):
    teachers = get_all_teachers()
    if not teachers:
        await message.answer("Преподаватели не найдены.")
        return

    await state.update_data(teachers=teachers, current_index=0)
    await send_teacher_edit(message, state)

async def send_teacher_edit(message_or_call, state: FSMContext, edit_message=False):
    data = await state.get_data()
    teachers = data.get("teachers", [])
    index = data.get("current_index", 0)

    if not teachers:
        await message_or_call.answer("Преподаватели не найдены.")
        return

    teacher = teachers[index]

    # Формируем текст с Markdown-разметкой
    caption = f"**{teacher.name}**\n\n"
    caption += teacher.description if teacher.description else "Описание отсутствует."

    # Клавиатура
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="<<", callback_data=PREV_CB),
            InlineKeyboardButton(text=">>", callback_data=NEXT_CB),
        ],
        [
            InlineKeyboardButton(text="Изменить имя", callback_data=EDIT_NAME_CB),
            InlineKeyboardButton(text="Изменить описание", callback_data=EDIT_DESC_CB),
        ],
        [
            InlineKeyboardButton(text="Изменить фото", callback_data=EDIT_PHOTO_CB),
            InlineKeyboardButton(text="Удалить", callback_data=DELETE_CB),
        ]
    ])

    # Отправляем или редактируем сообщение с фото
    photo_url = teacher.photo_url or "https://via.placeholder.com/300?text=No+Photo"

    if edit_message and isinstance(message_or_call, CallbackQuery):
        await message_or_call.message.edit_media(
            media=InputMediaPhoto(media=photo_url, caption=caption, parse_mode="Markdown"),
            reply_markup=keyboard
        )
        await message_or_call.answer()
    else:
        await message_or_call.answer_photo(photo=photo_url, caption=caption, parse_mode="Markdown", reply_markup=keyboard)

# Обработчики кнопок навигации

@router.callback_query(F.data == PREV_CB)
async def on_prev_teacher(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    index = data.get("current_index", 0)
    teachers = data.get("teachers", [])

    if not teachers:
        await call.answer("Нет преподавателей.", show_alert=True)
        return

    index = (index - 1) % len(teachers)
    await state.update_data(current_index=index)
    await send_teacher_edit(call, state, edit_message=True)

@router.callback_query(F.data == NEXT_CB)
async def on_next_teacher(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    index = data.get("current_index", 0)
    teachers = data.get("teachers", [])

    if not teachers:
        await call.answer("Нет преподавателей.", show_alert=True)
        return

    index = (index + 1) % len(teachers)
    await state.update_data(current_index=index)
    await send_teacher_edit(call, state, edit_message=True)

# Обработчики кнопок редактирования и удаления можно реализовать аналогично,
# например, переводить пользователя в соответствующее состояние FSM для ввода новых данных.

# ...

