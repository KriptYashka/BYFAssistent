from aiogram import Dispatcher

from routers.manage import router as r_manage
from routers.teacher_edit import router as r_teacher_edit

def create_dispatcher():
    dp = Dispatcher()
    dp.include_router(r_manage)
    dp.include_router(r_teacher_edit)
    return dp