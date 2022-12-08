from telethon import events, Button
from Zaid import Zaid, BOT_USERNAME
from Config import Config


btn =[
    [Button.inline("ئەدمین", data="admin"), Button.inline("پەخش کردن", data="play")],
    [Button.inline("سەرەتا", data="start")]]

HELP_TEXT = "بەخێربێیت بۆ لیستی یارمەتیدان Section\n\nClick on the Buttons!"


@Zaid.on(events.NewMessage(pattern="[!?/]help"))
async def help(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_group:
       await event.reply("پەیوەندیم پێوە بکە لە PM بۆ بەدەستهێنانی لیستی یارمەتی بەردەست", buttons=[
       [Button.url("یارمەتی و فەرمانەکان", "t.me/{}?start=help".format(BOT_USERNAME))]])
       return

    await event.reply(HELP_TEXT, buttons=btn)

@Zaid.on(events.NewMessage(pattern="^/start help"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    await event.reply(HELP_TEXT, buttons=btn)

@Zaid.on(events.callbackquery.CallbackQuery(data="help"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    await event.edit(HELP_TEXT, buttons=btn)
