import pyrogram
import importlib
from mayuri import bot, Command, OWNER
from pyrogram import filters
from pyrogram.handlers import MessageHandler
from mayuri.modules import ALL_MODULES

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("mayuri.modules." + module_name)
    importlib.reload(imported_module)
    if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
    	imported_module.__MODULE__ = imported_module.__MODULE__

@bot.on_message(filters.command("start", Command))
async def start(client,message):
	await message.reply_text("hello!\nThis bot is under development.\nYou can contact my master [here](tg://user?id={})\n\nPowered by [Pyrogram v{}](https://pyrogram.org)".format(OWNER[0],pyrogram.__version__))

bot.run()
