import sys
import asyncio
# Windows uchun asyncio muammosini hal qilish
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
#
import tracemalloc
tracemalloc.start()
#
from config import ADMINS_ID,ADMIN_USERNAME,cmd_help,admin_cmd,LOG_FILE,MAX_LOG_SIZE_MB
from aiogram import types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineQuery, InlineQueryResultArticle, InputTextMessageContent,FSInputFile
from database import add_user_settings, get_user_settings, update_user_settings,db_init,get_all_user_ids
from custom_logger import loggers
import requests
import datetime

import os

# bot default camands
from bot_cammands import set_default_commands
# 🔹 Bot sozlamalari
from loader import dp,bot
# datbase init
db_init()

#log glabal
log=loggers(log_name="Books-Bot")

def devolper_username():
    usernmae=""
    for name in ADMIN_USERNAME:
        usernmae+=f"Admin: {name}\n"
    return usernmae

# 🔹 /start buyruq
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    bot_data=await bot.get_me()
    bot_usernmae=bot_data.username
    user_id = message.from_user.id
    full_name=message.from_user.full_name
    username=message.from_user.username
    lang_code=message.from_user.language_code
    # Agar foydalanuvchi yangi bo‘lsa, uni bazaga qo‘shamiz
    if not get_user_settings(user_id):
        add_user_settings(user_id, lang_code)
        if username:
            invite_link = f"[@{username}]\n(https://t.me/{username})"
        else:
            invite_link = f"[Telegram profili](tg://user?id={message.from_user.id})"
        user_add_messgae = ((
        f"Salom : *{full_name}*!\n\n"
        f"📌Telegram profili: {invite_link}\n\n"
        f"⚙ Glabal lang_code: {lang_code}\n"
        f"⚙ User_id: {user_id}\n"
        f"🤖Bot usernmae:@{bot_usernmae}\n").format(full_name=full_name,invite_link=invite_link,lang_code=lang_code,user_id=user_id,bot_usernmae=bot_usernmae))
        for chat_id in ADMINS_ID:
            await bot.send_message(chat_id=chat_id,text=user_add_messgae)
        greeting_message = ((
        f"Salom Botimizga hush kelibsiz!: *{full_name}*!\n\n"
        f"🤖Bot usernmae:@{bot_usernmae}\n").format(full_name=full_name,bot_usernmae=bot_usernmae))
        await message.answer(text=greeting_message)
    elif user_id in ADMINS_ID:
        admin_messgae=(f"Salom, Admin! {full_name}\n\n")
        await message.answer(text=admin_messgae)
    else:
        await message.answer(text=("Sizga qanday yordam bera olaman.!"))

# ##############################################################################################
# /png komandasiga javob beradigan funksiya
@dp.message(Command('png'))
async def cmd_png(message: types.Message):
    chat_id=message.from_user.id
    text=message.text
    info_message=await message.answer(f"Ma`lumot qabul qilindi: {text}")
    try:
        bot_data=await bot.get_me()
        capshin2=f'\n@{bot_data.username}\n\n'
        text = message.text.split(maxsplit=1)  # Buyruqdan keyingi matnni olish
        if len(text) > 1:  # Agar matn bo'lsa
            user_text = text[1]  # Matnni olish
            # API URL
            api_url = f"https://api.smtv.uz/generator/index.php?text={user_text}"
            # API ga GET so'rov yuborish
            response = requests.get(api_url)
            if response.status_code == 200:
                await bot.delete_message(chat_id=chat_id,message_id=info_message.message_id)
                await asyncio.sleep(2)
                await message.reply_photo(photo=api_url,caption=user_text+capshin2)
            else:
                await message.reply(text=("Rasm yaratishda xatolik yuz berdi!"))
        else:
            await message.reply(text=("Iltimos, matn kiriting: /png [matn]"))
    except Exception as e:
        await message.reply(text=(f"Xatolik yuz berdi: {e}"))


# ✅ Bot log faylini yuborish va tozalash
@dp.message(Command("log"))
async def send_log(message: types.Message):
    chat_id=message.chat.id
    full_name=message.from_user.full_name

    if chat_id in ADMINS_ID:
        try:
            if not os.path.exists(LOG_FILE):
                return await message.answer("❌ Log fayli topilmadi!")
            info_messgae=await message.answer(f"Kutubturing {LOG_FILE} Jo`natishga tayyorlanmoqda.!")
            file_size_mb = os.path.getsize(LOG_FILE) / (1024 * 1024)  # MB ga o‘girish
            log_file = FSInputFile(LOG_FILE)
            await bot.send_chat_action(message.chat.id, "upload_document")
            await asyncio.sleep(1)
            await bot.delete_message(chat_id=chat_id,message_id=info_messgae.message_id)    
            await message.answer_document(log_file, caption=f"📂 `{LOG_FILE}` fayli\n📏 Hajmi: {file_size_mb:.2f} MB\n📅 Oxirgi yozilgan sana: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
            # Log faylni tozalash
            with open(LOG_FILE, "w", encoding="utf-8") as file:
                file.write("")

            await message.answer(f"✅ `{LOG_FILE}` fayli yangilandi!")
        except Exception as err:
            log.info(f"❌ {LOG_FILE} faylni yuborib bo‘lmadi! Xato: {err}")
            await message.answer(f"❌ {LOG_FILE} faylni yuborib bo‘lmadi! Xato: {err}")
    else:
        username = message.from_user.username  # Username (agar bo'lsa)
        log.info(f"Log fayilini: {full_name} <--> username: {username} olishga urindi")
        await message.answer("🚫 Siz bu buyruqni ishlata olmaysiz!")

 
# ✅ Log fayl hajmini tekshirish va avtomatik yuborish
async def check_log_file():
    if os.path.exists(LOG_FILE):
        file_size_mb = os.path.getsize(LOG_FILE) / (1024 * 1024)  # MB ga o‘girish
        if file_size_mb >= MAX_LOG_SIZE_MB:
            log_file = FSInputFile(LOG_FILE)
            for chat_id in ADMINS_ID:
                await bot.send_document(chat_id=chat_id,file=log_file, caption=f"📂 `bot.log` hajmi: {file_size_mb:.2f} MB\n📅 Oxirgi yozilgan sana: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            with open(LOG_FILE, "w", encoding="utf-8") as file:
                file.write("")  # Log faylni tozalash
            log.info("✅ Log fayli tozalandi va adminga yuborildi!")

# admin or user bot statistika
@dp.message(Command("stat"))
async def admin_base(message: types.Message):
    full_name=message.from_user.full_name
    user_id=message.from_user.id
    data=len(get_all_user_ids())
    if user_id in ADMINS_ID:
        text=("Salom {full_name}\nAdmin Bot obunachilari soni: {data}\n\n").format(full_name=full_name,data=data)
        await message.answer(text=text)
    else:
        text=("{full_name}\nBot obunachilari soni: {data}").format(full_name=full_name,data=data)
        await message.answer(text=text)

# 🔹 /help buyruq
@dp.message(Command('help'))
async def cmd_help(message: types.Message):
    chat_id=message.from_user.id
    if chat_id in  ADMINS_ID:
        await message.answer(text=(admin_cmd))
    else:
        await message.answer(text=(cmd_help))
# 🔹 Asosiy funksiya
# ######################################################################################################
async def main():
    try:
        await check_log_file()
        # nofactins_admin()
        await set_default_commands(bot=bot) 
        await dp.start_polling(bot)
            
    except KeyboardInterrupt:
        print("Siz dasturni to`xtatdingiz")

# 🔹 Botni ishga tushirish
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except(KeyboardInterrupt) as devstop:
        print("Siz dasturni to`xtatdingiz")
