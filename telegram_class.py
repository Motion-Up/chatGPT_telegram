import os
from dotenv import load_dotenv

from chatgpt import ChatGPT

load_dotenv()

CHAT_GPT_KEY = os.getenv('CHAT_GPT_KEY')
IGNAT = os.getenv('IGNAT')
NIKOLAY = os.getenv('NIKOLAY')


class Telegram:

    def start(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="ChatGPT бот запущен!")

    def response_chatGPT(self, update, context):
        if str(update.effective_chat.id) in [IGNAT, NIKOLAY]:
            chat = ChatGPT(CHAT_GPT_KEY)
            response = chat.get_response_from_chat(update.message.text)
            context.bot.send_message(chat_id=update.effective_chat.id, text=response)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="У вас нет доступа к этому боту!")