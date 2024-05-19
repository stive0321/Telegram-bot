import telepot
from telepot.loop import MessageLoop
import time
from config import TELEGRAM_BOT_TOKEN
from commands import start, help, info, status, ai

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text'].split()[0]

    if command == '/start':
        start.handle(chat_id, msg)
    elif command == '/help':
        help.handle(chat_id, msg)
    elif command == '/info':
        info.handle(chat_id, msg)
    elif command == '/status':
        status.handle(chat_id, msg)
    elif command.startswith('/ask'):
        ai.handle(chat_id, msg)
    else:
        telepot.Bot(TELEGRAM_BOT_TOKEN).sendMessage(chat_id, 'Unknown command. Type /help to see the available commands.')

bot = telepot.Bot(TELEGRAM_BOT_TOKEN)
MessageLoop(bot
  
