# asosiy sozlamalar bot conifguratsiyasi
BOT_TOKEN='8183549397:AAHy3nETk7Zn7cJlzHUVX84fzqCWZf_zGC4'
BOT_USERNAME='@FreeUzBot'
ADMINS_ID=[6646928202]#,6613047441
ADMIN_USERNAME=['@prodevuzoff','@Elyor_Xujamberdiyev']

# Botning database config
DB_TYPES='sqlite:///' # db configurate taype
DB_PATH = "bot.db"


# bot loger config file
LOG_FILE = "bot.log"
MAX_LOG_SIZE_MB=32
# BOTNING ASOSIY KANLI MA`LUMOTLARI
BOT_CHANEL_ID='-10090400404044'
BOT_CHANEL_URL='https://t.me/FreeUzBot'
BOT_CHANEL_NAME='Bot Kanali'
BOT_CHANEL_USERNAME='@FreeUzBot'

# BOTNING MUXOKAMA GURUXI

BOT_GURUX_ID='-1002355528439'
BOT_GURUX_URL='https://t.me/Potqursdoshlar_Xorazim_pro'
BOT_GURUX_NAME='Patqursdowlar👥'
BOT_GURUX_USERNAME='@Potqursdoshlar_Xorazim_pro'
BOT_GURUX_INVITELINK='https://t.me/+BPNy_6Cv0U84MDcy'
BOT_GURUX_INVITEHTML='<a href="https://t.me/+BPNy_6Cv0U84MDcy">Guruhga qo`shish</a>'

# botning help yordamchi matni userslar uchun 
cmd_help=(
    "Botdan foydalanish yo`riqnmoasi\n"
    "inline shazam funqsiyasi mavjud\n"
    f"Foydalanish `{BOT_USERNAME} shazam <song name>`\n"
    "Rasimlarni generatsiya qilish\n"
    "/png <matin> va sizga bot \n"
)

admin_cmd=( # botning adminlar uchun help matni
    "Botning admin buyruqlari\n"
    "/start - botni ishga tushirish\n"
    "/stat - botdan foydalanuvchilar\n"
    "/help - yordam\n"
    "/png - rasimlarni generatsiya qilish\n"
    "/admin - Admin panel\n"
    "/exit - botni to`xtatish\n"
    f"Bot kanali: {BOT_CHANEL_USERNAME}\n"
    f"{cmd_help}"
)
