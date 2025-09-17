from aiogram import Dispatcher

from bot.commands import task_add, task_list, task_delete, start

def add_routes(dp: Dispatcher) -> None:
    dp.include_router(task_add.router)
    dp.include_router(task_delete.router)
    dp.include_router(task_list.router)
    dp.include_router(start.router)