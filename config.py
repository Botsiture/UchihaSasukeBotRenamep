import os, time, re
id_pattern = re.compile(r'^-?\d+$')



class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "10658015")
    API_HASH  = os.environ.get("API_HASH", "a0087bca748f86698c53d291c9e5b3af")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","Cluster0")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get("ADMIN", "7657218453").split()]

    # channels logs
    FORCE_SUB   = os.environ.get("FORCE_SUB", "Sand_Village") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))

    # wes response configuration     
    WEBHOOK = os.environ.get("WEBHOOK", "True") == "True"



class Txt(object):
    # part of text configuration
    START_TXT = """**Hᴇy {} Darling ✨**
╭───────────────⋗
├⋗ **ɪ'ᴍ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴅ ʏᴇᴛ**
├⋗ **ᴘᴏᴡᴇʀғᴜʟ ʀᴇɴᴀᴍᴇ ʙᴏᴛ.**
├⋗ **ᴜsɪɴɢ ᴛʜɪs ʙᴏᴛ ʏᴏᴜ ᴄᴀɴ sᴇᴛ**
├⋗ **ᴛʜᴜᴍʙɴᴀɪʟ ᴏғ ʏᴏᴜʀ ғɪʟᴇs.**
├⋗ **ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴄᴏɴᴠᴇʀᴛ ᴠɪᴅᴇᴏ**
├⋗ **ᴛᴏ ғɪʟᴇ ᴀɴᴅ ғɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ.**
╰───────────────────⋗
"""

    ABOUT_TXT = """
╭────────────────⋗
├⋗<b> Mʏ Nᴀᴍᴇ</b> : **{}**
├⋗<b> Oᴡɴᴇʀ</b> : <a href=http://t.me/iMSASUKESi>**ＩＭ 𖣘︎ ＵＣＨＩＨＡ**</a> 
├⋗<b> Gʀᴏᴜᴘ</b> : <a href=https://t.me/SAND_VILLAGE>**𝐒ᴧηԃ 友 𝐕𝛊ʅʅᴧɠҽ**</a>
├⋗<b> Cʜᴀɴɴᴇʟ</b> : <a href=https://t.me/NARUTO_PUBLIC>𝐍𝐀𝐑𝐔𝐓𝐎 🌀</a>     
╰──────────────────⋗
"""

    HELP_TXT = """
🌌 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴᴀɪʟ</u></b>
  
➪ /start - Sᴛᴀʀᴛ Tʜᴇ Bᴏᴛ Aɴᴅ Sᴇɴᴅ Aɴʏ Pʜᴏᴛᴏ Tᴏ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ Sᴇᴛ Tʜᴜᴍʙɴᴀɪʟ.
➪ /del_thumb - Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴᴀɪʟ.
➪ /view_thumb - Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴᴀɪʟ.

📑 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ</u></b>

➪ /set_caption - Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ A Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ
➪ /see_caption - Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ
➪ /del_caption - Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ
➪ Exᴀᴍᴘʟᴇ - <code>/Set_caption 📕 Nᴀᴍᴇ ➠ : {filename}

🔗 Sɪᴢᴇ ➠ : {filesize} 

⏰ Dᴜʀᴀᴛɪᴏɴ ➠ : {duration}</code>

✏️ <b><u>ʜᴏᴡ ᴛᴏ ʀᴇɴᴀᴍᴇ ᴀ ғɪʟᴇ</u></b>

➪ sᴇɴᴛ ᴀɴʏ ғɪʟᴇ ᴀɴᴅ ᴛʏᴘᴇ ɴᴇᴡ ғɪʟᴇ ɴᴀᴍᴇ ᴀɴᴅ sᴇʟᴇᴄᴛ ᴛʜᴇ ғᴏʀᴍᴀᴛ [ ᴅᴏᴄᴜᴍᴇɴᴛ, ᴠɪᴅᴇᴏ, ᴀᴜᴅɪᴏ ].           

**Aɴʏ Qᴜᴇʀʏ ⌯ **<a href=http://t.me/iMSASUKESi>**ＩＭ 𖣘︎ ＵＣＨＩＨＡ**</a>
"""

    PROGRESS_BAR = """\n
 <b>🔗 Sɪᴢᴇ :</b> {1} | {2}
️ <b>⏳️ Dᴏɴᴇ :</b> {0}%
 <b>🚀 Sᴘᴇᴇᴅ :</b> {3}/s
️ <b>⏰️ ETA :</b> {4}
"""

    DONATE_TXT = """
<b>🥲 ᴛʜᴀɴᴋs ғᴏʀ sʜᴏᴡɪɴɢ ɪɴᴛᴇʀᴇsᴛ ɪɴ ᴅᴏɴᴀᴛɪᴏɴ! ❤️</b>

ɪғ ʏᴏᴜ ʟɪᴋᴇ ᴍʏ ʙᴏᴛs & ᴘʀᴏᴊᴇᴄᴛs, ʏᴏᴜ ᴄᴀɴ 🎁 ᴅᴏɴᴀᴛᴇ ᴍᴇ ᴀɴʏ ᴀᴍᴏᴜɴᴛ ғʀᴏᴍ 𝟷𝟶 ʀs ᴜᴘᴛᴜ ʏᴏᴜʀ ᴄʜᴏɪᴄᴇ.

<b>🛍 UPI ID:</b> `sasuke72@ptyes`
"""


    SEND_METADATA = """<b><u>🖼️  HOW TO SET CUSTOM METADATA</u></b>

ғᴏʀ ᴇxᴀᴍᴘʟᴇ! 

<code>By ❃ SAND VILLAGE</code>

💬 **ғᴏʀ ᴀɴʏ ʜᴇʟᴘ ᴄᴏɴᴛᴀᴄᴛ** @iMSASUKESi
"""








# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @JishuBotz
# Developer @JishuDeveloper
