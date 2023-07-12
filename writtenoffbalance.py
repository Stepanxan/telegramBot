from conf import bot
from telebot import types


class WrittenOffBalance():

    # Кнопка вибору кнопоки списання балансу
    @staticmethod
    def choose_written_off_balance(message):
        chat_id = message.chat.id
        markup = types.ReplyKeyboardMarkup(row_width=1)
        btn_1 = types.KeyboardButton('💸 Списання балансу')
        markup.row(btn_1)
        bot.send_message(chat_id, 'Підтвердіть списання балансу', reply_markup=markup)

    # Обробник натискання кнопоки списання балансу
    @staticmethod
    def handle_written_off_balance(message):
        chat_id = message.chat.id
        vertical = message.text
        bot.send_message(chat_id, f'Ви обрали: {vertical}')