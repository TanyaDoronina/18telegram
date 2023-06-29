import telebot


bot = telebot.TeleBot('5689642465:AAE6-ZphLlMEskwIDhbL5kcGGBkbaqyvjqw')
@bot.message_handler(content_types=['voice', ])
def repeat(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'у тебя очень красивый голос')

bot.polling(none_stop=True)

