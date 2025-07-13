from aiogram import Dispatcher

from routers.manage import router as r_manage

def create_dispatcher():
    dp = Dispatcher()
    dp.include_router(r_manage)
    return dp