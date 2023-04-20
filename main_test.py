import os
import sqlite3
import time
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ParseMode

from arrq import *
from menu import *
from function import *
from pentafoil_chart import *
from keyboards import test
from description_of_products import *

bot = Bot(token='6032169269:AAHY9H4tJXl2qLoKgY1nh7unX5-YKV51d1A')
dp = Dispatcher(bot)
conn = sqlite3.connect('db/test.db', check_same_thread=False)

cursor = conn.cursor()
users = []
ar = []
answers = ["-3", "-2", "-1", "0", "1", "2", "3"]

NEXT_BUTTON_TEXT = "Далее"


def get_menu_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    next_button = InlineKeyboardButton(text=NEXT_BUTTON_TEXT, callback_data="next")
    # analysis_button = InlineKeyboardButton(text=MENU_ANALYSIS_BUTTON_TEXT, callback_data="analysis")
    keyboard.add(next_button)
    # keyboard.add(next_button, analysis_button)
    return keyboard


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
    await message.answer("На связи проект <b>FoodMood!</b>\n\n"
                         "Мы занимаемся исследованиями в области <i>еды и её влияния на эмоциональное состояние человека.</i>\n\n"
                         "Для Вас мы:\n\n"
                         "1. Разберем состав блюд\n\n"
                         "2. Проанализируем биологический и химический состав блюд\n\n"
                         "3. Посоветуем Вам блюда, которые будут содержать нужные для улучшения Вашего настроения витамины и минералы\n\n\n"
                         "Для начала давайте узнаем Ваше эмоциональное состояние.\n\n"
                         "Нажмите кнопку «<b>Вперёд</b>» и пройдите быстрый тест, который поможет его определить",
                         reply_markup=keyboard,  parse_mode=ParseMode.HTML)


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

    kb =[[types.KeyboardButton(text="Да, очень много мыслей (-3)")],
         [types.KeyboardButton(text="Мыслей немного, но они есть (-2)")],
         [types.KeyboardButton(text="Мысли есть, но они незначительны (-1)")],
         [types.KeyboardButton(text="Затрудняюсь ответить (0) ⠀")],
         [types.KeyboardButton(text="Скорее нет, но обычно такое бывает (1)")],
         [types.KeyboardButton(text="Нет, навязчивые мысли практически не беспокоят (2)")],
         [types.KeyboardButton(text="Сегодня мой разум ясен и чист (3)")]]


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

    kb = [[types.KeyboardButton(text="Однозначно злюсь (-3)")],
          [types.KeyboardButton(text="Злости во мне больше, чем грусти (-2)")],
          [types.KeyboardButton(text="Наверное, больше злюсь (-1)")],
          [types.KeyboardButton(text="Ни то ни другое (0)")],
          [types.KeyboardButton(text="Наверное, больше расстраиваюсь (1)")],
          [types.KeyboardButton(text="Грусти во мне больше, чем злости (2)")],
          [types.KeyboardButton(text="Однозначно расстраиваюсь (3)")]]


    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True)

    if len(ans) >= 1 and ans[-2] == '(0)':
        cursor.execute(
            'UPDATE test SET question2 = ? WHERE user_id = ?;',
            (int(ans[-2][1:-1]), us_id))
    else:
        cursor.execute(
            'UPDATE test SET question2 = ? WHERE user_id = ?;',
            (int(ans[-1][1:-1]), us_id))
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
          [types.KeyboardButton(text="Затрудняюсь ответить (0) ⠀ ⠀ ⠀")],
          [types.KeyboardButton(text="Немного лучше, чем могло было быть (1)")],
          [types.KeyboardButton(text="В целом да, но были спорные моменты (2)")],
          [types.KeyboardButton(text="Точно удовлетворен (3)")]]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True)

    if len(ans) >= 2 and ans[-3] == '(0)':
        cursor.execute(
            'UPDATE test SET question3 = ? WHERE user_id = ?;',
            (int(ans[-3][1:-1]), us_id))
    else:
        cursor.execute(
            'UPDATE test SET question3 = ? WHERE user_id = ?;',
            (int(ans[-1][1:-1]), us_id))
    conn.commit()


    await message.answer("Удовлетворены ли Вы сегодняшним днём?",
                         reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in arrq4)
async def question5(message: types.Message):
    us_id = message.from_user.id
    ans = message.text.split()

    kb = [[types.KeyboardButton(text="Очень сложно (-3)")],
          [types.KeyboardButton(text="Были определенные трудности (-2)")],
          [types.KeyboardButton(text="Остались сомнений по ряду вопросов (-1)")],
          [types.KeyboardButton(text="Затрудняюсь ответить (0) ⠀ ⠀ ⠀ ⠀")],
          [types.KeyboardButton(text="Немного легче, чем я ожидал (1)")],
          [types.KeyboardButton(text="Довольно несложно (2)")],
          [types.KeyboardButton(text="Совсем легко (3)")]]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True)

    if len(ans) >= 6 and ans[-4] == '(0)':
        cursor.execute(
            'UPDATE test SET question4 = ? WHERE user_id = ?;',
            (int(ans[-4][1:-1]), us_id))
    else:
        cursor.execute(
            'UPDATE test SET question4 = ? WHERE user_id = ?;',
            (int(ans[-1][1:-1]), us_id))
    conn.commit()



    await message.answer("Легко ли было принимать решения в течение дня?",
                         reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in arrq5)
async def question6(message: types.Message):
    us_id = message.from_user.id
    ans = message.text.split()


    kb = [[types.KeyboardButton(text="Я крайне доволен окружающими людьми (-3)")],
          [types.KeyboardButton(text="Неожиданно радуют (-2)")],
          [types.KeyboardButton(text="Скорее радуют, чем злят (-1)")],
          [types.KeyboardButton(text="Затрудняюсь ответить (0) ⠀ ⠀ ⠀ ⠀ ⠀")],
          [types.KeyboardButton(text="Слегка раздражают, но не критично (1)")],
          [types.KeyboardButton(text="Кто-то подпортил моё настроение (2)")],
          [types.KeyboardButton(text="Люди сегодня просто раздражают (3)")]]


    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True)

    if len(ans) >= 6 and ans[-5] == '(0)':
        cursor.execute(
            'UPDATE test SET question5 = ? WHERE user_id = ?;',
            (int(ans[-5][1:-1]), us_id))
    else:
        cursor.execute(
            'UPDATE test SET question5 = ? WHERE user_id = ?;',
            (int(ans[-1][1:-1]), us_id))
    conn.commit()



    await message.answer("Радуют ли Вас сегодня окружающие люди?",
                         reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in arrq6)
async def question7(message: types.Message):
    us_id = message.from_user.id
    ans = message.text.split()


    kb =[[types.KeyboardButton(text="Был бы самым активным (-3)")],
         [types.KeyboardButton(text="Скорее всего занял бы его делами (-2)")],
         [types.KeyboardButton(text="Пару активностей и хватит (-1)")],
         [types.KeyboardButton(text="Затрудняюсь ответить (0) ⠀ ⠀ ⠀ ⠀ ⠀ ⠀")],
         [types.KeyboardButton(text="Наверное, остался бы дома (1)")],
         [types.KeyboardButton(text="Устал, хочу отлежаться в кровати (2)")],
         [types.KeyboardButton(text="Точно остался бы дома (3)")]]




    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True)


    if len(ans) >= 6 and ans[-6] == '(0)':
        cursor.execute(
            'UPDATE test SET question6 = ? WHERE user_id = ?;',
            (int(ans[-6][1:-1]), us_id))
    else:
        cursor.execute(
            'UPDATE test SET question6 = ? WHERE user_id = ?;',
            (int(ans[-1][1:-1]), us_id))
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
          [types.KeyboardButton(text="Затрудняюсь ответить (0) ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀")],
          [types.KeyboardButton(text="Совсем немного взволнован (1)")],
          [types.KeyboardButton(text="Есть небольшой страх (2)")],
          [types.KeyboardButton(text="Совсем не уверен (3)")]]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True)

    if len(ans) >= 7 and ans[-7] == '(0)':
        cursor.execute(
            'UPDATE test SET question7 = ? WHERE user_id = ?;',
            (int(ans[-7][1:-1]), us_id))
    else:
        cursor.execute(
            'UPDATE test SET question7 = ? WHERE user_id = ?;',
            (int(ans[-1][1:-1]), us_id))
    conn.commit()



    await message.answer("Уверены ли Вы в завтрашнем дне?",
                         reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in arrq8)
async def question9(message: types.Message):
    us_id = message.from_user.id
    ans = message.text.split()


    kb = [[types.KeyboardButton(text="Точно да (-3)")],
          [types.KeyboardButton(text="Сегодня ощущаю (-2)")],
          [types.KeyboardButton(text="За день было парочку счастливых моментов (-1)")],
          [types.KeyboardButton(text="Затрудняюсь ответить (0) ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀ ⠀")],
          [types.KeyboardButton(text="Хотелось бы быть более счастливым (1)")],
          [types.KeyboardButton(text="Сегодня не могу назвать себя счастливым (2)")],
          [types.KeyboardButton(text="К сожалению, нет (3)")]]



    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True)

    if len(ans) >= 7 and ans[-8] == '(0)':
        cursor.execute(
            'UPDATE test SET question8 = ? WHERE user_id = ?;',
            (int(ans[-8][1:-1]), us_id))
    else:
        cursor.execute(
            'UPDATE test SET question8 = ? WHERE user_id = ?;',
            (int(ans[-1][1:-1]), us_id))
    conn.commit()


    await message.answer("Вы ощущаете себя счастливым?",
                         reply_markup=keyboard)


@dp.message_handler(lambda message: message.text in arrq9)
async def result(message: types.Message):
    us_id = message.from_user.id
    ans = message.text.split()

    kb = [[types.KeyboardButton(text="Далее!")]]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    if len(ans) >= 8 and ans[-9] == '(0)':
        cursor.execute(
            'UPDATE test SET question9 = ? WHERE user_id = ?;',
            (int(ans[-9][1:-1]), us_id))
    else:
        cursor.execute(
            'UPDATE test SET question9 = ? WHERE user_id = ?;',
            (int(ans[-1][1:-1]), us_id))
    conn.commit()

    await message.answer("Получить график!",
                         reply_markup=keyboard)



@dp.message_handler(lambda message: "Далее!" in message.text)
async def send_graph(message: types.Message):
    us_id = message.from_user.id

    cursor.execute("SELECT question1, question2, question3, question4, question5, question6, question7, "
                   "question8, question9 FROM test WHERE user_id = ?;", (us_id,))
    row = cursor.fetchone()
    if row:
        a = list(row)
        print(type(a), a)
    else:
        a = []

    result_pechal, result_strax, result_gnev, result_schaste, result_chill = the_sum_of_net_indicators(a)
    max_val = max(result_pechal, result_strax, result_gnev, result_schaste, result_chill)
    if max_val == result_pechal:
        dom_emotion = "Печаль"
    elif max_val == result_strax:
        dom_emotion = "Страх"
    elif max_val == result_gnev:
        dom_emotion = "Гнев"
    elif max_val == result_schaste:
        dom_emotion = "Счастье"
    else:
        dom_emotion = "Спокойствие"
    if [result_pechal, result_schaste].count(max_val) > 1:
        dom_emotion = "Печаль и Спокойствие"

    draw_graph([result_pechal, result_strax, result_gnev, result_schaste, result_chill])
    photo = open('foo.png', 'rb')
    await bot.send_photo(message.from_user.id, photo)
    os.remove('foo.png')


    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='Да', callback_data='Yes'),
                 types.InlineKeyboardButton(text='Нет', callback_data='No'))
    await bot.send_message(message.from_user.id, f"Вы согласны, что Ваша доминирующая эмоция – {dom_emotion}?",
                           reply_markup=keyboard)

    @dp.callback_query_handler(lambda c: c.data in ['Yes', 'No'])
    async def process_callback_data(callback_query: types.CallbackQuery):
        if callback_query.data == 'Yes':
            cursor.execute(
                f"UPDATE test SET dominant_emotion = '{dom_emotion}' WHERE user_id = {callback_query.from_user.id}")
            await bot.send_message(callback_query.from_user.id, "Основываясь на Вашем настроении, нутрициолог Артем рекомендует выбрать следующие позиции из меню:")

            if dom_emotion == 'Печаль':
                await bot.send_message(callback_query.from_user.id, pechal_menu, parse_mode=ParseMode.HTML,
                                       reply_markup=get_menu_keyboard())
            elif dom_emotion == 'Страх':
                await bot.send_message(callback_query.from_user.id, strax_menu, parse_mode=ParseMode.HTML,
                                       reply_markup=get_menu_keyboard())
            elif dom_emotion == 'Гнев':
                await bot.send_message(callback_query.from_user.id, gnev_menu, parse_mode=ParseMode.HTML,
                                       reply_markup=get_menu_keyboard())
            elif dom_emotion == 'Счастье':
                await bot.send_message(callback_query.from_user.id, schaste_menu, parse_mode=ParseMode.HTML,
                                       reply_markup=get_menu_keyboard())
            elif dom_emotion == 'Спокойствие':
                await bot.send_message(callback_query.from_user.id, chill_menu, parse_mode=ParseMode.HTML,
                                       reply_markup=get_menu_keyboard())


        else:
            custom_keyboard = types.InlineKeyboardMarkup()
            custom_keyboard.add(types.InlineKeyboardButton(text='Печаль', callback_data='Печаль'),
                                types.InlineKeyboardButton(text='Страх', callback_data='Страх'),
                                types.InlineKeyboardButton(text='Гнев', callback_data='Гнев'),
                                types.InlineKeyboardButton(text='Счастье', callback_data='Счастье'),
                                types.InlineKeyboardButton(text='Спокойствие', callback_data='Спокойствие'))
            await bot.send_message(callback_query.from_user.id, "Выберите свою доминирующую эмоцию самостоятельно:",
                                   reply_markup=custom_keyboard)
            conn.commit()


        @dp.callback_query_handler(lambda c: c.data in ['Печаль', 'Страх', 'Гнев', 'Счастье', 'Спокойствие'])
        async def process_callback_data(callback_query: types.CallbackQuery):
            cursor.execute(
                f"UPDATE test SET dominant_emotion = '{callback_query.data.capitalize()}' WHERE user_id = {callback_query.from_user.id}")
            await bot.send_message(callback_query.from_user.id,
                                   "Основываясь на Вашем настроении, нутрициолог Артем рекомендует выбрать следующие позиции из меню:")
            conn.commit()
            if callback_query.data == 'Печаль':
                await bot.send_message(callback_query.from_user.id, pechal_menu, parse_mode=ParseMode.HTML,
                                       reply_markup=get_menu_keyboard())
            elif callback_query.data == 'Страх':
                await bot.send_message(callback_query.from_user.id, strax_menu, parse_mode=ParseMode.HTML,
                                       reply_markup=get_menu_keyboard())
            elif callback_query.data == 'Гнев':
                await bot.send_message(callback_query.from_user.id, gnev_menu, parse_mode=ParseMode.HTML,
                                       reply_markup=get_menu_keyboard())
            elif callback_query.data == 'Счастье':
                await bot.send_message(callback_query.from_user.id, schaste_menu, parse_mode=ParseMode.HTML,
                                       reply_markup=get_menu_keyboard())
            elif callback_query.data == 'Спокойствие':
                await bot.send_message(callback_query.from_user.id, chill_menu, parse_mode=ParseMode.HTML,
                                       reply_markup=get_menu_keyboard())


        @dp.callback_query_handler(lambda c: c.data in ['next', 'analysis'])
        async def process_menu_callback(callback_query: types.CallbackQuery):
            if callback_query.data == 'next':
                # Если была нажата кнопка "Далее", просим пользователя оставить отзыв
                await bot.send_message(callback_query.from_user.id, "Воспользовались ли Вы рекомендациями нашего бота?\n"
                                                                    "Улучшилось ли ваше настроение после приёма пищи?\n\n"
                                                                    "Ваш отзыв очень важен для развития проекта 🥺")

                # Обработчик сообщения с отзывом
                @dp.message_handler()
                async def process_feedback(message: types.Message):
                    cursor.execute(
                        f"UPDATE test SET feedback = '{message.text}' WHERE user_id = {message.from_user.id}")
                    await bot.send_message(message.from_user.id, "Спасибо за отзыв! 👐\n"
                                                                 "Для того, чтобы пройти заново тест, напишите /start")
                    conn.commit()
    #
    # if callback_query.data == 'analysis':
    #     # Если была нажата кнопка "Разбор меню", отправляем описание меню
    #     message_text = callback_query.message.text
    #     if message_text == pechal_menu:
    #         await bot.send_message(callback_query.from_user.id, pechal_menu_description)
    #     elif message_text == strax_menu:
    #         await bot.send_message(callback_query.from_user.id, strax_menu_description)
    #     elif message_text == gnev_menu:
    #         await bot.send_message(callback_query.from_user.id, gnev_menu_description)
    #     elif message_text == schaste_menu:
    #         await bot.send_message(callback_query.from_user.id, schaste_menu_description)
    #     elif message_text == chill_menu:
    #         await bot.send_message(callback_query.from_user.id, chill_menu_description)
    #     await bot.send_message(callback_query.from_user.id, "Оставьте, пожалуйста, свой отзыв:")
    #
    #     # Обработчик сообщения с отзывом
    #     @dp.message_handler()
    #     async def process_feedback(message: types.Message):
    #         cursor.execute(
    #             f"UPDATE test SET feedback = '{message.text}' WHERE user_id = {message.from_user.id}")
    #         await bot.send_message(message.from_user.id, "Спасибо за отзыв!\n"
    #                                                      "Для того, чтобы пройти заново тест, напишите /start")
    #         conn.commit()



if __name__ == '__main__':
    while True:
        try:
            executor.start_polling(dp, skip_updates=True)
        except Exception as e:
            print(f'Error: {e}')
            time.sleep(5)


