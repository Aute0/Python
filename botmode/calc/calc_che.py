from ast import keyword
from datetime import datetime
from imaplib import Commands
import telebot
import logging
from telebot import types

bot_for_games_che = telebot.TeleBot(
    '5600774130:AAFgX-Q5vQ2RCEIsh908iXDy9liuUr1VR84')

value = ''
prev_value = ''
username = ''
user_date = datetime.now

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(   telebot.types.InlineKeyboardButton('',callback_data='no'),
                telebot.types.InlineKeyboardButton('C', callback_data='C'),
                telebot.types.InlineKeyboardButton('<=', callback_data='<='),
                telebot.types.InlineKeyboardButton('/', callback_data='/'))

keyboard.row(   telebot.types.InlineKeyboardButton('7', callback_data='7'),
                telebot.types.InlineKeyboardButton('8', callback_data='8'),
                telebot.types.InlineKeyboardButton('9', callback_data='9'),
                telebot.types.InlineKeyboardButton('*', callback_data='*'))

keyboard.row(   telebot.types.InlineKeyboardButton('4', callback_data='4'),
                telebot.types.InlineKeyboardButton('5', callback_data='5'),
                telebot.types.InlineKeyboardButton('6', callback_data='6'),
                telebot.types.InlineKeyboardButton('-', callback_data='-'))

keyboard.row(   telebot.types.InlineKeyboardButton('1', callback_data='1'),
                telebot.types.InlineKeyboardButton('2', callback_data='2'),
                telebot.types.InlineKeyboardButton('3', callback_data='3'),
                telebot.types.InlineKeyboardButton('+', callback_data='+'))

keyboard.row(   telebot.types.InlineKeyboardButton('', callback_data='no'),
                telebot.types.InlineKeyboardButton('0', callback_data='0'),
                telebot.types.InlineKeyboardButton(',', callback_data='.'),
                telebot.types.InlineKeyboardButton('=', callback_data='='))

@bot_for_games_che.message_handler(commands=['start', 'user', 'calculator'])
def start(m, res=False):
    bot_for_games_che.send_message(
        m.chat.id, 'Привет. Эту программу написала Соня Ч.  Я учусь на факультете разработчик в GeekBrains! Тут можно немного посчитать числа ^_^ ')


@bot_for_games_che.message_handler(content_types=['text'])
def user(message):
    if message.text == '/user':
        bot_for_games_che.send_message(message.from_user.id, "Как тебя зовут?")
        # следующий шаг – функция get_name
        bot_for_games_che.register_next_step_handler(message, get_name)
    else:
        bot_for_games_che.send_message(message.from_user.id, 'Напиши /user')


def get_messages(message):
    global value
    if value == '':
        bot_for_games_che.send_message(message.from_user.id, '0', reply_markup=keyboard)
    else:
        bot_for_games_che.send_message(
            message.from_user.id, value, reply_markup=keyboard)

    bot_for_games_che.send_message(message.from_user.id,
                     "",
                     reply_markup=keyboard)

@bot_for_games_che.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global value, prev_value 
    data = query.data

    if data == 'no':
        pass
    elif data == 'C':
        value = ''
    elif data == '=':
        value = str( eval(value))
    else:
        value += data
    if value != prev_value:
        if value == '':
            bot_for_games_che.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text = '0', reply_markup=keyboard)
        else:
            bot_for_games_che.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text = value, reply_markup=keyboard)
    
    prev_value = value


logging.basicConfig(level=logging.INFO, filename="thecode.log")
bot_for_games_che.infinity_polling()
