from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.bot_commands.custom_commands import custom_commands

router = Router()

@router.message(CommandStart)
async def start(message: Message) -> None:
    await message.answer(f'Список команд\n\n {'\n'.join(f'{i.command} - {i.description}' for i in custom_commands)}')