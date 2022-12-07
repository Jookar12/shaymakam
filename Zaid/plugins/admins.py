from telethon import events, Button
from Zaid import Zaid
from Zaid.status import *
from Config import Config
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import ExportChatInviteRequest

@Zaid.on(events.callbackquery.CallbackQuery(data="admin"))
async def _(event):

    await event.edit(ADMIN_TEXT, buttons=[[Button.inline("« گەڕانەوە", data="help")]])

@Zaid.on(events.callbackquery.CallbackQuery(data="play"))
async def _(event):

    await event.edit(PLAY_TEXT, buttons=[[Button.inline("« گەڕانەوە", data="help")]])


ADMIN_TEXT = """
**✘ مۆدیولێک کە بەڕێوەبەرەکانی چاتەکە دەتوانن بەکاری بهێنن**

‣ `?end` - بۆ کۆتایی پێهێنانی تەوژمەکانی مۆسیقا.
‣ `?skip` - بۆ سکیپ کردن.
‣ `?pause` - بۆ وەستاندن.
‣ `?resume` - بۆ وەستاندن.
‣ `?leavevc` - ناچارکردنی Userbot بۆ جێهێشتنی وی سی چات (هەندێک جار پەیوەندی کراوە).
‣ `?playlist` - بۆ پشکنینی لیستەکانی پەخشکردن.
"""

PLAY_TEXT = """
**✘ مۆدیولێک کە بەڕێوەبەرەکانی چاتەکە دەتوانن بەکاری بهێنن!**

‣ `?play` - بۆ پەخشکردنی دەنگ لە وەڵامدانەوەی تر بۆ فایلی دەنگ.
‣ `?vplay` - بۆ ڤیدیۆکانی لێشاو.
"""
