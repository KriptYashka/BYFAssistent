from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

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
