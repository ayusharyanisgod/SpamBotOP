# By < MOHAMMAD AMAAN >
# // SPAMMERBOT MADE BY @CRIMINAL786 //

from .. import ATGK
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



