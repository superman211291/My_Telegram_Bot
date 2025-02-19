import telebot

# токен бота
bot = telebot.TeleBot("7947969538:AAGeRi_1b7E-AbidZxvhfjsJ06Mn9UHDu30")
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я не знаю такой команды. Напиши /help.")
        bot.polling(none_stop=True, interval=0)