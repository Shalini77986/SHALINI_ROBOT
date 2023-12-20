import asyncio
from platform import python_version as pyver

from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telethon import __version__ as tver

from MukeshRobot import SUPPORT_CHAT, pbot,BOT_USERNAME, OWNER_ID,BOT_NAME,START_IMG

PHOTO = [
    "https://telegra.ph/file/cdd0704cbe33240c9053c.jpg",
    "https://telegra.ph/file/3c23beb6c11abd0755ea6.jpg",
    "https://telegra.ph/file/a4e1a354023473403dd4c.jpg",
    "https://telegra.ph/file/5adf2c647d8e0f1a1acb3.jpg",
    "https://telegra.ph/file/091b2d70779a71ea74063.jpg",
]

Mukesh = [
    [
        InlineKeyboardButton(text="ᴍᴀɪɴᴛᴀɪɴᴇʀ", user_id=OWNER_ID),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]



@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("💞")
    await asyncio.sleep(0.2)
    await accha.edit("ꨄ︎ ʟᴏᴀᴅɪɴɢ..")
    await asyncio.sleep(0.1)
    await accha.edit("ꨄ︎ ʟᴏᴀᴅɪɴɢ......")
    await asyncio.sleep(0.1)
    await accha.edit("ꨄ︎ ʟᴏᴀᴅᴇᴅ..")

    await accha.delete()
    await asyncio.sleep(0.3)
    umm = await m.reply_sticker(
        "CAACAgUAAxkBAAELAAHyZYL5A3zZUwZ0bqxAQISYLaI3dQcAAj0LAALUmSlXg8dEg-__JsEzBA"
    )
    await umm.delete()
    await asyncio.sleep(0.2)
    await m.reply_photo(
        START_IMG,
        caption=f"""**ʜᴇʏ, ɪ ᴀᴍ 『[{BOT_NAME}](f"t.me/{BOT_USERNAME}")』**
   ━━━━━━━━━━━━━━━━━━━
  » **ᴍʏ ᴏᴡɴᴇʀ :** [ᴏᴡɴᴇʀ](tg://user?id={OWNER_ID})
  
  » **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{lver}`
  
  » **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tver}`
  
  » **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pver}`
  
  » **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{pyver()}`
   ━━━━━━━━━━━━━━━━━━━""",
        reply_markup=InlineKeyboardMarkup(Mukesh),
    )
