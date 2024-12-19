#!/usr/bin/python
import base64
# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
import re
import telebot
from telebot import types
import requests
from io import BytesIO
import PIL.Image

API_TOKEN = '7684324256:AAGLrK8CVtZyQFvtdLv3IMQDt0gMuR9ddCY'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['button'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("киску!")
    btn2 = types.KeyboardButton("мокрую киску!")
    # btn3 = types.KeyboardButton("Приватные услуги")
    # markup.add(btn1 , btn2, btn3)
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Выбери услугу".format(message.from_user), reply_markup=markup)
# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет, хочешь посмотреть киску? Напиши "киску!" или нажми кнопку"\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# @bot.message_handler(func=lambda message: True)

# def start(message): #Начало
# 	if message.text.lower() == 'вычисли сумму чисел' or message.text.lower() == '/sum':
# 		bot.send_message(message.from_user.id, 'Хорошо. Введи два числа которые ты хочешь суммировать. К примеру "1 и 5".')
# 		bot.register_next_step_handler(message, sumcalc)#"Перенаправляет" на след.функцию
# 	else:
# 		bot.send_message(message.from_user.id, 'Введи /sum, или напиши "Вычисли сумму чисел", чтобы продолжить.')
#
# def sumcalc(message):#После "перенаправления" функция сработает, лишь после получения message
#     number1, number2 = re.split(' и ', message.text, maxsplit = 1)
#     number1 = int(number1)
#     number2 = int(number2)
#     bot.send_message(message.from_user.id, 'Сумма двух введённых тобой чисел равна - ' + str(number1 + number2))

@bot.message_handler(func=lambda message: "киску!" in message.text.lower())
def cat_message(message):
    url = "https://cataas.com/"
    r = requests.get(url+"cat")
    # file_like = StringIO(r.content)
    img = PIL.Image.open(BytesIO(r.content))
    # img.show()
    bot.send_photo(message.chat.id, img)


bot.infinity_polling()