import logging
import sys
import asyncio
from aiogram import Dispatcher

from bot.bot import bot
from bot.bot_commands.custom_commands import custom_commands
from bot.routes import add_routes

dp = Dispatcher()

async def start_bot() -> None:
    add_routes(dp)
    await bot.set_my_commands(custom_commands)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(start_bot())
