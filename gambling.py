from conf import bot
from telebot import types

class Gembling():

#Кнопка вибору гембінга
    @staticmethod
    def choose_gempling(message):
        chat_id = message.chat.id

        # Створення клавіатури з кнопками гембінга
        markup = types.ReplyKeyboardMarkup(row_width=1)
        btn_1 = types.KeyboardButton('🔴 ленд')
        btn_2 = types.KeyboardButton('🟠 преленд')
        btn_3 = types.KeyboardButton('🟢 тг бот')
        btn_4 = types.KeyboardButton('🔵 кастом')
        back = types.KeyboardButton('⬅️ Назад')
        markup.row(btn_1, btn_2, btn_3, btn_4, back)
        bot.send_message(chat_id, 'Оберіть тип гемблінга', reply_markup=markup)


# Обробник натискання кнопок гемблінга
    @staticmethod
    def handle_gembling(message):
        chat_id = message.chat.id
        vertical = message.text
        if message.text == '⬅️ Назад':
            markup = types.ReplyKeyboardMarkup(row_width=1)
            btn_1 = types.KeyboardButton('🎰 гемблінг')
            markup.row(btn_1)
            bot.send_message(message.chat.id, 'повернувся до вибору вертикалі', reply_markup=markup)
        else:
            bot.send_message(chat_id, f'Ви обрали гемблінг: {vertical}')
