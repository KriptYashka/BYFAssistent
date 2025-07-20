from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

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
