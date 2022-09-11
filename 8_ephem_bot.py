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
from datetime import date
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters



logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')





def greet_user(update, context):
    update.message.reply_text('Use command "/planet [name]"')


def name_planet(update, context):
    user_text = update.message.text.split()
    today = date.today().strftime("%Y/%m/%d")
    planet_name = user_text[1].capitalize()
  
    if user_text[0] == '/planet' and len(user_text) < 2:
        if planet_name == 'Mars':
            constellationplanet = ephem.constellation(ephem.Mars(today))
        elif planet_name == 'Jupiter':
            constellationplanet = ephem.constellation(ephem.Jupiter(today))
        elif planet_name == 'Saturn':
            constellationplanet = ephem.constellation(ephem.Saturn(today))
        elif planet_name == 'Mercury':
            constellationplanet = ephem.constellation(ephem.Mercury(today))
        elif planet_name == 'Venus':
            constellationplanet = ephem.constellation(ephem.Venus(today))
        elif planet_name == 'Earth':
            constellationplanet = ephem.constellation(ephem.Earth(today))
        elif planet_name == 'Uranus':
            constellationplanet = ephem.constellation(ephem.Uranus(today))
        elif planet_name == 'Neptune':
            constellationplanet = ephem.constellation(ephem.Neptune(today))
        elif planet_name == 'Pluto':
            constellationplanet = ephem.constellation(ephem.Pluto(today))    
        else:
            update.message.reply_text('Unknown planet. Please try again')
        update.message.reply_text(f'Planete {planet_name} is in {constellationplanet[1]}')
    else:
        update.message.reply_text('Unknown command. Please try again')
        return





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
