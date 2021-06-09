from telegram import Bot;
from telegram import Update;
from telegram.ext import Updater;
from telegram.ext import CommandHandler;
from telegram.ext import MessageHandler;
from telegram.ext import Filters;
import telebot
from telebot import types
from docxtpl import DocxTemplate

TG_TOKEN = ("1843494655:AAFIwteongNr6nH30si0aPdmYnJQA7vjdnk")

bot = telebot.TeleBot("1843494655:AAFIwteongNr6nH30si0aPdmYnJQA7vjdnk")



@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    test1_button = types.InlineKeyboardButton(text="Подписаться", callback_data='subscribe')
    keyboard.add(test1_button)
    bot.send_message(message.chat.id,"Добро пожаловать! ",reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if (call.data == "subscribe"):
     video = open("/Users/aleksandrten/Downloads/documentbot/studybot/Bird.mp4", "rb")
     bot.send_video(call.message.chat.id, video)





if __name__ == '__main__':
    bot.infinity_polling()
