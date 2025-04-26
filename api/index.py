from flask import Flask
import telebot

bot = telebot.TeleBot('8005837758:AAEY0wZDeto4tchPqWnJ3DssgxXpDrrAuJk')
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@bot.message_handler(content_types=['text'])
def get_text_message(message):
  bot.send_message(message.from_user.id,message.text)

bot.polling(non_stop=True, interval=0) #запуск бота
