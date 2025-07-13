from aiogram import Dispatcher

from routers.register import router as r_register

def create_dispatcher():
    dp = Dispatcher()
    dp.include_router(r_register)
    return dp