import asyncio
from datetime import datetime, time, timedelta

import sqlalchemy as sa
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

# 1. Konfiguratsiya
BOT_TOKEN = "7552988744:AAFF1U_dEtU6LYNVYiw_9Tw3COutD6FmbDE"
ADMIN_ID = 6646928202  # o'z Telegram ID'ingizni qo'ying

# 2. DB tayyorlash
DATABASE_URL = "sqlite+aiosqlite:///./users.db"

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = sa.Column(sa.Integer, primary_key=True)
    tg_id = sa.Column(sa.BigInteger, unique=True, nullable=False)
    notify_hour = sa.Column(sa.Integer, nullable=True)
    notify_minute = sa.Column(sa.Integer, nullable=True)

engine = create_async_engine(DATABASE_URL, echo=False)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

# 3. Bot va Dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# 4. DB initialize funktsiyasi
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# 5. Foydalanuvchini yaratish yoki yangilash
async def add_or_update_user(tg_id: int, hour: int, minute: int):
    async with async_session() as session:
        result = await session.execute(sa.select(User).where(User.tg_id == tg_id))
        user = result.scalar_one_or_none()
        if user:
            user.notify_hour = hour
            user.notify_minute = minute
        else:
            user = User(tg_id=tg_id, notify_hour=hour, notify_minute=minute)
            session.add(user)
        await session.commit()

# 6. Foydalanuvchilarni vaqt bo‘yicha olish
async def get_users_for_time(hour: int, minute: int):
    async with async_session() as session:
        result = await session.execute(
            sa.select(User).where(
                User.notify_hour == hour,
                User.notify_minute == minute
            )
        )
        return result.scalars().all()

# 7. /start komandasi
@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "Salom!\n\n"
        "O‘z xabaringizni olish vaqtingizni o‘rnatish uchun /settime HH:MM formatida yozing.\n"
        "Masalan: /settime 21:30"
    )

# 8. /settime komandasi
@dp.message(Command("settime"))
async def settime_handler(message: Message):
    args = message.text.split()
    if len(args) != 2:
        await message.answer("Iltimos, vaqtni HH:MM formatida kiriting. Masalan: /settime 21:30")
        return
    try:
        t = datetime.strptime(args[1], "%H:%M").time()
    except ValueError:
        await message.answer("Noto‘g‘ri format. Iltimos, HH:MM formatida vaqt kiriting.")
        return

    await add_or_update_user(message.from_user.id, t.hour, t.minute)
    await message.answer(f"Sizning xabaringiz {t.strftime('%H:%M')} da yuboriladi.")

# 9. Admin uchun /stats komandasi
@dp.message(F.from_user.id == ADMIN_ID, Command("stats"))
async def stats_handler(message: Message):
    async with async_session() as session:
        result = await session.execute(sa.select(sa.func.count(User.id)))
        count = result.scalar()
        await message.answer(f"Botda jami {count} ta foydalanuvchi bor.")

# 10. Fon vazifa — xabarlarni yuborish
async def notify_task():
    while True:
        now = datetime.now()
        current_hour = now.hour
        current_minute = now.minute

        users = await get_users_for_time(current_hour, current_minute)
        if users:
            print(f"{len(users)} ta foydalanuvchiga xabar yuborilmoqda {current_hour}:{current_minute}")
        for user in users:
            try:
                await bot.send_message(user.tg_id, f"Salom! Bu sizning {current_hour:02d}:{current_minute:02d} da yuborilgan statistik xabaringiz.")
            except Exception as e:
                print(f"Xatolik: {e} - user_id: {user.tg_id}")

        # Keyingi minutgacha kutamiz
        await asyncio.sleep(60 - datetime.now().second)

# 11. Asosiy ishga tushirish
async def main():
    await init_db()
    print("Bot ishga tushmoqda...")
    # Fon vazifani ishga tushiramiz
    asyncio.create_task(notify_task())
    # Dispatcher polling
    await dp.start_polling(bot,timeout=30,HANDLE_SIGINT=True, HANDLE_SIGTERM=True)

if __name__ == "__main__":
    asyncio.run(main())
