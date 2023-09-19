import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"
 🤖 ᴍʏ ɴᴀᴍᴇ : {}
 👨‍💻 ᴄʀᴇᴀᴛᴏʀ : <a href='https://t.me/XAYOONARA'>𝑿𝑨𝒀𝑶𝑵𝑨𝑹𝑨</a>
 📚 ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a>
 📝 ʟᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/download/releases/3.0/'>ᴘʏᴛʜᴏɴ 3</a>
 ♻️ ᴅᴀᴛᴀ ʙᴀsᴇ : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏ ᴅʙ</a>
 📡 ʜᴏsᴛᴇᴅ ᴏɴ  : <a href='https://www.heroku.com/'>Heroku</a>
 🥶 ʙᴜɪʟᴅ sᴛᴀᴛᴜs : ᴠ3.0 [sᴛᴀʙʟᴇ]",quote=True)
