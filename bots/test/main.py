import telebot
from decouple import config

token = config('TOKEN')

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello')
    bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAEIBSBkBXYS0Uuc_JkZHX5Mce7QDmcITAAC5QIAAp9UvwdljZGwJB7CgC4E')
    bot.send_photo(message.chat.id,'https://as01.epimg.net/meristation_en/imagenes/2022/02/18/news/1645143158_918055_1645145092_noticia_normal.jpg')

@bot.message_handler(content_types=['text'])
def aaaa(message):
    if message.text == 'привет':
        bot.send_message(message.chat.id, 'привет')
    else:
        bot.send_message(message.chat.id, 'сообщение не распознанно')    

@bot.message_handler(content_types=['sticker'])
def bbbb(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)  
    bot.send_message(message.chat.id, message.sticker.file_id)      



bot.polling()
