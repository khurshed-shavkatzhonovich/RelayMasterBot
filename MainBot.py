import telebot

bot = telebot.TeleBot('7106678997:AAHQo55EywKxrKlsabfASsMR5Vl5szUd1IY')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет!')


bot.polling(none_stop=True)
