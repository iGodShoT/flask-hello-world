import os
import pip
pip.main(['install', 'pytelegrambotapi'])
import telebot
import time
from flask import Flask

bot = telebot.TeleBot('8005837758:AAEY0wZDeto4tchPqWnJ3DssgxXpDrrAuJk')

app = Flask('')

@app.route('/')
def home():
  return "I'm alive"