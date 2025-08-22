
try:
    a = float(input("Ведіть перше число: "))
    b = float(input("Ведіть друге число: "))
    result = a / b
    print("Результат ділення:", result)
except ValueError:
    print("Помилка: ведене значення не є числом!")
except ZeroDivisionError:
    print("Помилка: ділення на нуль неможливе!")
finally:
    print("Операція завершена (Завдання 1).")


numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Ведіть індекс елемента зі списку (0-4): "))
    print("Елемент за індексом:", numbers[index])
except ValueError:
    print("Помилка: індекс повинен бути числом!")
except IndexError:
    print("Помилка: індекс виходить за межі списку!")
finally:
    print("Операція завершена (Завдання 2).")


try:
    sales = input("Ведіть дані про продажі через пробіл: ")  
    sales_list = [int(x) for x in sales.split()]
    total = sum(sales_list)
    print("Загальна сума продажів:", total)
except ValueError:
    print("Помилка: введено некоректні дані!")
finally:
    print("Обробку завершено (Завдання 3).")
