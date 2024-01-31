from Zaid import app, API_ID, API_HASH
from config import OWNER_ID, ALIVE_PIC
from pyrogram import filters
import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import * 

PHONE_NUMBER_TEXT = (
    "✘ ʜʟᴏ ɢᴜʏs 👋!\n\n✘ ɪ ᴀᴍ ʏᴏᴜʀ ᴀssɪsᴛᴀɴᴛ\n\n‣ ɪ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ʜᴏsᴛ ʏᴏᴜʀ ʟᴇғᴛ ᴄʟɪᴇɴᴛs .\n\n‣ ᴛʜɪs sᴘᴇᴄɪᴀʟʟʏ ғᴏʀ ʙᴜᴢᴢʏ ᴘᴇᴏᴘʟᴇ (ʟᴀᴢʏ)\n\n‣ ɴᴏᴡ /clone {sᴇɴᴅ ʏᴏᴜʀ ᴘʏʀᴏɢʀᴀᴍ sᴛʀɪɴɢ sᴇssɪᴏɴ}"
)

@app.on_message(filters.user(OWNER_ID) & filters.command("start"))
async def hello(client: app, message):
    buttons = [
           [
                InlineKeyboardButton(" 🕊️⃝‌ٖٖٖٖ ‌ٖٖٖٖٖ𝐁α∂ ❤️ᥫ᭡፝֟፝֟", url="t.me/II_BAD_BBY_II"),
            ],
            [
                InlineKeyboardButton("🕊️⃝‌ٖٖٖٖ ‌ٖٖٖٖٖ𝐔ρ∂αтє ❤️ᥫ᭡፝֟፝֟", url="t.me/ll_THE_BAD_BOT_ll"),
            ],
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, ALIVE_PIC, caption=PHONE_NUMBER_TEXT, reply_markup=reply_markup)

# © By Itz-Zaid Your motherfucker if uh Don't gives credits.
@app.on_message(filters.user(OWNER_ID) & filters.command("clone"))
async def clone(bot: app, msg: Message):
    chat = msg.chat
    text = await msg.reply("Usage:\n\n /clone session")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("Booting Your Client")
                   # change this Directry according to ur repo
        client = Client(name="Melody", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="Pbx1.0/modules"))
        await client.start()
        user = await client.get_me()
        await msg.reply(f"Your Client Has Been Successfully As {user.first_name} ✅.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
