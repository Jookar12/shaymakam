from Zaid import Zaid, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
بەخێربێت! {}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ **من مۆسیقایەکی سادەی تەلگرام و بۆتێکی بەڕێوەبردنم**.
‣ **دەتوانم بە دەنگی تۆ گۆرانی بژەنم**.
‣ ** من نزیکەی هەموو تایبەتمەندیەکانم هەیە کە پێویستی بە بۆتێکی مۆسیقا هەیە ئەم بۆتەیە لەسەر بنەمای تەلەفۆنە**
‣ **کەواتە جێگیری زیاتر دابین دەکات لە ڕووەکەکانی تر**!
‣ **من دەتوانم شتی تر بکەم وەک پین و هتد**.
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ **کرتە بکە لەسەر یارمەتی بۆتۆن 🔘 بۆ زانیاریi️ زیاتر**.
"""

@Zaid.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("➕ زیادی گرووپەکەتم بکە", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👨‍💻 دەسکاری مەکە", "https://github.com/ITZ-ZAID/Telethon-Music")],
        [Button.url("🗣️ گرووپەکەم", f"https://t.me/{Config.SUPPORT}"), Button.url("📣 چەناڵەکەم", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("داوای یارمەتی کردن", data="help")]])
       return

    if event.is_group:
       await event.reply("**ʜᴇʏ! ɪ'ᴍ ꜱᴛɪʟʟ ᴀʟɪᴠᴇ ✅**")
       return



@Zaid.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ زیادی گرووپەکەتم بکە", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👨‍💻 دەسکاری مەکە", "https://github.com/ITZ-ZAID/Telethon-Music")],
        [Button.url("🗣️ گرووپەکەم", f"https://t.me/{Config.SUPPORT}"), Button.url("📣 چەناڵەکەم", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("داوای یارمەتی کردن", data="help")]])
       return
