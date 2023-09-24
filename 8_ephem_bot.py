"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging

import ephem
from datetime import datetime
from settings import TGBOT_KEY
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')    

def planet_info(update, context):
    user_request = update.message.text
    planet = user_request.split()[1]
    if planet == 'Mercury':
        planet = ephem.Mercury()
    elif planet == 'Venus':
        planet = ephem.Venus()
    elif planet == 'Mars':
        planet = ephem.Mars()
    elif planet == 'Jupiter':
        planet = ephem.Jupiter()
    elif planet == 'Saturn':
        planet = ephem.Saturn()
    elif planet == 'Uranus':
        planet = ephem.Uranus()
    elif planet == 'Neptune':
        planet = ephem.Neptune()
    else:
        response = 'для этой планеты нет созвездия'
        update.message.reply_text(response)
    planet.compute(datetime.now())
    response = ephem.constellation(planet)[1]
    update.message.reply_text(f'В созвездии {response}')


def greet_user(update, context):
    text = 'Доступные команды:\n/planet'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(TGBOT_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_info))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
