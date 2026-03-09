from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

router = Router()
builder = InlineKeyboardBuilder()

web_app = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🌐 Web App-ni ochish", 
                web_app=WebAppInfo(url="https://mirsaidcoder.uz"))
        ]
    ]
)

@router.message(CommandStart())
async def start_cmd(message: Message):
    emoji = '<tg-emoji emoji-id="5415765090932641459">🌙</tg-emoji>'
    emoji2 = '<tg-emoji emoji-id="5471927376080280073">💪</tg-emoji>'
    emoji1 = '<tg-emoji emoji-id="5472367477084134145">📲</tg-emoji>'
    emoji1 = '<tg-emoji emoji-id="5472367477084134145">📲</tg-emoji>'
    await message.answer(f"""
{emoji} <b>Assalomu alaykum!

{emoji1} O'zbekistondagi yagona jonli va aktiv obunachi qo'shuvchi WebApp botga xush kelibsiz!

{emoji2} Qanday ishlaydi?

Kanallarga a'zo bo'ling va do'stlarni taklif qilib pul ishlang.

Yig'ilgan mablag'ga obunachi yoki ko'rishlar buyurtma bering.

 Tezkor buyurtma: "Profil" bo'limidan hisobingizni to'ldiring va darhol obunachi oling!</b>
""",
reply_markup=web_app,
parse_mode="HTML")

def register(dp):
    dp.include_router(router)