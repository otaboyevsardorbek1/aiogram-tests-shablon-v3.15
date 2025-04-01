from aiogram.types import BotCommand
from aiogram import types,Bot
from aiogram.filters import command
from custom_logger import loggers
from loader import bot,dp

bot_infa=loggers(log_name='bot-cammands run status')

async def set_default_commands(bot: Bot):
    bot_infa.info("Botga default bot buyruqlari qo`shildi")
    commands = [
        BotCommand(command="start", description="Botni ishga tushirish"),
        BotCommand(command="help", description="Yordam ma'lumotlari"),
        BotCommand(command="info", description="Bot haqida ma'lumot"),
        BotCommand(command="admin", description="Admin panel")
    ]
    await bot.set_my_commands(commands)
    bot_infa.info('Buyruqlar paneli qo`shildi.!')