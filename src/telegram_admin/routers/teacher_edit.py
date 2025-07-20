from aiogram import Router, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message, CallbackQuery, InputMediaPhoto, InputFile, BufferedInputFile
from aiogram.fsm.context import FSMContext

from filters.common import TextEqualsFilter
from handlers.teachers import get_all_teachers
from keyboards.common import teacher_edit_inline_kb
from misc.common import TeacherEditCallback as Callback
from utils.image import get_image_placeholder

router = Router()

@router.callback_query(F.data == Callback.PREV)
async def on_prev_teacher(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    index = data.get("current_index", 0)
    teachers = data.get("teachers", [])

    if not teachers:
        await call.answer("Нет преподавателей.", show_alert=True)
        return

    index = (index - 1) % len(teachers)
    await state.update_data(current_index=index)
    await send_teacher_edit(call, state)

@router.callback_query(F.data == Callback.NEXT)
async def on_next_teacher(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    index = data.get("current_index", 0)
    teachers = data.get("teachers", [])

    if not teachers:
        await call.answer("Нет преподавателей.", show_alert=True)
        return

    index = (index + 1) % len(teachers)
    await state.update_data(current_index=index)
    await send_teacher_edit(call, state)

@router.message(TextEqualsFilter("Редактировать"))
async def show_teacher_edit_start(message: Message, state: FSMContext):
    teachers = get_all_teachers()
    if not teachers:
        await message.answer("Преподаватели не найдены.")
        return

    await state.update_data(teachers=teachers, current_index=0)
    await send_teacher_edit(message, state)

def get_teacher_caption(teacher):
    caption = f"**{teacher.name}**\n\n"
    caption += teacher.description if teacher.description else "Описание отсутствует."
    return caption

async def send_teacher_edit(message_or_call, state: FSMContext):
    data = await state.get_data()
    teachers = data.get("teachers", [])
    index = data.get("current_index", 0)

    if not teachers:
        await message_or_call.answer("Преподаватели не найдены.")
        return

    teacher = teachers[index]
    caption = get_teacher_caption(teacher)
    photo_url = teacher.photo_url

    try:
        await answer_message_with_media(message_or_call, caption, photo_url)
    except TelegramBadRequest:
        await answer_message_with_media(message_or_call, caption)


async def answer_message_with_media(message_or_call, caption, photo_url=None):
    photo_url = photo_url or BufferedInputFile(get_image_placeholder(), "Неизвестно")

    if isinstance(message_or_call, CallbackQuery):
        await message_or_call.message.edit_media(
            media=InputMediaPhoto(media=photo_url, caption=caption, parse_mode="Markdown"),
            reply_markup=teacher_edit_inline_kb
        )
        await message_or_call.answer()
    else:
        await message_or_call.answer_photo(photo=photo_url, caption=caption, parse_mode="Markdown",
                                           reply_markup=teacher_edit_inline_kb)
