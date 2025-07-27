import sys
import asyncio
# Windows uchun asyncio muammosini hal qilish
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import asyncio
import logging
import sys
from typing import Any, Dict
from aiogram import Bot, Dispatcher, F, Router, html,types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

TOKEN ='7552988744:AAFF1U_dEtU6LYNVYiw_9Tw3COutD6FmbDE'

form_router = Router()

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

async def set_default_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Start bot"),
        BotCommand(command="stop", description="Yordam ma'lumotlari")
    ]
    await bot.set_my_commands(commands, scope=types.BotCommandScopeDefault())

dp = Dispatcher()

dp.include_router(form_router)

class Form(StatesGroup):
    name = State()
    like_bots = State()
    language = State()


@form_router.message(CommandStart())
async def command_start(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.name)
    await message.answer(
        "Salom menga ismingizni jo`nating.\nMasalan: (akbar)",
        reply_markup=ReplyKeyboardRemove(),
    )


@form_router.message(Command("stop"))
@form_router.message(F.text.casefold() == "stop")
async def cancel_handler(message: Message, state: FSMContext) -> None:
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info("Cancelling state %r", current_state)
    await state.clear()
    await message.answer(
        "To`xtatildi.!",
        reply_markup=ReplyKeyboardRemove(),
    )


@form_router.message(Form.name)
async def process_name(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await state.set_state(Form.like_bots)
    await message.answer(
        f"Jida yaxshi, {html.quote(message.text)}!\nUsbu botlar haqida nima deb o`ylaysiz?\nSizga yoqadi mi?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="ha"),
                    KeyboardButton(text="yo`q"),
                ]
            ],
            resize_keyboard=True,
            one_time_keyboard=True,
        ),
    )


@form_router.message(Form.like_bots, F.text.casefold() == "yo`q")
async def process_dont_like_write_bots(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    await state.clear()
    await message.answer(
        "Sizga yoqmaganidan afsusdaman.\n",
        reply_markup=ReplyKeyboardRemove(),
    )
    await show_summary(message=message, data=data, positive=False)


@form_router.message(Form.like_bots, F.text.casefold() == "ha")
async def process_like_write_bots(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.language)

    await message.reply(
        "Yaxshi siz ushnu botni qaysi dasturni qaysi\ndasturlash tili yaratilgan dep o`ylaysiz?",
        reply_markup=ReplyKeyboardRemove(),
    )


@form_router.message(Form.like_bots)
async def process_unknown_write_bots(message: Message) -> None:
    await message.reply("Sizni men tushundamandim :(")


@form_router.message(Form.language)
async def process_language(message: Message, state: FSMContext) -> None:
    data = await state.update_data(language=message.text)
    await state.clear()

    if message.text.casefold() == "python":
        await message.reply(
            "Omad siz tog`ri topdingiz 😉",
            reply_markup=ReplyKeyboardRemove(),
        )

    await show_summary(message=message, data=data)
    await state.clear()

async def show_summary(message: Message, data: Dict[str, Any], positive: bool = True) -> None:
    name = data["name"]
    language = data.get("language", "<something unexpected>")
    text = f"Sizga to`liq ma`lumot berishimdan husrsandaman {html.quote(name)}, "
    text += (
        f"Siz {html.quote(language)}  dasturlash tilida aiogram v3.15 versiyasida botlar yozishni yoqtirarsiz."
        if positive
        else "siz botni yoqtirmaysiz, lekin bu ham yaxshi, chunki har kimning o`z fikri bor."
    )
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())


async def main():

    # Start event dispatching
    await set_default_commands(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())