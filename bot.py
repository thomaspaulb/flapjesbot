import time
import telepot

import config

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    command = msg['text']

    if command == '/camera':
        bot.sendMessage(chat_id, 'Hallo!')

bot = telepot.Bot(config.API_KEY)
bot.message_loop(handle)
print 'I am listening ...'

while 1:
    time.sleep(10)
