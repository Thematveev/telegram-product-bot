from telebot import TeleBot
from commands.low import low_controller, category_controller

TOKEN = "6163778644:AAEjDv5FauetPZH_uN7dVaW5RpsQmbQJB7A"

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['low'])
def low(message):
    low_controller(message, bot)



bot.polling()
