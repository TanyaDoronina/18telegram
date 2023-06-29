import telebot


bot = telebot.TeleBot('5689642465:AAE6-ZphLlMEskwIDhbL5kcGGBkbaqyvjqw')

@bot.message_handler(commands=['start', 'help'])
def repeat(message: telebot.types.Message):
    bot.reply_to(message, f'Приветсвую, {message.chat.active_username}')

bot.polling(none_stop=True)