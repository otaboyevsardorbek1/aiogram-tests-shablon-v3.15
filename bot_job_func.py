import asyncio
from datetime import datetime, timedelta

# Belgilangan yuborish vaqti (masalan, har kuni soat 12:00)
target_hour = 21
target_minute = 13

# Hoziroq vaqt
current_time = datetime.now()

# Belgilangan vaqti aniqlash
last_sent_time = current_time.replace(hour=target_hour, minute=target_minute, second=0, microsecond=0)

# Agar hozirgi vaqt belgilangan vaqtdan o‘tgandan keyin bo‘lsa, 1 kun oldinga surish
if current_time > last_sent_time:
    next_send_time = current_time + timedelta(days=1)
    print("Ertaga surildi.!")
else:
    next_send_time = last_sent_time  # Agar vaqt hali o'tmagan bo'lsa

# Yuborish uchun kutish (asynchronous)
async def bot_job():
    global next_send_time  # next_send_time ni global qilib olish
    while True:
        current_time = datetime.now()
        if current_time >= next_send_time:
            print(f"Xabar yuborilmoqda: {next_send_time}")

            next_send_time = current_time + timedelta(days=1)
        await asyncio.sleep(60)  # Har 60 sekundda vaqtni tekshirib borish

async def main():
    await bot_job()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except(KeyboardInterrupt):
        print("Dastur to`xtatildi.!")
    finally:
        print("Dastur yakuniga yetdi.!")
