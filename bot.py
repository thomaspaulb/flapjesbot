import time
import telepot
import sqlite3

import config


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    command = msg['text']

    if command == '/camera':
        bot.sendMessage(chat_id, 'Hallo!')
        print c


bot = telepot.Bot(config.API_KEY)
bot.message_loop(handle)
print 'I am listening ...'

conn = sqlite3.connect('billsplit.db')
c = conn.cursor()

while 1:
    time.sleep(10)
