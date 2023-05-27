import os
import sqlite3

from PIL import Image
import io
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ParseMode
from aiogram import types
from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton
from menu import *
from function import *
from pentafoil_chart import *
from answer_values_for_test import *


bot = Bot(token='YOUR TOKEN')
dp = Dispatcher(bot)
conn = sqlite3.connect('db/test.db', check_same_thread=False)
start_photo = 'start_photo.png'

cursor = conn.cursor()
users = []
ar = []
answers = ["-3", "-2", "-1", "0", "1", "2", "3"]

NEXT_BUTTON_TEXT = "Оставить отзыв"

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
            ' question6 = ? , question7 = ?, question8 = ?, question9 = ?, dominant_emotion = ?, feedback = ? WHERE user_id = ?;',
            (100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, user_id))
        conn.commit()


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    # загрузка изображения
    with open("start_photo.png", "rb") as file:
        photo = io.BytesIO(file.read())

    # создание клавиатуры
    kb = [[types.KeyboardButton(text="Вперёд!")]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True)

    # отправка сообщения с изображением и клавиатурой
    await message.answer_photo(photo, caption="На связи проект <b>Food Mood!</b>\n\n"
                                                "Мы занимаемся исследованиями в области <i>еды и её влияния на эмоциональное состояние человека.</i>\n\n"
                                                "Для Вас мы:\n"
                                                "🔹 Разберем состав блюд;\n"
                                                "🔹 Проанализируем биологический и химический состав блюд;\n"
                                                "🔹 Посоветуем Вам блюда, которые будут содержать нужные для улучшения Вашего настроения витамины и минералы;\n\n"
                                                "Для начала давайте узнаем Ваше эмоциональное состояние.\n\n"
                                                "Нажмите кнопку «<b>Вперёд</b>» и пройдите быстрый тест, который поможет его определить\n\n"
                                                "<i>Тест занимает меньше 2-ух минут</i>",
                                reply_markup=keyboard, parse_mode=ParseMode.HTML)



# Create a reply keyboard with buttons for each answer choice
test_buttons1 = ReplyKeyboardMarkup(resize_keyboard=True)
for answer in answer_values_q1.keys():
    button = KeyboardButton(answer)
    test_buttons1.add(button)

test_buttons2 = ReplyKeyboardMarkup(resize_keyboard=True)
for answer in answer_values_q2.keys():
    button = KeyboardButton(answer)
    test_buttons2.add(button)

test_buttons3 = ReplyKeyboardMarkup(resize_keyboard=True)
for answer in answer_values_q3.keys():
    button = KeyboardButton(answer)
    test_buttons3.add(button)

test_buttons4 = ReplyKeyboardMarkup(resize_keyboard=True)
for answer in answer_values_q4.keys():
    button = KeyboardButton(answer)
    test_buttons4.add(button)

test_buttons5 = ReplyKeyboardMarkup(resize_keyboard=True)
for answer in answer_values_q5.keys():
    button = KeyboardButton(answer)
    test_buttons5.add(button)

test_buttons6 = ReplyKeyboardMarkup(resize_keyboard=True)
for answer in answer_values_q6.keys():
    button = KeyboardButton(answer)
    test_buttons6.add(button)

test_buttons7 = ReplyKeyboardMarkup(resize_keyboard=True)
for answer in answer_values_q7.keys():
    button = KeyboardButton(answer)
    test_buttons7.add(button)

test_buttons8 = ReplyKeyboardMarkup(resize_keyboard=True)
for answer in answer_values_q8.keys():
    button = KeyboardButton(answer)
    test_buttons8.add(button)

test_buttons9 = ReplyKeyboardMarkup(resize_keyboard=True)
for answer in answer_values_q9.keys():
    button = KeyboardButton(answer)
    test_buttons9.add(button)



@dp.message_handler(lambda message: message.text == "Вперёд!")
async def choose(message: types.Message):
    # Get user info and insert into database
    us_id = message.from_user.id
    us_name = message.from_user.first_name
    us_sname = message.from_user.last_name
    username = message.from_user.username
    await db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

    # Ask the first question with the reply keyboard
    await message.answer(text="Чувствуете ли Вы сонливость в данный момент?", reply_markup=test_buttons1)


# Handler for when the user selects an answer to question 1
@dp.message_handler(lambda message: message.text in answer_values_q1.keys())
async def process_q1_answer(message: types.Message):

    # Extract the answer value from the answer text
    answer_value = answer_values_q1[message.text]

    # Update the database with the user's answer
    user_id = message.from_user.id
    conn.execute("UPDATE test SET question1=? WHERE user_id=?", (answer_value, user_id))
    conn.commit()

    # Show the next question
    await message.answer(text="Преследуют ли Вас сегодня навязчивые мысли?", reply_markup=test_buttons2)

# Handler for when the user selects an answer to question 1
@dp.message_handler(lambda message: message.text in answer_values_q2.keys())
async def process_q2_answer(message: types.Message):
    # Extract the answer value from the answer text
    answer_value = answer_values_q2[message.text]

    # Update the database with the user's answer
    user_id = message.from_user.id
    conn.execute("UPDATE test SET question2=? WHERE user_id=?", (answer_value, user_id))
    conn.commit()

    # Show the next question
    await message.answer(text="Последнее время Вы чаще злитесь или расстраиваетесь?", reply_markup=test_buttons3)

# Handler for when the user selects an answer to question 1
@dp.message_handler(lambda message: message.text in answer_values_q3.keys())
async def process_q3_answer(message: types.Message):
    # Extract the answer value from the answer text
    answer_value = answer_values_q3[message.text]

    # Update the database with the user's answer
    user_id = message.from_user.id
    conn.execute("UPDATE test SET question3=? WHERE user_id=?", (answer_value, user_id))
    conn.commit()

    # Show the next question
    await message.answer(text="Удовлетворены ли Вы сегодняшним днём?", reply_markup=test_buttons4)

# Handler for when the user selects an answer to question 1
@dp.message_handler(lambda message: message.text in answer_values_q4.keys())
async def process_q4_answer(message: types.Message):
    # Extract the answer value from the answer text
    answer_value = answer_values_q4[message.text]

    # Update the database with the user's answer
    user_id = message.from_user.id
    conn.execute("UPDATE test SET question4=? WHERE user_id=?", (answer_value, user_id))
    conn.commit()

    # Show the next question
    await message.answer(text="Легко ли было принимать решения в течение дня?", reply_markup=test_buttons5)

# Handler for when the user selects an answer to question 1
@dp.message_handler(lambda message: message.text in answer_values_q5.keys())
async def process_q5_answer(message: types.Message):
    # Extract the answer value from the answer text
    answer_value = answer_values_q5[message.text]

    # Update the database with the user's answer
    user_id = message.from_user.id
    conn.execute("UPDATE test SET question5=? WHERE user_id=?", (answer_value, user_id))
    conn.commit()

    # Show the next question
    await message.answer(text="Радуют ли Вас сегодня окружающие люди?", reply_markup=test_buttons6)

# Handler for when the user selects an answer to question 1
@dp.message_handler(lambda message: message.text in answer_values_q6.keys())
async def process_q6_answer(message: types.Message):
    # Extract the answer value from the answer text
    answer_value = answer_values_q6[message.text]

    # Update the database with the user's answer
    user_id = message.from_user.id
    conn.execute("UPDATE test SET question6=? WHERE user_id=?", (answer_value, user_id))
    conn.commit()

    # Show the next question
    await message.answer(text="Как бы Вы провели сегодняшний день, если бы были абсолютно свободным?", reply_markup=test_buttons7)

# Handler for when the user selects an answer to question 1
@dp.message_handler(lambda message: message.text in answer_values_q7.keys())
async def process_q7_answer(message: types.Message):
    # Extract the answer value from the answer text
    answer_value = answer_values_q7[message.text]

    # Update the database with the user's answer
    user_id = message.from_user.id
    conn.execute("UPDATE test SET question7=? WHERE user_id=?", (answer_value, user_id))
    conn.commit()

    # Show the next question
    await message.answer(text="Уверены ли Вы в завтрашнем дне?", reply_markup=test_buttons8)

# Handler for when the user selects an answer to question 1
@dp.message_handler(lambda message: message.text in answer_values_q8.keys())
async def process_q8_answer(message: types.Message):
    # Extract the answer value from the answer text
    answer_value = answer_values_q8[message.text]

    # Update the database with the user's answer
    user_id = message.from_user.id
    conn.execute("UPDATE test SET question8=? WHERE user_id=?", (answer_value, user_id))
    conn.commit()

    # Show the next question
    await message.answer(text="Вы ощущаете себя счастливым?", reply_markup=test_buttons9)

@dp.message_handler(lambda message: message.text in answer_values_q9.keys())
async def process_q9_answer(message: types.Message):
    # Extract the answer value from the answer text
    answer_value = answer_values_q9[message.text]

    # Update the database with the user's answer
    user_id = message.from_user.id
    conn.execute("UPDATE test SET question9=? WHERE user_id=?", (answer_value, user_id))
    conn.commit()

    # Ask the user if they want to get the graph
    kb = [[types.KeyboardButton(text="Далее!")]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Для получения графика, нажмите <b>Далее!</b>", parse_mode=ParseMode.HTML,
                         reply_markup=keyboard, )

# Handler for when the user wants to see the graph
@dp.message_handler(lambda message: "Далее!" in message.text)
async def send_graph(message: types.Message):
    us_id = message.from_user.id

    # Retrieve the user's answers from the database
    cursor.execute("SELECT question1, question2, question3, question4, question5, question6, question7, "
                   "question8, question9 FROM test WHERE user_id = ?;", (us_id,))
    row = cursor.fetchone()
    if row:
        a = list(row)
    else:
        a = []

    # Calculate the dominant emotion and draw the graph
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
    keyboard.add(types.InlineKeyboardButton(text='Далее', callback_data='No'))
    await bot.send_message(message.from_user.id, f"График показывает, что Ваша доминирующая эмоция – <b>{dom_emotion}</b>",
                           reply_markup=keyboard, parse_mode=ParseMode.HTML)

    @dp.callback_query_handler(lambda c: c.data in ['Yes', 'No'])
    async def process_callback_data(callback_query: types.CallbackQuery):
        user_id = callback_query.from_user.id
        if callback_query.data == 'No':
            custom_keyboard = types.InlineKeyboardMarkup()
            custom_keyboard.add(types.InlineKeyboardButton(text='Печаль', callback_data='Печаль'),
                                types.InlineKeyboardButton(text='Страх', callback_data='Страх'),
                                types.InlineKeyboardButton(text='Гнев', callback_data='Гнев'),
                                types.InlineKeyboardButton(text='Счастье', callback_data='Счастье'),
                                types.InlineKeyboardButton(text='Спокойствие', callback_data='Спокойствие'))
            await bot.send_message(callback_query.from_user.id, "Выберите свою доминирующую эмоцию:",
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
            await bot.send_message(callback_query.from_user.id, "✍️ Воспользовались ли Вы рекомендациями нашего бота?\n"
                                                                "✍️ Улучшилось ли ваше настроение после приёма пищи?\n\n"
                                                                "Ваш отзыв очень важен для развития проекта 🥺")

    # Обработчик сообщения с отзывом
    @dp.message_handler()
    async def process_feedback(message: types.Message):
        cursor.execute(
            f"UPDATE test SET feedback = '{message.text}' WHERE user_id = {message.from_user.id}")
        await bot.send_message(message.from_user.id, "Спасибо за отзыв! 👐\n"
                                                     "Для того, чтобы пройти заново тест, напишите /start")
        conn.commit()




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)





# @dp.message_handler(lambda message: "Далее!" in message.text)
# async def send_graph(message: types.Message):
#     us_id = message.from_user.id
#
#     cursor.execute("SELECT question1, question2, question3, question4, question5, question6, question7, "
#                    "question8, question9 FROM test WHERE user_id = ?;", (us_id,))
#     row = cursor.fetchone()
#     if row:
#         a = list(row)
#         print(type(a), a)
#     else:
#         a = []
#
#     result_pechal, result_strax, result_gnev, result_schaste, result_chill = the_sum_of_net_indicators(a)
#     max_val = max(result_pechal, result_strax, result_gnev, result_schaste, result_chill)
#     if max_val == result_pechal:
#         dom_emotion = "Печаль"
#     elif max_val == result_strax:
#         dom_emotion = "Страх"
#     elif max_val == result_gnev:
#         dom_emotion = "Гнев"
#     elif max_val == result_schaste:
#         dom_emotion = "Счастье"
#     else:
#         dom_emotion = "Спокойствие"
#     if [result_pechal, result_schaste].count(max_val) > 1:
#         dom_emotion = "Печаль и Спокойствие"
#
#     draw_graph([result_pechal, result_strax, result_gnev, result_schaste, result_chill])
#     photo = open('foo.png', 'rb')
#     await bot.send_photo(message.from_user.id, photo)
#     os.remove('foo.png')
#
#
#     keyboard = types.InlineKeyboardMarkup()
#     keyboard.add(types.InlineKeyboardButton(text='Да', callback_data='Yes'),
#                  types.InlineKeyboardButton(text='Нет', callback_data='No'))
#     await bot.send_message(message.from_user.id, f"Вы согласны, что Ваша доминирующая эмоция – {dom_emotion}?",
#                            reply_markup=keyboard)
#
#     @dp.callback_query_handler(lambda c: c.data in ['Yes', 'No'])
#     async def process_callback_data(callback_query: types.CallbackQuery):
#         if callback_query.data == 'Yes':
#             cursor.execute(
#                 f"UPDATE test SET dominant_emotion = '{dom_emotion}' WHERE user_id = {callback_query.from_user.id}")
#             await bot.send_message(callback_query.from_user.id, "Основываясь на Вашем настроении, нутрициолог Артем рекомендует выбрать следующие позиции из меню:")
#
#             if dom_emotion == 'Печаль':
#                 await bot.send_message(callback_query.from_user.id, pechal_menu, parse_mode=ParseMode.HTML,
#                                        reply_markup=get_menu_keyboard())
#             elif dom_emotion == 'Страх':
#                 await bot.send_message(callback_query.from_user.id, strax_menu, parse_mode=ParseMode.HTML,
#                                        reply_markup=get_menu_keyboard())
#             elif dom_emotion == 'Гнев':
#                 await bot.send_message(callback_query.from_user.id, gnev_menu, parse_mode=ParseMode.HTML,
#                                        reply_markup=get_menu_keyboard())
#             elif dom_emotion == 'Счастье':
#                 await bot.send_message(callback_query.from_user.id, schaste_menu, parse_mode=ParseMode.HTML,
#                                        reply_markup=get_menu_keyboard())
#             elif dom_emotion == 'Спокойствие':
#                 await bot.send_message(callback_query.from_user.id, chill_menu, parse_mode=ParseMode.HTML,
#                                        reply_markup=get_menu_keyboard())
#
#
#         else:
#             custom_keyboard = types.InlineKeyboardMarkup()
#             custom_keyboard.add(types.InlineKeyboardButton(text='Печаль', callback_data='Печаль'),
#                                 types.InlineKeyboardButton(text='Страх', callback_data='Страх'),
#                                 types.InlineKeyboardButton(text='Гнев', callback_data='Гнев'),
#                                 types.InlineKeyboardButton(text='Счастье', callback_data='Счастье'),
#                                 types.InlineKeyboardButton(text='Спокойствие', callback_data='Спокойствие'))
#             await bot.send_message(callback_query.from_user.id, "Выберите свою доминирующую эмоцию самостоятельно:",
#                                    reply_markup=custom_keyboard)
#             conn.commit()
#
#
#         @dp.callback_query_handler(lambda c: c.data in ['Печаль', 'Страх', 'Гнев', 'Счастье', 'Спокойствие'])
#         async def process_callback_data(callback_query: types.CallbackQuery):
#             cursor.execute(
#                 f"UPDATE test SET dominant_emotion = '{callback_query.data.capitalize()}' WHERE user_id = {callback_query.from_user.id}")
#             await bot.send_message(callback_query.from_user.id,
#                                    "Основываясь на Вашем настроении, нутрициолог Артем рекомендует выбрать следующие позиции из меню:")
#             conn.commit()
#             if callback_query.data == 'Печаль':
#                 await bot.send_message(callback_query.from_user.id, pechal_menu, parse_mode=ParseMode.HTML,
#                                        reply_markup=get_menu_keyboard())
#             elif callback_query.data == 'Страх':
#                 await bot.send_message(callback_query.from_user.id, strax_menu, parse_mode=ParseMode.HTML,
#                                        reply_markup=get_menu_keyboard())
#             elif callback_query.data == 'Гнев':
#                 await bot.send_message(callback_query.from_user.id, gnev_menu, parse_mode=ParseMode.HTML,
#                                        reply_markup=get_menu_keyboard())
#             elif callback_query.data == 'Счастье':
#                 await bot.send_message(callback_query.from_user.id, schaste_menu, parse_mode=ParseMode.HTML,
#                                        reply_markup=get_menu_keyboard())
#             elif callback_query.data == 'Спокойствие':
#                 await bot.send_message(callback_query.from_user.id, chill_menu, parse_mode=ParseMode.HTML,
#                                        reply_markup=get_menu_keyboard())
#
#
#         @dp.callback_query_handler(lambda c: c.data in ['next', 'analysis'])
#         async def process_menu_callback(callback_query: types.CallbackQuery):
#             if callback_query.data == 'next':
#                 # Если была нажата кнопка "Далее", просим пользователя оставить отзыв
#                 await bot.send_message(callback_query.from_user.id, "Воспользовались ли Вы рекомендациями нашего бота?\n"
#                                                                     "Улучшилось ли ваше настроение после приёма пищи?\n\n"
#                                                                     "Ваш отзыв очень важен для развития проекта 🥺")
#
#                 # Обработчик сообщения с отзывом
#                 @dp.message_handler()
#                 async def process_feedback(message: types.Message):
#                     cursor.execute(
#                         f"UPDATE test SET feedback = '{message.text}' WHERE user_id = {message.from_user.id}")
#                     await bot.send_message(message.from_user.id, "Спасибо за отзыв! 👐\n"
#                                                                  "Для того, чтобы пройти заново тест, напишите /start")
#                     conn.commit()
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



# if __name__ == '__main__':
#     while True:
#         try:
#             executor.start_polling(dp, skip_updates=True)
#         except Exception as e:
#             print(f'Error: {e}')
#             time.sleep(5)


