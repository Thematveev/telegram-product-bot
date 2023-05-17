from telebot import TeleBot
from commands.low import low_controller
from keyboards import main_markup

TOKEN = "6163778644:AAEjDv5FauetPZH_uN7dVaW5RpsQmbQJB7A"

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['low'])
def low(message):
    low_controller(message, bot)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Выберите дейстие", reply_markup=main_markup())


bot.polling()
