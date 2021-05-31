import telebot
import recommend_system

token = '1675003500:AAEGMnM_DG3Qw0liRGltidp773L81iJxfag'
bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я первый телеграм-бот на русском языке, который может посоветовать фильмы.' +  '\n' +
                     'Напиши мне название любого фильма, и я вышлю список из 3 фильмов, которые рекомендованы для тебя.' + '\n' +
                     'В дальнейшем будут реализованы и другие функции, также будет выдаваться не только название фильма')

@bot.message_handler(content_types = ['text'])
def recommend(message):
    mes = recommend_system.recommender(title = message.text)
    for i in range(3):
        bot.send_message(message.chat.id, mes[i])

if __name__ == '__main__':
     bot.polling(timeout = 10)