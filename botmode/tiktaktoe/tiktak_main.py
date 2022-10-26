from time import sleep as s

import telebot
from telebot import types

bot_for_games_che = telebot.TeleBot(
    '5600774130:AAFgX-Q5vQ2RCEIsh908iXDy9liuUr1VR84')
print('Готов к работе...')

players = []
bot_send = True


def call_data(index1, index2, call):
    global board, players
    if hod % 2 == 0 and call.message.chat.id == user2.id:
        if board[index1][index2] == '◻':
            board[index1][index2] = 'x'
            plus_hod()
            bot_for_games_che.edit_message_reply_markup(
                user2.id, message_id=us2_mes.id, reply_markup=make_board())
            bot_for_games_che.edit_message_reply_markup(
                user1.id, message_id=us1_mes.id, reply_markup=make_board())
            if check_win(board)[0] == True or check_win(board)[0] == None:
                if check_win(board)[0] == None:
                    draw = True
                else:
                    draw = False
                bot_for_games_che.edit_message_reply_markup(user1.id, message_id=us1_mes.id,
                                              reply_markup=make_board(end=True, draw=draw, symbol=check_win(board)))
                bot_for_games_che.edit_message_reply_markup(user2.id, message_id=us2_mes.id,
                                              reply_markup=make_board(end=True, draw=draw, symbol=check_win(board)))
                players.clear()
        else:
            bot_for_games_che.answer_callback_query(
                callback_query_id=call.id, text='Эта клетка уже занята!')
    elif hod % 2 != 0 and call.message.chat.id == user1.id:
        if board[index1][index2] == '◻':
            board[index1][index2] = 'o'
            plus_hod()
            bot_for_games_che.edit_message_reply_markup(
                user2.id, message_id=us2_mes.id, reply_markup=make_board())
            bot_for_games_che.edit_message_reply_markup(
                user1.id, message_id=us1_mes.id, reply_markup=make_board())
            if check_win(board)[0] == True or check_win(board)[0] == None:
                if check_win(board)[0] == None:
                    draw = True
                else:
                    draw = False
                bot_for_games_che.edit_message_reply_markup(user1.id, message_id=us1_mes.id,
                                              reply_markup=make_board(end=True, draw=draw, symbol=check_win(board)))
                bot_for_games_che.edit_message_reply_markup(user2.id, message_id=us2_mes.id,
                                              reply_markup=make_board(end=True, draw=draw, symbol=check_win(board)))
                players.clear()
        else:
            bot_for_games_che.answer_callback_query(
                callback_query_id=call.id, text='Эта клетка уже занята!')
    else:
        bot_for_games_che.answer_callback_query(
            callback_query_id=call.id, text='Не твой ход! Ожидай соперника!')


def make_bot_true():
    global bot_send
    bot_send = True


def make_bot_false():
    global bot_send
    bot_send = False


def check_win(board):
    for i in range(3):
        if board[i][1] == board[i][0] and board[i][1] == board[i][2] and board[i][1] != '◻':
            return True, board[i][0]
    for i in range(3):
        if board[1][i] == board[0][i] and board[1][i] == board[2][i] and board[1][i] != '◻':
            return True, board[1][i]
    for i in range(2):
        if board[0][0] == board[1][1] and board[1][1] != '◻' and board[1][1] == board[2][2]:
            return True, board[0][0]
        elif board[1][1] != '◻' and board[1][1] == board[0][2] and board[0][2] == board[2][0]:
            return True, board[1][1]
    if board[0][0] != '◻' and board[1][0] != '◻' and board[2][0] != '◻' and board[1][0] != '◻' and board[1][
            1] != '◻' and board[1][2] != '◻' and board[2][0] != '◻' and board[2][1] != '◻' and board[2][2] != '◻':
        return None, None
    return False, False


def make_board(end=False, draw=False, symbol='x'):
    if end:
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        if draw:
            txt = 'Конец! Ничья!'
        else:
            txt = f'Конец! Победил игрок , который играл за "{symbol[1]}"'
        b1 = types.InlineKeyboardButton(text=txt, callback_data=102)
        keyboard.add(b1)
        return keyboard
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    b1 = types.InlineKeyboardButton(text=board[0][0], callback_data=1)
    b2 = types.InlineKeyboardButton(text=board[0][1], callback_data=2)
    b3 = types.InlineKeyboardButton(text=board[0][2], callback_data=3)
    b4 = types.InlineKeyboardButton(text=board[1][0], callback_data=4)
    b5 = types.InlineKeyboardButton(text=board[1][1], callback_data=5)
    b6 = types.InlineKeyboardButton(text=board[1][2], callback_data=6)
    b7 = types.InlineKeyboardButton(text=board[2][0], callback_data=7)
    b8 = types.InlineKeyboardButton(text=board[2][1], callback_data=8)
    b9 = types.InlineKeyboardButton(text=board[2][2], callback_data=9)
    keyboard.add(b1, b2, b3, b4, b5, b6, b7, b8, b9)
    return keyboard


def plus_hod():
    global hod
    hod += 1


def del_users():
    global user1, user2
    user1, user2 = None, None
    players.clear()


@bot_for_games_che.message_handler(content_types=['text'])
def main(message):
    global user1, user2, players, stop
    user1, user2 = None, None
    make_bot_true()
    stop = False
    bot_for_games_che.send_message(message.from_user.id,
                     'Это крестики-нолики!')
    loading = bot_for_games_che.send_message(message.from_user.id, 'Ищу пользователей...')
    players.append(message.from_user)
    s(3)
    while True:
        if len(players) <= 1:
            bot_for_games_che.edit_message_text(
                chat_id=message.from_user.id, message_id=loading.id, text='█▒▒▒▒▒▒▒▒▒')
            s(0.5)
            bot_for_games_che.edit_message_text(
                chat_id=message.from_user.id, message_id=loading.id, text='███▒▒▒▒▒▒▒')
            s(0.5)
            bot_for_games_che.edit_message_text(
                chat_id=message.from_user.id, message_id=loading.id, text='█████▒▒▒▒▒')
            s(0.5)
            bot_for_games_che.edit_message_text(
                chat_id=message.from_user.id, message_id=loading.id, text='███████▒▒▒')
            s(0.5)
            bot_for_games_che.edit_message_text(
                chat_id=message.from_user.id, message_id=loading.id, text='██████████')
            s(0.5)
        else:
            bot_for_games_che.send_message(message.from_user.id, 'Пользователь найден!')
            user1 = players[0]
            user2 = players[1]
            chat(message)
            break


def chat(message):
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, hod, user1, user2, board, us1_mes, us2_mes
    board = [['◻'] * 3 for i in range(3)]
    players = [user1, user2]
    hod = 0
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    b1 = types.InlineKeyboardButton(text='◻', callback_data=1)
    b2 = types.InlineKeyboardButton(text='◻', callback_data=2)
    b3 = types.InlineKeyboardButton(text='◻', callback_data=3)
    b4 = types.InlineKeyboardButton(text='◻', callback_data=4)
    b5 = types.InlineKeyboardButton(text='◻', callback_data=5)
    b6 = types.InlineKeyboardButton(text='◻', callback_data=6)
    b7 = types.InlineKeyboardButton(text='◻', callback_data=7)
    b8 = types.InlineKeyboardButton(text='◻', callback_data=8)
    b9 = types.InlineKeyboardButton(text='◻', callback_data=9)
    keyboard.add(b1, b2, b3, b4, b5, b6, b7, b8, b9)
    if bot_send:
        make_bot_false()
        us1_mes = bot_for_games_che.send_message(
            user1.id, f'Играйте! Ты - Нолик! Ты  играешь против {user2.first_name}', reply_markup=keyboard)
        us2_mes = bot_for_games_che.send_message(
            user2.id, f'Играйте! Ты - Крестик! Ты играешь против {user1.first_name}', reply_markup=keyboard)
    bot_for_games_che.register_next_step_handler(message, main)


@bot_for_games_che.callback_query_handler(func=lambda call: True)
def query_handler(call):
    global board, players
    if call.data == '1':
        call_data(0, 0, call=call)
    elif call.data == '2':
        call_data(0, 1, call=call)
    elif call.data == '3':
        call_data(0, 2, call=call)
    elif call.data == '4':
        call_data(1, 0, call=call)
    elif call.data == '5':
        call_data(1, 1, call=call)
    elif call.data == '6':
        call_data(1, 2, call=call)
    elif call.data == '7':
        call_data(2, 0, call=call)
    elif call.data == '8':
        call_data(2, 1, call=call)
    elif call.data == '9':
        call_data(2, 2, call=call)
    else:
        bot_for_games_che.answer_callback_query(call.message.chat.id, 'Игра завершена!')


while True:
  try:
    bot_for_games_che.polling(non_stop=True)
  except Exception as _ex:
    print(_ex)
