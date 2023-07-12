from conf import bot
from telebot import types

class Product():

    # Кнопка вибору кнопоки продукт і всі його комплетуючі разом з мануалом
    @staticmethod
    def choose_product(message):
        chat_id = message.chat.id
        markup = types.ReplyKeyboardMarkup(row_width=1)
        btn_1 = types.KeyboardButton('продукт і всі його комплетуючі разом з мануалом')
        markup.row(btn_1)
        bot.send_message(chat_id, 'продукт і всі його комплетуючі разом з мануалом', reply_markup=markup)

    # Обробник натискання продукт і всі його комплетуючі разом з мануалом
    @staticmethod
    def handle_product(message):
        chat_id = message.chat.id
        vertical = message.text
        bot.send_message(chat_id, f'Ви обрали: {vertical}')