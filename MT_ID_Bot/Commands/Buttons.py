from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

START_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("🛠️ Bot Updates", url=f"t.me/mo_tech_yt"),
       InlineKeyboardButton("📝 Source Code", url=f"https://github.com/PR0FESS0R-99/ID-Bot")
       ],[
       InlineKeyboardButton("🔙 More Information 🔜", callback_data="help")
       ]]
       )

HELP_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("🆔 Telegram ID", callback_data="id"),
       InlineKeyboardButton("🆕 Telegram Info", callback_data="info")
       ],[
       InlineKeyboardButton("🏠 Beranda", callback_data="start"),
       InlineKeyboardButton("❎ Tutup", callback_data="close"),
       InlineKeyboardButton("👨🏻‍💻 Tentang", callback_data="about")
       ]]
       )

ABOUT_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("🔙 Kembali", callback_data="help"),
       InlineKeyboardButton("🏠 Beranda", callback_data="start"),
       InlineKeyboardButton("❎ Tutup", callback_data="close")
       ]]
       )
