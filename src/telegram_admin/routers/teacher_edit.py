from aiogram import Router, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message, CallbackQuery, InputMediaPhoto, InputFile, BufferedInputFile
from aiogram.fsm.context import FSMContext

from filters.common import TextEqualsFilter
from handlers.teachers import get_all_teachers, update_teacher, delete_teacher
from keyboards.common import cancel_kb
from keyboards.teacher import teacher_edit_inline_kb
from misc.common import TeacherEditCallback as Callback
from misc.states import TeacherEditStates as States
from utils.image import get_image_placeholder

router = Router()

async def get_state_data(state: FSMContext):
    data = await state.get_data()
    index = data.get("current_index", 0)
    teachers = data.get("teachers", [])
    return index, teachers

@router.message(F.text.casefold() == "отмена")
async def cancel_any_state(message: Message, state: FSMContext):
    """
    Возврат к редактированию текущего преподавателя (если индекс сохранён)
    """
    index, _ = await get_state_data(state)
    await state.clear()
    await show_teacher_edit_start(message, state, current_index=index)


@router.callback_query(F.data == Callback.PREV)
async def on_prev_teacher(call: CallbackQuery, state: FSMContext):
    index, teachers = await get_state_data(state)

    if not teachers:
        await call.answer("Нет преподавателей.", show_alert=True)
        return

    index = (index - 1) % len(teachers)
    await state.update_data(current_index=index)
    await send_teacher_edit(call, state)


@router.callback_query(F.data == Callback.NEXT)
async def on_next_teacher(call: CallbackQuery, state: FSMContext):
    index, teachers = await get_state_data(state)

    if not teachers:
        await call.answer("Нет преподавателей.", show_alert=True)
        return

    index = (index + 1) % len(teachers)
    await state.update_data(current_index=index)
    await send_teacher_edit(call, state)

@router.callback_query(F.data == Callback.EDIT_NAME)
async def on_edit_name_teacher_callback(call: CallbackQuery, state: FSMContext):
    index, teachers = await get_state_data(state)

    if not teachers:
        await call.answer("Нет преподавателей.", show_alert=True)
        return

    await state.set_state(States.edit_name)
    await call.message.answer("Введите новое имя", reply_markup=cancel_kb)

@router.message(States.edit_name)
async def on_edit_name_teacher_set_name(message: Message, state: FSMContext):
    index, teachers = await get_state_data(state)
    pk = teachers[index].id
    name = message.text
    update_teacher(pk, name=name)

    await state.clear()
    await show_teacher_edit_start(message, state, current_index=index)

@router.callback_query(F.data == Callback.EDIT_DESC)
async def on_edit_desc_teacher_callback(call: CallbackQuery, state: FSMContext):
    index, teachers = await get_state_data(state)

    if not teachers:
        await call.answer("Нет преподавателей.", show_alert=True)
        return

    await state.set_state(States.edit_description)
    await call.message.answer("Введите новое описание преподавателя", reply_markup=cancel_kb)

@router.message(States.edit_description)
async def on_edit_desc_teacher_set(message: Message, state: FSMContext):
    index, teachers = await get_state_data(state)
    pk = teachers[index].id
    description = message.text
    update_teacher(pk, description=description)

    await state.clear()
    await show_teacher_edit_start(message, state, current_index=index)

@router.callback_query(F.data == Callback.EDIT_PHOTO)
async def on_edit_photo_teacher_callback(call: CallbackQuery, state: FSMContext):
    index, teachers = await get_state_data(state)

    if not teachers:
        await call.answer("Нет преподавателей.", show_alert=True)
        return

    await state.set_state(States.edit_photo)
    await call.message.answer("Вставьте новую ссылку (URL) на фото преподавателя", reply_markup=cancel_kb)

@router.message(States.edit_photo)
async def on_edit_photo_teacher_set(message: Message, state: FSMContext):
    index, teachers = await get_state_data(state)
    pk = teachers[index].id
    photo_url = message.text
    update_teacher(pk, photo_url=photo_url)

    await state.clear()
    await show_teacher_edit_start(message, state, current_index=index)


@router.callback_query(F.data == Callback.DELETE)
async def on_delete_teacher_callback(call: CallbackQuery, state: FSMContext):
    index, teachers = await get_state_data(state)

    if not teachers:
        await call.answer("Нет преподавателей.", show_alert=True)
        return

    await state.set_state(States.confirm_delete)
    await call.message.answer(
        "Вы уверены, что хотите удалить этого преподавателя?\n\n"
        "Введите 'Да' для подтверждения или нажмите Отмена.",
        reply_markup=cancel_kb
    )

@router.message(States.confirm_delete)
async def confirm_delete_teacher(message: Message, state: FSMContext):
    index, teachers = await get_state_data(state)
    text = message.text.lower()
    if text == "да":
        pk = teachers[index].id
        delete_teacher(pk)

        teachers = get_all_teachers()
        if not teachers:
            await message.answer("Преподавателей больше нет.")
            await state.clear()
            return

        if index >= len(teachers):
            index = 0
        await state.update_data(teachers=teachers, current_index=index)

    await state.clear()
    await show_teacher_edit_start(message, state, current_index=index)


@router.message(TextEqualsFilter("Редактировать"))
async def show_teacher_edit_start(message: Message, state: FSMContext, current_index=0):
    teachers = get_all_teachers()
    if not teachers:
        await message.answer("Преподаватели не найдены.")
        return

    await state.update_data(teachers=teachers, current_index=current_index)
    await send_teacher_edit(message, state)

def get_teacher_caption(teacher):
    caption = f"**{teacher.name}**\n\n"
    caption += teacher.description if teacher.description else "Описание отсутствует."
    return caption

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
