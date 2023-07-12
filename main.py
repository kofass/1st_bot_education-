from aiogram import Bot, types
from aiogram.utils import executor
import asyncio
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
import config
import keyboard
import logging


storage = MemoryStorage()
bot = Bot(token=config.botkey, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(format=u"%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s",
                    level=logging.INFO)

@dp.message_handler(Command("start"), state=None)
async def welcome(message):
    joinedFile = open("user.txt", 'r')
    joinedUsers = set()
    for line in joinedFile:
        joinedUsers.add(line.strip())

    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("user.txt", 'a')
        joinedFile.write(str(message.chat.id) + '\n')
        joinedUsers.add(message.chat.id)

    await message.answer(text=f"Hello, *{message.from_user.first_name},* BOT IS WORKING",
                           reply_markup=keyboard.inline_help_keyboard, parse_mode="Markdown")

# @dp.message_handler(content_types=['text'])
# async def get_message(message):
#     if message.text == "Information":
#         await bot.send_message(message.chat.id,
#                                text="_Information_\nBot was created for educational reasons",
#                                parse_mode="Markdown")
#     elif message.text == "I am":
#         await bot.send_message(message.chat.id,
#                                text=f"***Information about user***\n{message.from_user.username}",parse_mode="Markdown")
@dp.callback_query_handler()
async def callback_info(callback):
    if callback.data == "info":
        await callback.message.answer("This bot was created for an educational reason.")
    elif callback.data == "literature":
        await callback.message.answer("Here you will find some books:"
                               "\nhttps://wiki.python.org/moin/PythonBooks"
                               "\nhttps://wiki.python.org/moin/PythonBooks"
                               "\nhttps://realpython.com/best-python-books/\n etc.")

if __name__ == '__main__':
    print("bot is running")
    executor.start_polling(dp)