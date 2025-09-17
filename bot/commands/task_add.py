import json
import os

import requests

from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

from dotenv import load_dotenv

load_dotenv()

router = Router()

@router.message(Command('add'))
async def task_add(message: Message, command: CommandObject) -> None:
    if not command.args:
        await message.answer("❌ Нужно указать текст задачи!\nПример: /add Купить хлеб")
        return

    task_text = command.args
    data = json.dumps({'description': task_text})
    response = requests.post(url=f'{os.getenv('MAIN_ENDPOINT')}/tasks/create', data=data)
    if response.status_code != 201:
        await message.answer("❌ Что то пошло не так, попробуйте еще раз")
        return

    await message.answer(f"✅ Задача добавлена: {task_text}")