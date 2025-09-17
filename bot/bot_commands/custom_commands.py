from aiogram.types import BotCommand

custom_commands = [
    BotCommand(command='/list', description='список заметок'),
    BotCommand(command='/add', description='Добавить заметку (например: /add Купить хлеб)'),
    BotCommand(command='/delete', description='удалить заметку (например: /delete 1)'),
]