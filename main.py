import os
import telebot

TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Бот успешно запущен на Railway!")

bot.infinity_polling()
