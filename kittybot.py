from telegram.ext import CommandHandler, Updater, Filters, MessageHandler
from telegram import ReplyKeyboardMarkup
import requests

URL = 'https://api.thecatapi.com/v1/images/search'
update = Updater(token='5306488432:AAHSUp-jzHTOGqbv9NOlsJfLfelCY8dbrdE')


def say_hi(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    print(update)
    context.bot.send_message(
        chat_id=chat.id,
        text='Привет {}, я KittyBot!'.format(name))


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([
        ['показать фото :joy:'],
        ['показать время'],
        ['/random_digit']
        ])
    context.bot.send_message(
        chat_id=chat.id,
        text='Спасибо {}, я теперь работаю!!!'.format(name),
        reply_markup=button
        )


def nah(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    context.bot.send_message(
        chat_id=chat.id,
        text='Не ругайся матом{}, а то отшлёпаю'.format(name)
        )

def get_img(update, context):
    response = requests.get(URL).json()
    
    context.bot.send_message(
        chat_id=chat.id,
        text='Не ругайся матом{}, а то отшлёпаю'.format(name)
        )

def new_cat(update, context):
    response = requests.get(URL).json()
    
    context.bot.send_message(
        chat_id=chat.id,
        text='Не ругайся матом{}, а то отшлёпаю'.format(name)
        )

update.dispatcher.add_handler(CommandHandler('start', wake_up))

update.dispatcher.add_handler(CommandHandler('newcat', new_cat))

update.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))


update.start_polling()
update.idle()
