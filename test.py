import telegramm.ext
import os

from telegramm.ext import Updater, CommandHandler, MessageHandler, Filters

PORT = int(os.environ.get('PORT', '8443'))


def starts(updater, context):
    update.message.reply_text('Hi')

def echo(update,context):
    update.message.reply_text(update.message.text)


def main():

    TOKEN = ''
    APP_NAME = ''

    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path = TOKEN, webhook_url=APP_NAME+ TOKEN)
    updateridle()

if __