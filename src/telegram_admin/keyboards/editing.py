from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from misc.common import TeacherEditCallback

teacher_edit_inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="<<", callback_data=TeacherEditCallback.PREV),
        InlineKeyboardButton(text=">>", callback_data=TeacherEditCallback.NEXT),
    ],
    [
        InlineKeyboardButton(text="Изменить имя", callback_data=TeacherEditCallback.EDIT_NAME),
        InlineKeyboardButton(text="Изменить описание", callback_data=TeacherEditCallback.EDIT_DESC),
    ],
    [
        InlineKeyboardButton(text="Изменить фото", callback_data=TeacherEditCallback.EDIT_PHOTO),
        InlineKeyboardButton(text="Удалить", callback_data=TeacherEditCallback.DELETE),
    ]
])
