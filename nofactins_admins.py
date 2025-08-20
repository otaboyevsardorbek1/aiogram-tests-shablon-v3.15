import time
from aiogram import Dispatcher,types,Bot
from config import ADMINS_ID,BOT_USERNAME
from custom_logger import loggers
from loader import bot,dp
ADMINS_NOTIFY=loggers(log_name='ADMINS_NOTIFY')

date_now = time.strftime("%Y-%m-%d", time.localtime())
time_now = time.strftime("%H:%M:%S", time.localtime())

# bot ishga tushganda adminlarga habar yuborish
async def on_startup_notify(dp: Dispatcher):
    ADMINS_NOTIFY.info("Adminga habar berish jarayoni boshlandi")
    for admin in ADMINS_ID:
        try:
            text = (f"✅Bot ishga tushdi!✅\n"
                    f"📅Mon: {date_now}\n"
                    f"⏰Vaqt: {time_now}\n"
                    f"Bot: {BOT_USERNAME}")
            await bot.send_message(
                admin, text=text, disable_notification=True
            )
        except Exception as error:
            text=(f"Bunday admin yo`q:{admin}\nXato: {error}")
            await bot.send_message(chat_id=admin,text=text)

# Bot ishdan chiqsa yoki to‘xtab qolsa adminga xabar yuborish
async def on_shutdown_notify(dp: Dispatcher):
    ADMINS_NOTIFY.info("Bot to‘xtab qolganda adminga xabar berish")
    for admin in ADMINS_ID:
        try:
            text = ("Bot ishdan chiqdi\n"
                    f"📅Mon: {date_now}\n"
                    f"⏰Vaqt: {time_now}\n"
                    "Sababini /log buyrug‘i orqali ko‘rib olishingiz mumkin!")
            await bot.send_message(
                admin, text=text, disable_notification=True
            )
        except Exception as error:
            text = f"Bunday admin yo‘q: {admin}\nXato: {error}"
            await bot.send_message(chat_id=admin, text=text)
    await bot.session.close()
            
async def ERROR_TO_ADMIN_SEND(update: types.Update, exception: Exception):
    try:
       for chat_id in ADMINS_ID:
            await bot.send_message(chat_id, f"Xato yuz berdi: {exception}\nUpdate: {update}")
    except Exception as e:
        ADMINS_NOTIFY.error(f"Xato yuborishda muammo: {e}")

#Error handlerni botga qo'shish
async def nofactins_admin():
    dp.error.handlers.append(ERROR_TO_ADMIN_SEND)
    dp.startup.handlers.append(on_startup_notify(dp=dp))
    dp.shutdown.handlers.append(on_shutdown_notify(dp=dp))
    
     