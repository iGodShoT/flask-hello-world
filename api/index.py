import os
import pip
pip.main(['install', 'pytelegrambotapi'])
import telebot
import time

bot = telebot.TeleBot('8005837758:AAEY0wZDeto4tchPqWnJ3DssgxXpDrrAuJk')

@bot.message_handler(content_types=['text'])
def get_text_message(message):
  bot.send_message(message.from_user.id,message.text)
# echo-функция, которая отвечает на любое текстовое сообщение таким же текстом   

bot.polling(non_stop=True, interval=0) #запуск бота