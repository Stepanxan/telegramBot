from conf import bot
from telebot import types

class Project():
    # Кнопка вибору кнопоки прикладу роботи і опису проекту
    @staticmethod
    def choose_project(message):
        chat_id = message.chat.id


        markup = types.ReplyKeyboardMarkup(row_width=1)
        btn_1 = types.KeyboardButton('💼 Приклад робіт і опис проекту')
        markup.row(btn_1)
        bot.send_message(chat_id, f'Ви обрали: {message.text}', reply_markup=markup)

    # Обробник натискання кнопоки прикладу роботи і опису проекту
    @staticmethod
    def handle_project(message):
        chat_id = message.chat.id
        vertical = message.text
        bot.send_message(chat_id, f'Ви обрали приклад роботи і опису проекту: {vertical}')
