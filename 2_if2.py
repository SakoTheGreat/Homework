"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(first_str, second_str):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    if not ((type(first_str) is str) and (type(second_str) is str)):
        return 0 
    else:
        if first_str == second_str:
            return 1
        elif len(first_str) > len(second_str):
            return 2
        elif second_str == 'learn':
            return 3


if __name__ == "__main__":
    print(main('forofor', 13134))
    print(main('python', 'python'))
    print(main('forofor', 'small'))
    print(main('forof', 'learn'))


