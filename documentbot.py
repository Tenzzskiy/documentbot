from telegram import Bot;
from telegram import Update;
from telegram.ext import Updater;
from telegram.ext import CommandHandler;
from telegram.ext import MessageHandler;
from telegram.ext import Filters;
import telebot
from telebot import types
from docxtpl import DocxTemplate

TG_TOKEN = ("1701456576:AAH7KdkRVig3tM6eqRp0veINIfZdHarHOcc")

bot = telebot.TeleBot("1701456576:AAH7KdkRVig3tM6eqRp0veINIfZdHarHOcc")

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    test1_button = types.InlineKeyboardButton(text="Тестовая кнопка", callback_data='pravodoc')
    test2_button = types.InlineKeyboardButton(text="Пустая кнопка", callback_data="faq")
    test3_button = types.InlineKeyboardButton(text="Пустая кнопка", callback_data='konsultation')
    test4_button = types.InlineKeyboardButton(text="Пустая кнопка", callback_data='business')
    keyboard.add(test1_button,test2_button,test3_button,test4_button)
    bot.send_message(message.chat.id,"Добро пожаловать! нажмите на тестовую кнопку для получения документа {} 👋 \nПривет",reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if (call.data == 'pravodoc'):
        bot.send_message(call.message.chat.id, 'Ваш готовый файл')
        doc = open("/Users/aleksandrten/Downloads/documentbot/test1.docx", "rb")
        bot.send_document(call.message.chat.id, doc)
        bot.register_next_step_handler(call.message, handle_start_help)

if __name__ == '__main__':
    bot.infinity_polling()
