from conf import bot
from telebot import types

class Vertical():

    @staticmethod
    def choose_vertical(message):
        chat_id = message.chat.id

        # Створення клавіатури з кнопками вертикалей
        markup = types.ReplyKeyboardMarkup(row_width=1)
        btn_1 = types.KeyboardButton('🎰 гемблінг')
        btn_2 = types.KeyboardButton('⚽️ бетінг')
        btn_3 = types.KeyboardButton('🧘 нутра')
        btn_4 = types.KeyboardButton('🛒 товарка')
        btn_5 = types.KeyboardButton('💰 крипта')
        back = types.KeyboardButton('⬅️ Назад')
        markup.row(btn_1, btn_2, btn_3, btn_4, btn_5, back)
        bot.send_message(chat_id, 'Оберіть вертикаль:', reply_markup=markup)

    @staticmethod
    def handle_vertical(message):
        chat_id = message.chat.id
        vertical = message.text
        if message.text == '⬅️ Назад':
            markup = types.ReplyKeyboardMarkup(row_width=1)
            btn_1 = types.KeyboardButton('🔢 Вибір вертикалі')
            markup.row(btn_1)
            bot.send_message(message.chat.id, 'повернувся до вибору вертикалі', reply_markup=markup)
        else:
            bot.send_message(chat_id, f'Ви обрали вертикаль: {vertical}')