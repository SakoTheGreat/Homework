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
    if (type(first_str) is str) and (type(second_str) is str):
        # Я так и не понял по заданию делать через if или все таки использовать elif 
        if first_str == second_str:
            return 1
        elif len(first_str) > len(second_str):
            return 2
        elif first_str != second_str and second_str == 'learn':
            return 3
    else:
        return 0


if __name__ == "__main__":
    main(first_str='ne', second_str='to')


print(main('forofor', 13134))
print(main('python', 'python'))
print(main('forofor', 'small'))
print(main('forof', 'learn'))