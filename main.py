from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from keyboards import test, scale1
import sqlite3
from db.graph import *
from test import *
import os

from db.excel_func import *

bot = Bot(token='6064231364:AAGB_5W5CVaj56N5lnwFIvs4EYLYJQswKMg')
dp = Dispatcher(bot)
conn = sqlite3.connect('test.db', check_same_thread=False)
cursor = conn.cursor()
users = []
ar = []
answers = ["-3", "-2", "-1", "0", "1", "2", "3"]


async def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
    try:
        cursor.execute('INSERT INTO test (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
                       (user_id, user_name, user_surname, username))
        conn.commit()
    except:

        cursor.execute(
            'UPDATE test SET question1 = ? , question2 = ?, question3 = ?, question4 = ?, question5 = ?,'
            ' question6 = ? , question7 = ?, question8 = ?, question9 = ? WHERE user_id = ?;',
            (100, 100, 100, 100, 100, 100, 100, 100, 100, user_id))
        conn.commit()


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    kb = [[types.KeyboardButton(text="Вперёд!")]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True)
    await message.answer("Здравствуй, друг!\n"
                         "С тобой на связи команда “Food Mood”\n"
                         "Мы занимаемся исследованиями в области питания и того, "
                         "как оно влияет на эмоциональное состояние человека.\n"
                         "Давай узнаем, какие блюда тебе стоит заказать, чтобы чувствовать себя лучше!",
                         reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Вперёд!")
async def choose(message: types.Message):
    us_id = message.from_user.id
    us_name = message.from_user.first_name
    us_sname = message.from_user.last_name
    username = message.from_user.username
    await db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)
    await message.answer(text="Какое у тебя сейчас настроение? "
                              "Обратите внимание на свое эмоциональное состояние и ответь на следующие вопросы!",
                         reply_markup=test)


@dp.callback_query_handler(text="test")
async def question1(callback: types.CallbackQuery):
    kb = [[types.KeyboardButton(text="Вы чувствуете сонливость на -3")],
          [types.KeyboardButton(text="Вы чувствуете сонливость на -2")],
          [types.KeyboardButton(text="Вы чувствуете сонливость на -1")],
          [types.KeyboardButton(text="Вы чувствуете сонливость на 0")],
          [types.KeyboardButton(text="Вы чувствуете сонливость на 1")],
          [types.KeyboardButton(text="Вы чувствуете сонливость на 2")],
          [types.KeyboardButton(text="Вы чувствуете сонливость на 3")]]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True)

    await callback.message.answer("Чувствуете ли Вы сонливость в данный момент?",
                                  reply_markup=keyboard)


@dp.message_handler(lambda message: "сонливость" in message.text)
async def question2(message: types.Message):
    us_id = message.from_user.id
    ans = message.text.split()
    kb = [[types.KeyboardButton(text="Меня преследуют навязчивые мысли на -3")],
          [types.KeyboardButton(text="Меня преследуют навязчивые мысли на -2")],
          [types.KeyboardButton(text="Меня преследуют навязчивые мысли на -1")],
          [types.KeyboardButton(text="Меня преследуют навязчивые мысли на 0")],
          [types.KeyboardButton(text="Меня преследуют навязчивые мысли на 1")],
          [types.KeyboardButton(text="Меня преследуют навязчивые мысли на 2")],
          [types.KeyboardButton(text="Меня преследуют навязчивые мысли на 3")]]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True)

    cursor.execute(
        'UPDATE test SET question1 = ? WHERE user_id = ?;',
        (int(ans[-1]), us_id))
    conn.commit()

    await message.answer("Преследуют ли Вас сегодня навязчивые мысли?",
                         reply_markup=keyboard)


@dp.message_handler(lambda message: "навязчивые" in message.text)
async def question3(message: types.Message):
    us_id = message.from_user.id
    ans = message.text.split()
    kb = [[types.KeyboardButton(text="Я удовлевтворён сегодняшним днём на -3")],
          [types.KeyboardButton(text="Я удовлевтворён сегодняшним днём на -2")],
          [types.KeyboardButton(text="Я удовлевтворён сегодняшним днём на -1")],
          [types.KeyboardButton(text="Я удовлевтворён сегодняшним днём на 0")],
          [types.KeyboardButton(text="Я удовлевтворён сегодняшним днём на 1")],
          [types.KeyboardButton(text="Я удовлевтворён сегодняшним днём на 2")],
          [types.KeyboardButton(text="Я удовлевтворён сегодняшним днём на 3")]]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True)

    cursor.execute(
        'UPDATE test SET question2 = ? WHERE user_id = ?;',
        (int(ans[-1]), us_id))
    conn.commit()

    await message.answer("Удовлетворены ли Вы сегодняшним днём?",
                         reply_markup=keyboard)


@dp.message_handler(lambda message: "сегодняшним" in message.text)
async def question4(message: types.Message):
    us_id = message.from_user.id
    ans = message.text.split()
    kb = [[types.KeyboardButton(text="Принимать решения в течение дня было тяжело на -3")],
          [types.KeyboardButton(text="Принимать решения в течение дня было тяжело на -2")],
          [types.KeyboardButton(text="Принимать решения в течение дня было тяжело на -1")],
          [types.KeyboardButton(text="Принимать решения в течение дня было тяжело на 0")],
          [types.KeyboardButton(text="Принимать решения в течение дня было тяжело на 1")],
          [types.KeyboardButton(text="Принимать решения в течение дня было тяжело на 2")],
          [types.KeyboardButton(text="Принимать решения в течение дня было тяжело на 3")]]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True)

    cursor.execute(
        'UPDATE test SET question3 = ? WHERE user_id = ?;',
        (int(ans[-1]), us_id))
    conn.commit()

    await message.answer("Принимать решения в течение дня было?",
                         reply_markup=keyboard)


@dp.message_handler(lambda message: "решения" in message.text)
async def question5(message: types.Message):
    us_id = message.from_user.id
    ans = message.text.split()
    kb = [[types.KeyboardButton(text="Окружающие люди сегодня радуют на -3")],
          [types.KeyboardButton(text="Окружающие люди сегодня радуют на -2")],
          [types.KeyboardButton(text="Окружающие люди сегодня радуют на -1")],
          [types.KeyboardButton(text="Окружающие люди сегодня радуют на 0")],
          [types.KeyboardButton(text="Окружающие люди сегодня радуют на 1")],
          [types.KeyboardButton(text="Окружающие люди сегодня радуют на 2")],
          [types.KeyboardButton(text="Окружающие люди сегодня радуют на 3")]]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True)

    cursor.execute(
        'UPDATE test SET question4 = ? WHERE user_id = ?;',
        (int(ans[-1]), us_id))
    conn.commit()

    await message.answer("Окружающие люди сегодня Вас (радуют/злят)",
                         reply_markup=keyboard)


@dp.message_handler(lambda message: "радуют" in message.text)
async def question6(message: types.Message):
    us_id = message.from_user.id
    ans = message.text.split()
    kb = [[types.KeyboardButton(text="Чувствую себя активным на -3")],
          [types.KeyboardButton(text="Чувствую себя активным на -2")],
          [types.KeyboardButton(text="Чувствую себя активным на -1")],
          [types.KeyboardButton(text="Чувствую себя активным на 0")],
          [types.KeyboardButton(text="Чувствую себя активным на 1")],
          [types.KeyboardButton(text="Чувствую себя активным на 2")],
          [types.KeyboardButton(text="Чувствую себя активным на 3")]]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True)

    cursor.execute(
        'UPDATE test SET question5 = ? WHERE user_id = ?;',
        (int(ans[-1]), us_id))
    conn.commit()

    await message.answer(
        "Если бы Вы сегодня были абсолютно свободными, то: (заполнили бы день активностями, которые давно хотели опробовать/остались бы дома)",
        reply_markup=keyboard)


@dp.message_handler(lambda message: "активным" in message.text)
async def question7(message: types.Message):
    us_id = message.from_user.id
    ans = message.text.split()
    kb = [[types.KeyboardButton(text="Сталкивался со сложным выбором на -3")],
          [types.KeyboardButton(text="Сталкивался со сложным выбором на -2")],
          [types.KeyboardButton(text="Сталкивался со сложным выбором на -1")],
          [types.KeyboardButton(text="Сталкивался со сложным выбором на 0")],
          [types.KeyboardButton(text="Сталкивался со сложным выбором на 1")],
          [types.KeyboardButton(text="Сталкивался со сложным выбором на 2")],
          [types.KeyboardButton(text="Сталкивался со сложным выбором на 3")]]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True)

    cursor.execute(
        'UPDATE test SET question6 = ? WHERE user_id = ?;',
        (int(ans[-1]), us_id))
    conn.commit()

    await message.answer("Сталкивались ли Вы сегодня со сложным выбором?",
                         reply_markup=keyboard)


@dp.message_handler(lambda message: "сложным" in message.text)
async def question8(message: types.Message):
    us_id = message.from_user.id
    ans = message.text.split()
    kb = [[types.KeyboardButton(text="Я оцениваю свой день на -3")],
          [types.KeyboardButton(text="Я оцениваю свой день на -2")],
          [types.KeyboardButton(text="Я оцениваю свой день на -1")],
          [types.KeyboardButton(text="Я оцениваю свой день на 0")],
          [types.KeyboardButton(text="Я оцениваю свой день на 1")],
          [types.KeyboardButton(text="Я оцениваю свой день на 2")],
          [types.KeyboardButton(text="Я оцениваю свой день на 3")]]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True)

    cursor.execute(
        'UPDATE test SET question7 = ? WHERE user_id = ?;',
        (int(ans[-1]), us_id))
    conn.commit()

    await message.answer("Каким Вы запомните сегодняшний день?",
                         reply_markup=keyboard)


@dp.message_handler(lambda message: "день" in message.text)
async def question9(message: types.Message):
    us_id = message.from_user.id
    ans = message.text.split()
    kb = [[types.KeyboardButton(text="-3")],
          [types.KeyboardButton(text="-2")],
          [types.KeyboardButton(text="-1")],
          [types.KeyboardButton(text="0")],
          [types.KeyboardButton(text="1")],
          [types.KeyboardButton(text="2")],
          [types.KeyboardButton(text="3")]]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True)

    cursor.execute(
        'UPDATE test SET question8 = ? WHERE user_id = ?;',
        (int(ans[-1]), us_id))
    conn.commit()

    await message.answer("Последнее время Вы чаще (злитесь/расстраиваетесь)",
                         reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in answers)
async def question10(message: types.Message):
    us_id = message.from_user.id
    ans = message.text.split()

    kb = [[types.KeyboardButton(text="Далее!")]]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    cursor.execute(
        'UPDATE test SET question9 = ? WHERE user_id = ?;',
        (int(ans[-1]), us_id))
    conn.commit()

    await message.answer("Получить график!",
                         reply_markup=keyboard)


@dp.message_handler(lambda message: "Далее!" in message.text)
async def send_graph(message: types.Message):
    a = []
    cursor.execute("SELECT user_id, question1, question2, question3, question4, question5, question6, question7, "
                   "question8, question9 FROM test")
    rows = cursor.fetchall()
    for i in rows:
        for j in range(len(i)):
            if i[j] == message.from_user.id:
                a = i[1:10]
                print(type(a), a)
            break
        break

    ans = [sadness(a), fear(a), rage(a), happiness(a), calm(a)]
    draw_graph(ans)

    photo = open('foo.png', 'rb')
    await bot.send_photo(message.from_user.id, photo)
    os.remove('foo.png')


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)
