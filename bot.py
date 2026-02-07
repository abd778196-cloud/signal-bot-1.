import telebot
from telebot import types

TOKEN = "PUT_YOUR_BOT_TOKEN_HERE"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=[ start ])
def start(message):
    bot.send_message(message.chat.id, "أهلاً بك 👋\nبوت الإشارات شغال بنجاح ✅")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, "تم استلام رسالتك 📩")

print("Bot is running...")
bot.infinity_polling()
