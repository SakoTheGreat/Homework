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
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters



logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')





def greet_user(update, context):
    update.message.reply_text('Use command "/planet [name]"')


def name_planet(update, context):
    planet = update.message.text.split()
    try:
        planet_ephem = getattr(ephem, planet[1].capitalize())(datetime.now())
    
        constellation = ephem.constellation(planet_ephem)
      
        text = f"Планета {planet[1].capitalize()} находится в {constellation}"
    except AttributeError:
        text = f"Планета {planet[1].capitalize()} не найдена."
    update.message.reply_text(text)





def main():
    mybot = Updater("5672379591:AAGy1rdE_o0NHnTitJ_J8bqsjKCxeauFS54", use_context=True)

    dp = mybot.dispatcher

    dp.start
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, name_planet))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
