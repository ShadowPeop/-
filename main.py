import os

from flask import Flask, request
from telebot import types

import telebot

TOKEN = '5247574196:AAFnSeAipdSm7tNp6ULSJ7n4LCrR1Y_WVwA'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


vopros = ["как зовут главного героя", "как зовут сына гланого героя", "какие монстры были в первом мире в который попал кратос", "сколько кратос нашел драконов", "как его звали в начале игры", "кто это"]
pravilno = ["Кратос", "Атрей", "Темные эльфы", "4", "чужак", "Фрея"]


@bot.message_handler(content_types = ['text'])
def eho(message):
  if message.text == "/start":
    bot.send_message(message.chat.id, vopros[0])
    bot.register_next_step_handler(message, check)

def check(message):
    if message.text == pravilno[0]:
      bot.send_message(message.chat.id, "верно")
    else:
      bot.send_message(message.chat.id, "неверно")
    bot.send_message(message.chat.id, vopros[1])
    bot.register_next_step_handler(message, check2)

def check2(message):
    if message.text == pravilno[1]:
      bot.send_message(message.chat.id, "верно")
    else:
      bot.send_message(message.chat.id, "неверно")
    bot.send_message(message.chat.id, vopros[2])
    bot.register_next_step_handler(message, check3)
def check3(message):
    if message.text == pravilno[2]:
      bot.send_message(message.chat.id, "верно")
    else:
      bot.send_message(message.chat.id, "неверно")
    bot.send_message(message.chat.id, vopros[3])
    bot.register_next_step_handler(message, check4)
def check4(message):
    if message.text == pravilno[3]:
      bot.send_message(message.chat.id, "верно")
    else:
      bot.send_message(message.chat.id, "неверно")
    bot.send_message(message.chat.id, vopros[4])
    img = open("gods-kratos-killed-15.jpg", 'rb')
    bot.send_photo(message.chat.id, img)
    img.close()
    bot.register_next_step_handler(message, check5)
def check5(message):
    if message.text == pravilno[4]:
      bot.send_message(message.chat.id, "верно")
    else:
      bot.send_message(message.chat.id, "неверно")
    bot.send_message(message.chat.id, vopros[5])
    img = open("ahtz.jpg", 'rb')
    bot.send_photo(message.chat.id, img)
    img.close()
    bot.register_next_step_handler(message, check6)
def check6(message):
     bot.send_message(message.chat.id, "Вы прошли тест")


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200
    
@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://shddd.herokuapp.com/' + TOKEN)
    return "!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
