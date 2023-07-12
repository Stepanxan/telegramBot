from conf import bot
from telebot import types

class Upplybutton():

    # Кнопка вибору кнопоки кнопка оплати
    @staticmethod
    def choose_button(message):
        chat_id = message.chat.id
        markup = types.ReplyKeyboardMarkup(row_width=1)
        btn_1 = types.KeyboardButton('💳 кнопка оплати')
        markup.row(btn_1)
        bot.send_message(chat_id, 'Виберіть кнопку оплати', reply_markup=markup)

    # Обробник натискання кнопоки кнопка оплати
    @staticmethod
    def handle_button(message):
        chat_id = message.chat.id
        vertical = message.text
        bot.send_message(chat_id, f'Ви обрали: {vertical}')