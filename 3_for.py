"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

spicok_slovarei = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]


def main(spicok_slovarei):
    
    sum_product = {}
    average_sum_product = {}
    all_sum_products = 0
    average_sum_all = 0
    for slovar in spicok_slovarei:
        sum_product[slovar['product']] = sum_product.get(slovar['product'], sum(slovar['items_sold']))
        average_sum_product[slovar['product']] = average_sum_product.get(slovar['product'], int((sum(slovar['items_sold'])/len(slovar['items_sold']))))

    for i, j in sum_product.items():
        all_sum_products += j

    for i, j in average_sum_product.items():    
        average_sum_all += j

    average_sum_all = int(average_sum_all/3)

    return f'''
Сумма продаж каждого прoдукта по отдельности {sum_product}
Среднее количество продаж каждого продукта {average_sum_product}
Сумма продаж всех продуктов {all_sum_products}
Среднее количество продаж каждого продукта {average_sum_all}'''

if __name__ == "__main__":
    return_to_the_basic = main(spicok_slovarei)

    print(return_to_the_basic)


