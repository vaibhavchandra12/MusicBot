from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import SUPPORT_GROUP,UPDATES_CHANNEL,BOT_USERNAME
from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAELcSphJP9zfZgHUVwbgJr3ctDcwXj2rAACuAcAArHWCFUxMUPx-GRPIiAE")
    await message.reply_text(
        f"""Hey 👋 
I am Carvinal Music Bot, Use me to play music in your groups Voice Chat.
Hosted On VPS, So no lag
✅Need Help /help
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 Support", url="https://t.me/AddySupport"
                    ),
                    InlineKeyboardButton(
                        "🔊 Updates", url="https://t.me/AddyUpdates"
                    ),
                    InlineKeyboardButton(
                        "Owner😎", url="https://t.me/AddyxD"
                    )
                ],
                [ 
                    InlineKeyboardButton(
                        "🤔Commands", url="https://t.me/AddyUpdates/2"
                    )],
                [ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/CarvinalMusicBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )
            # Kanged by @AddyxD
@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**One Music Bot Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Help🤔", url="https://t.me/AddySupport")
                ]
            ]
        )
   )


