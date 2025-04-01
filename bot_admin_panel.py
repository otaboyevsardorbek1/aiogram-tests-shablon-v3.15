import sys
import asyncio
# Windows uchun asyncio muammosini hal qilish
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import time
import logging
from aiogram import Bot, Dispatcher,F,Router
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
from aiogram.filters import Command,CommandStart
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker,declarative_base
from aiogram.filters import StateFilter

# Logging konfiguratsiyasi
logging.basicConfig(level=logging.INFO)

API_TOKEN = '8183549397:AAHy3nETk7Zn7cJlzHUVX84fzqCWZf_zGC4'
ADMINS =[6646928202,6613047441] # admin IDS

# admin router
admin_router=Router()

# SQLAlchemy konfiguratsiyasi
DATABASE_URL = "sqlite:///admin_panel_demo.db"
Base = declarative_base()

# Ma'lumotlar bazasi modellari
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    block = Column(Integer, default=0)

class Schedule(Base):
    __tablename__ = 'schedule'
    id = Column(Integer, primary_key=True)
    description = Column(Text)

# SQLAlchemy Session yaratish
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# barcha jadvlallarni yaratish
Base.metadata.create_all(engine)

# Aiogram bot va dispatcher
bot = Bot(token=API_TOKEN)
storage=MemoryStorage()

dp = Dispatcher(storage=storage)

dp.include_router(admin_router)
# Foydalanuvchi va jadval funksiyalarini qo'shish
class Dialog(StatesGroup):
    spam = State()
    blacklist = State()
    whitelist = State()
    command = State()
    all_command = State()

@admin_router.message(CommandStart())
async def start(message: Message):
    user_id = message.from_user.id
    full_name=message.from_user.full_name

    user = session.query(User).filter_by(user_id=user_id).first()

    if message.from_user.id in ADMINS:

        # ReplyKeyboardMarkup yaratish
        keyboard = ReplyKeyboardBuilder()
        # Tugmalar qo'shish
        keyboard.button(text='Yuborish')
        keyboard.button(text='FVQ')
        keyboard.button(text='FVOT')
        keyboard.button(text='Jadvalni qo`shish')
        keyboard.button(text='Barcha jadvallar')
        keyboard.button(text='Ortga')
        keyboard.adjust(3, 3)

        # Foydalanuvchiga xabar yuborish
        await message.answer(
            f'Xush kelibsiz {message.from_user.username} Admin paneliga',
            reply_markup=keyboard.as_markup()
        )
    elif not user:
        new_user = User(user_id=user_id)
        session.add(new_user)
        session.commit()
        
        welcom_user_dialog = (
            "Salom hurmatli foydalanuvchi\n"
            f" '{full_name}' !\n"
        )
        await message.answer(text=welcom_user_dialog)
    else:
        user_dialog = (
            "Sizga qanday yordam bera olaman\n"
            f" '{full_name}' !\n"
        )
        await message.answer(text=user_dialog)


# Jadvalni qo'shish
@admin_router.message(F.text=='Jadvalni qo`shish')
async def add_command(message: Message,state: FSMContext):
    if message.from_user.id in  ADMINS:
        await message.answer('Qo`shmoqchi bo`lgan ma`lumotni jo`nating:')
        await state.set_state(Dialog.command)
    else:
        await message.answer('Admin emasiz.!')

@admin_router.message(StateFilter(Dialog.command))
async def save_schedule(message: Message, state: FSMContext):
    if message.text == 'Ortga':
        await back_to_main_menu(message)
        await state.set_state(None)
    else:
        new_schedule = Schedule(description=message.text)
        session.add(new_schedule)
        session.commit()
        await message.answer(f'Jadvalga qo`shildi:{message.text}')
        await back_to_main_menu(message=message)
        await state.set_state(None)

# Barcha jadvalni ko'rsatish
@admin_router.message(F.text=='Barcha jadvallar')
async def show_all_schedules(message: Message):
    schedules = session.query(Schedule).all()
    for schedule in schedules:
        await message.answer(schedule.description)

    await back_to_main_menu(message=message)

# Spam yuborish
@admin_router.message(F.text=='Yuborish')
async def spam(message: Message,state: FSMContext):
    if message.from_user.id in ADMINS:
        
        await state.set_state(Dialog.spam)

        await message.answer('Matini jo`nating:')
    else:
        await message.answer('Bu buyruq adminlar uchun')

@admin_router.message(StateFilter(Dialog.spam))
async def send_spam(message: Message, state: FSMContext):
    if message.text == 'Ortga':
        await back_to_main_menu(message)
        await state.set_state(None)
    else:
        users = session.query(User).all()
        siz=len(users)
        for user in users:
            try:
                await bot.send_message(user.user_id, message.text)
            except Exception as e:
                logging.error(f"Failed to send message to {user.user_id}: {e}")
                
        await message.answer(f'Habar: {siz} jao`natildi.!')
        await back_to_main_menu(message=message)
        await state.set_state(None)

# Foydalanuvchilarni bloklash
@admin_router.message(F.text=='FVQ')
async def add_to_blacklist(message: Message,state: FSMContext):
    if message.from_user.id in ADMINS:

        await state.set_state(Dialog.blacklist)

        await message.answer('Bloklamoqchi bo`lgan foydalanuvchining chat_id ni jo`nating: ')
    else:
        await message.answer('Faqat admin uchun ishlaydi bu buyruq.!')

@admin_router.message(StateFilter(Dialog.blacklist))
async def block_user(message: Message, state: FSMContext):
    if message.text == 'Ortga':
        await back_to_main_menu(message)
        await state.set_state(None)
    else:
        user_id = int(message.text)
        user = session.query(User).filter_by(user_id=user_id).first()
        if user:
            user.block = 1
            session.commit()
            await message.answer(f'Foydlanuvchi {user_id} bloklandi.!')
            await back_to_main_menu(message=message)
        else:
            await message.answer(f'Foydlanuvchi {user_id} topilmadi.!')
            await back_to_main_menu(message=message)
        await state.set_state(None)

# Foydalanuvchini blokdan chiqarish
@admin_router.message(F.text=='FVOT')
async def remove_from_blacklist(message: Message,state: FSMContext):
    if message.from_user.id in ADMINS:
        await state.set_state(Dialog.whitelist)

        await message.answer('bloklangan foydalanuvchining chat_idsini jo`nating: ')
    else:
        await message.answer('Admin foydalana oladi bu buyruqdan.!')

@admin_router.message(StateFilter(Dialog.whitelist))
async def unblock_user(message: Message, state: FSMContext):
    if message.text == 'Ortga':
        await back_to_main_menu(message)
        await state.set_state(None)
    else:
        try:
            user_id = int(message.text)
            user = session.query(User).filter_by(user_id=user_id).first()
            if user:
                user.block = 0
                session.commit()
                await message.answer(f'Foydlanauvchi {user_id} bloklandi.!')
                await back_to_main_menu(message=message)
            else:
                await message.answer(f'Foydlanauvchi {user_id} topilmadi.!')
                await back_to_main_menu(message=message)
            await state.set_state(None)
        except(ValueError):
            text=(
                "Xato ma`lumot kiritdingiz\n"
                "Botga ixtiyoriy userning\n"
                "chat_id ni jo`nating.!\n"
                f"Bu {user_id} ma`lumotni emas.!!!"
            )
            await message.answer(text=text)

# Orqaga qaytish
async def back_to_main_menu(message: Message):
    keyboard = ReplyKeyboardBuilder()
        # Tugmalar qo'shish
    keyboard.button(text='Yuborish')
    keyboard.button(text='FVQ')
    keyboard.button(text='FVOT')
    keyboard.button(text='Jadvalni qo`shish')
    keyboard.button(text='Barcha jadvallar')
    keyboard.button(text='Ortga')
    keyboard.adjust(3, 3)
    await message.answer('Asosiy menyu', reply_markup=keyboard.as_markup())

# Botni ishga tushirish
async def on_startup(dp):
    logging.warning('Starting connection...')
    try:
        date_now = time.strftime("%Y-%m-%d", time.localtime())
        time_now = time.strftime("%H:%M:%S", time.localtime())
        for chat_id in ADMINS:
            text = (f"✅Bot ishga tushdi!✅\n"
                    f"📅Mon: {date_now}\n"
                    f"⏰Vaqt: {time_now}")
            await bot.send_message(chat_id=chat_id, text=text)
        logging.warning('Connection established.')  
    except Exception as e:
        for chat_id in ADMINS:
            await bot.send_message(chat_id=chat_id, text=f'Error: {e}')
        logging.error(f"Error: {e}")

async def on_shutdown(dp):
    logging.warning('Bot ishlashni to`xtatildi.!!')
    try:
        date_now = time.strftime("%Y-%m-%d", time.localtime())
        time_now = time.strftime("%H:%M:%S", time.localtime())
        for chat_id in ADMINS:
            text = (f"🛑Bot to`xtatildi.!🛑\n"
                    f"📅Mon: {date_now}\n"
                    f"⏰Vaqt: {time_now}")
            await bot.send_message(chat_id=chat_id, text=text)
        logging.warning('Connection established.')  
    except Exception as e:
        for chat_id in ADMINS:
            await bot.send_message(chat_id=chat_id, text=f'Error: {e}')
        logging.error(f"Error: {e}")


async def main():
    try:
        await on_startup(dp)
        await dp.start_polling(bot)
    except Exception:
        pass
    finally:
        await asyncio.sleep(1)
        await on_shutdown(dp)
        await asyncio.sleep(1)
        await dp.storage.close()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception:
        pass
    except(KeyboardInterrupt) as devstop:
        print("\n")
        print("Dasturni to`xtatdingiz.!")

