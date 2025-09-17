import os

import requests

from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

from dotenv import load_dotenv

load_dotenv()

router = Router()

@router.message(Command('delete'))
async def task_add(message: Message, command: CommandObject) -> None:
    if not command.args or not command.args.isdigit():
        await message.answer("❌ Нужно указать id задачи!\nПример: /delete 1")
        return

    task_id = int(command.args)
    response = requests.delete(url=f'{os.getenv('MAIN_ENDPOINT')}/tasks/delete/{task_id}')
    if response.status_code != 200:
        await message.answer("❌ Что то пошло не так, попробуйте еще раз")
        return

    await message.answer('Операция прошла успешно!')