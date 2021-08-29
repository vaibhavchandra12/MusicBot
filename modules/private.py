from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import SUPPORT_GROUP,UPDATES_CHANNEL,BOT_USERNAME
from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAEGU0JhK49gLY2KvJUabs-p1A8BOUtFXgACBAMAAmA2WVUykujmd_XWISAE")
    await message.reply_text(
        f"""𝐇𝐞𝐲 👋 
𝐈 𝐚𝐦 𝐂𝐚𝐫𝐯𝐢𝐧𝐚𝐥 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭, 𝐔𝐬𝐞 𝐦𝐞 𝐭𝐨 𝐩𝐥𝐚𝐲 𝐦𝐮𝐬𝐢𝐜 𝐢𝐧 𝐲𝐨𝐮𝐫 𝐠𝐫𝐨𝐮𝐩𝐬 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭.
𝐇𝐨𝐬𝐭𝐞𝐝 𝐎𝐧 𝐕𝐏𝐒, 𝐒𝐨 𝐧𝐨 𝐥𝐚𝐠
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url="https://t.me/AddySupport"
                    ),
                    InlineKeyboardButton(
                        "🔊 𝐔𝐩𝐝𝐚𝐭𝐞𝐬", url="https://t.me/AddyUpdates"
                    )
                ],
                [ 
                    InlineKeyboardButton(
                        "🤔𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬", url="https://t.me/AddyUpdates/5"
                    )],
                [ 
                    InlineKeyboardButton(
                        "➕ 𝐀𝐝𝐝 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ➕", url="https://t.me/CarnivalMusicBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )
            # Kanged by @AddyxD
@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""𝐎𝐧𝐞 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 𝐎𝐧𝐥𝐢𝐧𝐞 ✅""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Help🤔", url="https://t.me/AddySupport")
                ]
            ]
        )
   )


