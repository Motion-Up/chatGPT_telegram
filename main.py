import os

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv

from telegram_class import Telegram

load_dotenv()

TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')
telegram_bot = Telegram()


def main():
    bot = telegram.Bot(token=TELEGRAM_API_KEY)

    updater = Updater(token=TELEGRAM_API_KEY, use_context=True)

    # Получаем диспетчер сообщений
    dispatcher = updater.dispatcher

    # Создаем обработчик команды /start
    start_handler = CommandHandler('start', telegram_bot.start)
    dispatcher.add_handler(start_handler)

    # Создаем обработчик текстовых сообщений
    echo_handler = MessageHandler(Filters.text & (~Filters.command), telegram_bot.response_chatGPT)
    dispatcher.add_handler(echo_handler)

    # Запускаем бота
    updater.start_polling()

    # Запускаем бесконечный цикл обработки сообщений
    updater.idle()

if __name__ == '__main__':
    main()
