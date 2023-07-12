from aiogram import types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup,InlineKeyboardButton
#start = types.ReplyKeyboardMarkup(resize_keyboard=True)
# info = types.KeyboardButton("Information")
# stats = types.KeyboardButton("Statistics")
# my_info = types.KeyboardButton("I am")
inline_help_keyboard = types.InlineKeyboardMarkup()
inline_info_bt = types.InlineKeyboardButton(text="Information",
                                            callback_data="info")
inline_litreture_bt = types.InlineKeyboardButton(text="literature links for Python",
                                                 callback_data="literature")
#start.add(stats, info, my_info)
inline_help_keyboard.add(inline_info_bt).add(inline_litreture_bt)
