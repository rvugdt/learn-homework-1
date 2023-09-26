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

def compare_strings(str1, str2):
    if isinstance(str1, str) and isinstance(str2, str):
        result = 0
    elif str1 == str2:
        result = 1
    elif str1 != str2 and len(str1) > len(str2):
        result = 2
    elif str1 != str2 and str2 == 'learn':
        result = 3
    return result

def main():
    try:
      print('hint: Ctrl+C для выхода')
      while True:
          str1 = input('\nПервая строка: ')
          str2 = input('Вторая строка: ')
          result = compare_strings(str1, str2)
          print(f'Результат: {result}')
    except KeyboardInterrupt:
        pass
        
if __name__ == "__main__":
    main()
