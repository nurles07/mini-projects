import telebot
from decouple import config


token = config('TOKEN')

# стикеры
yes_sticker = 'CAACAgIAAxkBAAEIBWNkBYbFfYJWz-Ipe4MZ2tCsnHAbhwACvRMAAgvWyUuDLxP60AH0yS4E'
no_stecker = 'CAACAgIAAxkBAAEIBV1kBYbBacXcA3GfjsEU7f2U932gxQACLxQAArKOyUuB5P9zXg4heS4E'

# клавиатура под сообщением
keyboard = telebot.types.InlineKeyboardMarkup()
b1 = telebot.types.InlineKeyboardButton('да', callback_data='yes')
b2 = telebot.types.InlineKeyboardButton('нет', callback_data='no')
keyboard.add(b1, b2)


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'привет выбери кнопку', reply_markup=keyboard)

# func - функция фильтр , в данном случаи разрешаются все сообщение
@bot.callback_query_handler(func=lambda x: True) 
def reply_to_button(call):
    if call.data == 'yes':
        bot.send_sticker(call.from_user.id, yes_sticker)
    elif call.data == 'no':
        bot.send_sticker(call.from_user.id, no_stecker)    



bot.polling()    