from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

# Создание кнопки "пройти тест!"
test = InlineKeyboardMarkup(row_width=2)
test_button = InlineKeyboardButton(text="Пройти тест!",
                                   resize_keyboard=True,
                                   callback_data="test")
test.add(test_button)

kb = [[types.KeyboardButton(text="-3")],
      [types.KeyboardButton(text="-2")],
      [types.KeyboardButton(text="-1")],
      [types.KeyboardButton(text="0")],
      [types.KeyboardButton(text="1")],
      [types.KeyboardButton(text="2")],
      [types.KeyboardButton(text="3")]]

keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                     resize_keyboard=True)

sc = [
    [

        types.KeyboardButton(text="-3",
                             callback_data="-3"),
        types.KeyboardButton(text="-2",
                             callback_data="-2"),
        types.KeyboardButton(text="-1",
                             callback_data="-1"),
        types.KeyboardButton(text="0",
                             callback_data="0"),
        types.KeyboardButton(text="1",
                             callback_data="1"),
        types.KeyboardButton(text="2",
                             callback_data="2"),
        types.KeyboardButton(text="3",
                             callback_data="3"),
    ],
]

scale1 = types.ReplyKeyboardMarkup(
    keyboard=sc,
    resize_keyboard=True,)

scale2 = types.ReplyKeyboardMarkup(
    keyboard=sc,
    resize_keyboard=True)

scale3 = types.ReplyKeyboardMarkup(
    keyboard=sc,
    resize_keyboard=True)

scale4 = types.ReplyKeyboardMarkup(
    keyboard=sc,
    resize_keyboard=True)

scale5 = types.ReplyKeyboardMarkup(
    keyboard=sc,
    resize_keyboard=True)


# scale1 = InlineKeyboardMarkup(row_width=2)




# sc1_b1 = InlineKeyboardButton(text="-3",
#                                    resize_keyboard=True,
#                                    callback_data="-3.1")
#
# sc1_b2 = InlineKeyboardButton(text="-2",
#                                    resize_keyboard=True,
#                                    callback_data="-2.1")
#
# sc1_b3 = InlineKeyboardButton(text="-1",
#                                    resize_keyboard=True,
#                                    callback_data="-1.1")
#
# sc1_b4 = InlineKeyboardButton(text="0",
#                                    resize_keyboard=True,
#                                    callback_data="0.1")
#
# sc1_b5 = InlineKeyboardButton(text="1",
#                                    resize_keyboard=True,
#                                    callback_data="1.1")
#
# sc1_b6 = InlineKeyboardButton(text="2",
#                                    resize_keyboard=True,
#                                    callback_data="2.1")
#
# sc1_b7 = InlineKeyboardButton(text="3",
#                                    resize_keyboard=True,
#                                    callback_data="3.1")

# scale1.add(sc1_b1).add(sc1_b2).add(sc1_b3).add(sc1_b4).add(sc1_b5).add(sc1_b6).add(sc1_b7)
