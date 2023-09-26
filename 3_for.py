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

def avg_calc(lst: list):
    sold_count, sum = sum_calc(lst)
    avg = sum/sold_count
    return avg

def sum_calc(lst: list):
    sum = 0
    for i in range(len(lst)):
        sum=sum+lst[i]
    return i+1, sum

def total_sold(data):
    total_sum = 0
    for i in data:
        sold_count, product_sum = sum_calc(i["items_sold"])
        total_sum = total_sum+product_sum
    print(f'Суммарное количество продаж всех товаров: {total_sum}')

def average_sold(data):
    sold_count, product_sum = 0, 0
    for i in data:
        sold_count, product_sum = sum_calc(i["items_sold"])
        sold_count += sold_count
        product_sum += product_sum
    avg_sold=product_sum/sold_count
    print(f'Среднее количество продаж всех товаров: {avg_sold}')


def average_sold_by_item(data):
    for i in data:
        avg = avg_calc(i['items_sold'])
        print(f'Среднее количество продаж для {i["product"]}: {avg}')

def total_sold_by_item(data):
    for i in data:
        sold_count, sum = sum_calc(i["items_sold"])
        print(f'Суммарное количество продаж для {i["product"]}: {sum}')
        

def main():
    data = [
    {'product': 'iPhone 12','items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
    total_sold_by_item(data)
    print("\n")
    average_sold_by_item(data)
    print("\n")
    total_sold(data)
    print("\n")
    average_sold(data)
    
if __name__ == "__main__":
    main()
