import os
from telebot import TeleBot
from api import get_gpt_reply

BOT_TOKEN = os.environ['BOT_TOKEN']

bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def on_start(message):
  chat_id = message.chat.id
  text = 'Hi Dear Im Bot Created By:@GaelanKRD ، How can I help you'
  bot.send_message(chat_id,text)
  return

@bot.message_handler()
def on_message(message):
  chat_id = message.chat.id
  prompt = message.text[:250]
  bot.send_chat_action(chat_id,action='typing')
  text = get_gpt_reply(prompt,500)
  bot.send_message(chat_id,text)
  return

bot.infinity_polling()
