"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
age = input('Введите свой возраст смертный ')


def main(age):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    
 
      # Попытка принимать и не целые числа, и со знаком минуса=)
    age = int(age)  
    if 1<=age<7:
        return 'Да вашему ребенку срочно нужно в садик'
    elif age<=18:
        return 'Добро пожаловать в самые "лучшие" годы в жизни'
    elif age<=65:
        return 'Тут выбор непростой=) Армия, институт, работа!'
    else:
        return 'Свое ты уже отработал, научился, кайфанул... пора бы и честь знать! Заслуженная пенсия!'
     


if __name__ == "__main__":
    nu_teper_tochno_pravilno = main(age)
    print(nu_teper_tochno_pravilno)
