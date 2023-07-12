import telebot

token = '6322977859:AAHuQBiddHs0KUOgffgGSuHGTnLrxyAabfI'
secret = 'v1Wyg9nZIQVw)kso8b4'
url = 'https://Stepan4k.pythonanywhere.com/' + secret

bot = telebot.TeleBot(token, threaded=False)
bot.remove_webhook()
bot.set_webhook(url=url)

