import telebot
from decouple import config


token = config('TOKEN')

# стикеры
yes_sticker = 'CAACAgIAAxkBAAEIBWNkBYbFfYJWz-Ipe4MZ2tCsnHAbhwACvRMAAgvWyUuDLxP60AH0yS4E'
no_stecker = 'CAACAgIAAxkBAAEIBV1kBYbBacXcA3GfjsEU7f2U932gxQACLxQAArKOyUuB5P9zXg4heS4E'

bot = telebot.TeleBot(token)

# клавиатура
keyboard = telebot.types.ReplyKeyboardMarkup()
b1 = telebot.types.KeyboardButton('да')
b2 = telebot.types.KeyboardButton('нет')
keyboard.add(b1, b2)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'привет выбери кнопку', reply_markup=keyboard)
    bot.register_next_step_handler(message, reply_to_button)

def reply_to_button(message):
    if message.text == 'да':
        bot.send_sticker(message.chat.id, yes_sticker)
    elif message.text == 'нет':
        bot.send_sticker(message.chat.id, no_stecker)
    else:
        bot.send_message(message.chat.id, 'нажмите на кнопку')
        
    bot.register_next_step_handler(message, reply_to_button)    



bot.polling()    