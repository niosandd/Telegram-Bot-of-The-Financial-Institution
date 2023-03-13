from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from keyboards import test, scale1
import sqlite3
from graph import *
from test import *
import os

from func import *

bot = Bot(token='6064231364:AAGB_5W5CVaj56N5lnwFIvs4EYLYJQswKMg')
dp = Dispatcher(bot)
conn = sqlite3.connect('db/test.db', check_same_thread=False)
cursor = conn.cursor()
users = []
ar = []
answers = ["-3", "-2", "-1", "0", "1", "2", "3"]

arrq1 = ["Чувствую большую сонливость (3)", "Чувствую умеренную сонливость (2)",
         "Слегка чувствую сонливость (1)", "Затрудняюсь ответить (0)",
         "Практически не чувствую сонливость (-1)",
         "Умеренно бодр (-2)", "Совсем не чувствую сонливость (-3)"]

arrq2 = ["Да, очень много мыслей (3)", "Мыслей немного, но они есть (2)", "Мысли есть, но они незначительны (1)",
         "Затрудняюсь ответить (0)", "Скорее нет, но обычно такое бывает (-1)",
         "Нет, навязчивые мысли практически не беспокоят (-2)", "Сегодня мой разум ясен и чист (-3)"]

arrq3 = ["Однозначно злюсь (3)", "Злости во мне больше, чем грусти (2)", "Наверное, больше злюсь (1)",
         "Ни то ни другое (0)",
         "Наверное, больше расстраиваюсь (-1)", "Грусти во мне больше, чем злости (-2)",
         "Однозначно расстраиваюсь (-3)"]

arrq4 = ["Точно удовлетворен (3)", "В целом да, но были спорные моменты (2)", "Немного лучше, чем могло было быть (1)",
         "Затрудняюсь ответить (0)", "Скорее нет, чем да (-1)", "Всё могло быть куда лучше (-2)",
         "Совсем не удовлетворен (-3)"]

arrq5 = ["Очень сложно (3)", "Были определенные трудности (2)",
         "Остались сомнений по ряду вопросов (1)", "Затрудняюсь ответить (0)",
         "Немного легче, чем я ожидал (-1)", "Довольно несложно (-2)", "Совсем легко (-3)"]

arrq6 = ["Люди сегодня просто раздражают (-3)", "Кто-то подпортил моё настроение (-2)",
         "Слегка раздражают, но не критично (-1)",
         "Затрудняюсь ответить (0)", "Скорее радуют, чем злят (1)", "Неожиданно радуют (2)",
         "Я крайне доволен окружающими людьми (3)"]

arrq7 = ["Был бы самым активным (3)", "Скорее всего занял бы его делами (2)",
         "Пару активностей и хватит (1)", "Затрудняюсь ответить (0)", "Наверное, остался бы дома (-1)",
         "Устал, хочу отлежаться в кровати (-2)", "Точно остался бы дома (-3)"]

arrq8 = ["Совсем не уверен (3)", "Есть небольшой страх (2)", "Совсем немного взволнован (1)",
         "Затрудняюсь ответить (0)", "Скорее уверен, чем нет (-1)", "Весьма уверен (-2)", "Очень уверен (-3)"]

arrq9 = ["Точно да (3)", "Сегодня ощущаю (2)", "За день было парочку счастливых моментов (1)",
         "Затрудняюсь ответить (0)",
         "Хотелось бы быть более счастливым (-1)", "Сегодня не могу назвать себя счастливым (-2)",
         "К сожалению, нет (-3)"]


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
    await message.answer("Привет, друг!\n"
                         "На связи чат-бот проекта FoodMood\n\n"
                         "Мы занимаемся исследованиями в области еды и её влиянии на эмоциональное состояние"
                         "человека.\n\n"
                         "Наш бот поможет подобрать тебе позиции меню, которые содержат необходимые для улучшения"
                         "твоего настроения биологические вещества и витамины.\n\n"
                         "Для начала давай узнаем твоё эмоциональное состояние. Нажми кнопку «Вперёд» и пройди"
                         "быстрый тест, который поможет его определить.",
                         reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Вперёд!")
async def choose(message: types.Message):
    us_id = message.from_user.id
    us_name = message.from_user.first_name
    us_sname = message.from_user.last_name
    username = message.from_user.username
    await db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)
    await message.answer(text="На связи Владислав - психолог команды FoodMood.\n\n"
                              "Обратите внимание на свое эмоциональное состояние и ответьте на следующие вопросы!\n\n"
                              "Тест занимает < 2 мин",
                         reply_markup=test)


@dp.callback_query_handler(text="test")
async def question1(callback: types.CallbackQuery):
    kb = [[types.KeyboardButton(text="Совсем не чувствую сонливость (-3)")],
          [types.KeyboardButton(text="Умеренно бодр (-2)")],
          [types.KeyboardButton(text="Практически не чувствую сонливость (-1)")],
          [types.KeyboardButton(text="Затрудняюсь ответить (0)")],
          [types.KeyboardButton(text="Слегка чувствую сонливость (1)")],
          [types.KeyboardButton(text="Чувствую умеренную сонливость (2)")],
          [types.KeyboardButton(text="Чувствую большую сонливость (3)")]]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True)

    await callback.message.answer("Чувствуете ли Вы сонливость в данный момент?",
                                  reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in arrq1)
async def question2(message: types.Message):
    us_id = message.from_user.id
    ans = message.text.split()
    kb = [[types.KeyboardButton(text="Сегодня мой разум ясен и чист (-3)")],
          [types.KeyboardButton(text="Нет, навязчивые мысли практически не беспокоят (-2)")],
          [types.KeyboardButton(text="Скорее нет, но обычно такое бывает (-1)")],
          [types.KeyboardButton(text="Затрудняюсь ответить (0)")],
          [types.KeyboardButton(text="Мысли есть, но они незначительны (1)")],
          [types.KeyboardButton(text="Мыслей немного, но они есть (2)")],
          [types.KeyboardButton(text="Да, очень много мыслей (3)")]]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True)

    cursor.execute(
        'UPDATE test SET question1 = ? WHERE user_id = ?;',
        (int(ans[-1][1:-1:]), us_id))
    conn.commit()

    await message.answer("Преследуют ли Вас сегодня навязчивые мысли?",
                         reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in arrq2)
async def question3(message: types.Message):
    us_id = message.from_user.id
    ans = message.text.split()
    kb = [[types.KeyboardButton(text="Однозначно расстраиваюсь (-3)")],
          [types.KeyboardButton(text="Грусти во мне больше, чем злости (-2)")],
          [types.KeyboardButton(text="Наверное, больше расстраиваюсь (-1)")],
          [types.KeyboardButton(text="Ни то ни другое (0)")],
          [types.KeyboardButton(text="Наверное, больше злюсь (1)")],
          [types.KeyboardButton(text="Злости во мне больше, чем грусти (2)")],
          [types.KeyboardButton(text="Однозначно злюсь (3)")]]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True)

    cursor.execute(
        'UPDATE test SET question2 = ? WHERE user_id = ?;',
        (int(ans[-1][1:-1:]), us_id))
    conn.commit()

    await message.answer("Последнее время Вы чаще злитесь или расстраиваетесь?",
                         reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in arrq3)
async def question4(message: types.Message):
    us_id = message.from_user.id
    ans = message.text.split()
    kb = [[types.KeyboardButton(text="Совсем не удовлетворен (-3)")],
          [types.KeyboardButton(text="Всё могло быть куда лучше (-2)")],
          [types.KeyboardButton(text="Скорее нет, чем да (-1)")],
          [types.KeyboardButton(text="Затрудняюсь ответить (0)")],
          [types.KeyboardButton(text="Немного лучше, чем могло было быть (1)")],
          [types.KeyboardButton(text="В целом да, но были спорные моменты (2)")],
          [types.KeyboardButton(text="Точно удовлетворен (3)")]]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True)

    cursor.execute(
        'UPDATE test SET question3 = ? WHERE user_id = ?;',
        (int(ans[-1][1:-1:]), us_id))
    conn.commit()

    await message.answer("Удовлетворены ли Вы сегодняшним днём?",
                         reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in arrq4)
async def question5(message: types.Message):
    us_id = message.from_user.id
    ans = message.text.split()
    kb = [[types.KeyboardButton(text="Совсем легко (-3)")],
          [types.KeyboardButton(text="Довольно несложно (-2)")],
          [types.KeyboardButton(text="Немного легче, чем я ожидал (-1)")],
          [types.KeyboardButton(text="Затрудняюсь ответить (0)")],
          [types.KeyboardButton(text="Остались сомнений по ряду вопросов (1)")],
          [types.KeyboardButton(text="Были определенные трудности (2)")],
          [types.KeyboardButton(text="Очень сложно (3)")]]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True)

    cursor.execute(
        'UPDATE test SET question4 = ? WHERE user_id = ?;',
        (int(ans[-1][1:-1:]), us_id))
    conn.commit()

    await message.answer("Легко ли было принимать решения в течение дня?",
                         reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in arrq5)
async def question6(message: types.Message):
    us_id = message.from_user.id
    ans = message.text.split()
    kb = [[types.KeyboardButton(text="Люди сегодня просто раздражают (-3)")],
          [types.KeyboardButton(text="Кто-то подпортил моё настроение (-2)")],
          [types.KeyboardButton(text="Слегка раздражают, но не критично (-1)")],
          [types.KeyboardButton(text="Затрудняюсь ответить (0)")],
          [types.KeyboardButton(text="Скорее радуют, чем злят (1)")],
          [types.KeyboardButton(text="Неожиданно радуют (2)")],
          [types.KeyboardButton(text="Я крайне доволен окружающими людьми (3)")]]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True)

    cursor.execute(
        'UPDATE test SET question5 = ? WHERE user_id = ?;',
        (int(ans[-1][1:-1:]), us_id))
    conn.commit()

    await message.answer("Радуют ли Вас сегодня окружающие люди?",
                         reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in arrq6)
async def question7(message: types.Message):
    us_id = message.from_user.id
    ans = message.text.split()
    kb = [[types.KeyboardButton(text="Точно остался бы дома (-3)")],
          [types.KeyboardButton(text="Устал, хочу отлежаться в кровати (-2)")],
          [types.KeyboardButton(text="Наверное, остался бы дома (-1)")],
          [types.KeyboardButton(text="Затрудняюсь ответить (0)")],
          [types.KeyboardButton(text="Пару активностей и хватит (1)")],
          [types.KeyboardButton(text="Скорее всего занял бы его делами (2)")],
          [types.KeyboardButton(text="Был бы самым активным (3)")]]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True)

    cursor.execute(
        'UPDATE test SET question6 = ? WHERE user_id = ?;',
        (int(ans[-1][1:-1:]), us_id))
    conn.commit()

    await message.answer("Как бы Вы провели сегодняшний день, если бы были абсолютно свободным?",
                         reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in arrq7)
async def question8(message: types.Message):
    us_id = message.from_user.id
    ans = message.text.split()
    kb = [[types.KeyboardButton(text="Очень уверен (-3)")],
          [types.KeyboardButton(text="Весьма уверен (-2)")],
          [types.KeyboardButton(text="Скорее уверен, чем нет (-1)")],
          [types.KeyboardButton(text="Затрудняюсь ответить (0)")],
          [types.KeyboardButton(text="Совсем немного взволнован (1)")],
          [types.KeyboardButton(text="Есть небольшой страх (2)")],
          [types.KeyboardButton(text="Совсем не уверен (3)")]]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True)

    cursor.execute(
        'UPDATE test SET question7 = ? WHERE user_id = ?;',
        (int(ans[-1][1:-1:]), us_id))
    conn.commit()

    await message.answer("Уверены ли Вы в завтрашнем дне?",
                         reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in arrq8)
async def question9(message: types.Message):
    us_id = message.from_user.id
    ans = message.text.split()
    kb = [[types.KeyboardButton(text="К сожалению, нет (-3)")],
          [types.KeyboardButton(text="Сегодня не могу назвать себя счастливым (-2)")],
          [types.KeyboardButton(text="Хотелось бы быть более счастливым (-1)")],
          [types.KeyboardButton(text="Затрудняюсь ответить (0)")],
          [types.KeyboardButton(text="За день было парочку счастливых моментов (1)")],
          [types.KeyboardButton(text="Сегодня ощущаю (2)")],
          [types.KeyboardButton(text="Точно да (3)")]]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True)

    cursor.execute(
        'UPDATE test SET question8 = ? WHERE user_id = ?;',
        (int(ans[-1][1:-1:]), us_id))
    conn.commit()

    await message.answer("Вы ощущаете себя счастливым?",
                         reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in arrq9)
async def result(message: types.Message):
    us_id = message.from_user.id
    ans = message.text.split()

    kb = [[types.KeyboardButton(text="Далее!")]]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    cursor.execute(
        'UPDATE test SET question9 = ? WHERE user_id = ?;',
        (int(ans[-1][1:-1:]), us_id))
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
