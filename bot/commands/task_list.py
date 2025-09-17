import os

import requests

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from dotenv import load_dotenv

load_dotenv()

router = Router()

@router.message(Command('list'))
async def task_list(message: Message) -> None:
    response = requests.get(url=f'{os.getenv('MAIN_ENDPOINT')}/tasks/get-all')
    if response.status_code != 200:
        await message.answer("❌ Что то пошло не так, попробуйте еще раз")
        return

    await message.answer(f"Список задач:\n\n {'\n'.join([f'{item['id']}) {item['description']}' for item in response.json()])}")