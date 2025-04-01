from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from config import BOT_TOKEN
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher(bot=bot)