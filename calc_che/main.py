import controller as c
import telebot
bot = telebot.TeleBot('5600774130: AAFgX-Q5vQ2RCEIsh908iXDy9liuUr1VR84')

@bot.message_handler(commands = ['start','calculator'])

def get_messages(message):
    bot.send_message(message.from_user.id, "Привет. Эту программу написала Соня Ч. Тут можно немного посчитать числа ^_^")

bot.polling(none_stop=False, interval=0)

#c.button_click()