from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Заявки"), KeyboardButton(text="Управление")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
manage_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Группы"), KeyboardButton(text="Расписание")],
        [KeyboardButton(text="Прочее")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
manage_other_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Преподаватели"), KeyboardButton(text="Студии")],
        [KeyboardButton(text="Залы")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

add_or_edit_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Добавить"), KeyboardButton(text="Редактировать")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

add_or_delete_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Добавить"), KeyboardButton(text="Удалить")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
