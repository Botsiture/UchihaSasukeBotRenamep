
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from helper.database import jishubotz
from config import Config, Txt  
  

@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user = message.from_user
    await jishubotz.add_user(client, message)                
    button = InlineKeyboardMarkup([
        [InlineKeyboardButton("᪥ sᴜᴘᴘᴏʀᴛ ᪥", url='https://t.me/NARUTO_PUBLIC'),
        InlineKeyboardButton("᪥ ᴜᴘᴅᴀᴛᴇ ᪥", url='https://t.me/Sand_Village')],
        [InlineKeyboardButton("᪥ ᴀʙᴏᴜᴛ ᪥", callback_data='about'),
        InlineKeyboardButton("᪥ ʜᴇʟᴘ ᪥", callback_data='help')],
        [InlineKeyboardButton("᯽ ɴᴀʀᴜᴛᴏ sʜɪᴘᴘᴜᴅᴇɴ ᯽", url='https://t.me/Naruto_Public')]
    ])
    if Config.START_PIC:
        await message.reply_photo(Config.START_PIC, caption=Txt.START_TXT.format(user.mention), reply_markup=button)       
    else:
        await message.reply_text(text=Txt.START_TXT.format(user.mention), reply_markup=button, disable_web_page_preview=True)
   

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=Txt.START_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton("᪥ sᴜᴘᴘᴏʀᴛ ᪥", url='https://t.me/NARUTO_PUBLIC'),
                InlineKeyboardButton("᪥ ᴜᴘᴅᴀᴛᴇ ᪥", url='https://t.me/Sand_Village')],
                [InlineKeyboardButton("᪥ ᴀʙᴏᴜᴛ ᪥", callback_data='about'),
                InlineKeyboardButton("᪥ ʜᴇʟᴘ ᪥", callback_data='help')],
                [InlineKeyboardButton("᯽ ɴᴀʀᴜᴛᴏ sʜɪᴘᴘᴜᴅᴇɴ ᯽", url='https://t.me/Naruto_Public')]
            ])
        )
    elif data == "help":
        await query.message.edit_text(
            text=Txt.HELP_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("᯽ ᴅᴇᴠᴇʟᴏᴘᴇʀ ᯽", url="http://t.me/iMSASUKESi")],
                [InlineKeyboardButton("⪻ ʙᴀᴄᴋ", callback_data = "start"),
                InlineKeyboardButton("ᴄʟᴏsᴇ ⪼", callback_data = "close")]
            ])            
        )
    elif data == "about":
        await query.message.edit_text(
            text=Txt.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("᯽ ʏᴏᴜ ᴛᴜʙᴇ ᯽", url="https://youtube.com/@lyrics_1m")],
                [InlineKeyboardButton("⪻ ʙᴀᴄᴋ", callback_data = "start"),
                InlineKeyboardButton("ᴄʟᴏsᴇ ⪼", callback_data = "close")]
            ])            
        )
    elif data == "close":
       try:
        if query.message.reply_to_message:
            await query.message.reply_to_message.delete()

        await query.message.delete()

    except Exception as e:
        print(e)




@Client.on_message(filters.private & filters.command(["donate", "d"]))
async def donate(client, message):
	text = Txt.DONATE_TXT
	keybord = InlineKeyboardMarkup([
        			[InlineKeyboardButton("◎ ᴀᴅᴍɪɴ ◎",url = "http://t.me/iMSASUKESi"), 
        			InlineKeyboardButton("◎ ᴄʟᴏsᴇ ◎",callback_data = "close") ]])
	await message.reply_text(text = text,reply_markup = keybord)



# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @JishuBotz
# Developer @JishuDeveloper
