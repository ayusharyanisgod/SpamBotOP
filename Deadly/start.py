from OpUstad import UstaD, UstaD2, UstaD3, UstaD4, UstaD5, UstaD6, UstaD7, UstaD8, UstaD9, UstaD10, SUDO_USERS

from telethon import events, Button

@ATGK.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("ѕοмє ιиƒο αϐουτ οωиєя.",
                    buttons=[
                        [Button.url("οωиєя", url="https://t.me/AnonymusHu_Bot")],
                        [Button.inline("Cнєϲκ мє",data="ishu")]
                    ])

@ATGK.on(events.callbackquery.CallbackQuery(data="ishu"))
async def ex(event):
    await event.edit("υѕє τнιѕ ρℓєαѕє /help",
                    buttons=[
                        [Button.url("οωиєя", url="https://t.me/AnonymusHu_Bot")]
                    ])



