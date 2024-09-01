from pyrogram import Client, filters 
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery
import random
import datetime
from pyrogram.errors import UserNotParticipant


force_channel = "MLMDubbedMovies1"

SOULTG = Client(
    name="MLMTGRobot",
    api_id= "23050566",
    api_hash= "25e954ccd4afb778eea69bd6754275ff",
    bot_token= "6765813090:AAE6MgNRL6GeHGPPalhJf7fXv875gv4nSs0"
)

PICS = [
 "https://telegra.ph/file/9befe93227525cc5de3d7.jpg",
 "https://telegra.ph/file/a04afd5b0353d65c07050.jpg",
 "https://telegra.ph/file/1a3f98bd9e7eb4ea8d4ba.jpg",
 "https://telegra.ph/file/0922c5d8e5a378e716beb.jpg",
 "https://telegra.ph/file/693f33f82212da4b1dfc1.jpg",
 "https://telegra.ph/file/08627a85ed831456f6797.jpg"
]

@SOULTG.on_message(filters.command("start"))
async def start_cmd(client, message):
    if force_channel:
        try:
            user = await client.get_chat_member(force_channel, message.from_user.id)
            if user.status == "kicked out":
                await message.reply_text("You Are Banned")
                return
        except UserNotParticipant :
            await message.reply_text(
                text="Sᴏʀʀy Dᴜᴅᴇ Yᴏᴜ'ʀᴇ Nᴏᴛ Jᴏɪɴᴇᴅ My Cʜᴀɴɴᴇʟ 😐. Sᴏ Pʟᴇᴀꜱᴇ Jᴏɪɴ Oᴜʀ Uᴩᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ Tᴏ Cᴄᴏɴᴛɪɴᴜᴇ",
                reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("Join Update Channel 📣", url=f"t.me/{force_channel}")
                 ]]
                 )
            )
            return
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=START_MESSAGE.format{get} (message.from_user.mention),
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("CHANNEL 📢", url="t.me/ManjuUpdates"),
            ],[
            InlineKeyboardButton("CREATOR 👨‍💻", url="www.github.com/SOULTG/"),
            InlineKeyboardButton("SUPPORT 🗣", url="t.me/SoulBotzz")
            ]]
            )
        )
