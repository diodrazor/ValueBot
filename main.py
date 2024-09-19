import telebot
from config import TOKEN, keys
from extensions import APIException, ValueConverter
from telebot import types
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start', 'help'])
def start_function(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате: \n<имя валюты>\
‹в какую валюту перевести> \ ‹количество переводимой валюты>\nУвидеть список всех доступных валют: /values\n (название любой валюты с маленькой буквы)'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = types.KeyboardButton('доллар евро 1')
    itembtn2 = types.KeyboardButton('евро доллар 1')
    itembtn3 = types.KeyboardButton('доллар рубль 1')
    itembtn4 = types.KeyboardButton('евро рубль 1')
    itembtn5 = types.KeyboardButton('юань рубль 1')
    itembtn6 = types.KeyboardButton('доллар юань 1')
    markup.row(itembtn1, itembtn2)
    markup.row(itembtn3, itembtn4)
    markup.row(itembtn5, itembtn6)
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.message_handler (commands=['values'])
def values (message: telebot. types. Message):
    text = 'Доступные валюты: '
    for key in keys.keys():
        text = '\n'. join((text, key))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def value(message: telebot.types.Message):
    try:
        text = message.text.split()
        if len(text)!= 3:
            raise APIException('Неверное количество параметров')
        base, quote, amount = text
        total_base = ValueConverter.get_price(base, quote, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'He удалось обработать команду\n{e}')
    else:
        # print(total_base)
        bot.reply_to(message, total_base)


bot.polling()
"""
import requests
import json
a = requests.get("http://data.fixer.io/api/latest?access_key=0f55eef4a61508ec1b549df88eeed941")
b = json.loads(a.content)
print(b)"""