
print("\n--- Завданя 1: Розрахунок фінальної ціни ---")
try:
    price = float(input("Ведіть вихідну ціну товару: "))
    discount = float(input("Ведіть відсоток знижки: "))
    final_price = price * (1 - discount / 100)
    print(f"Фінальна ціна: {final_price:.2f} грн")
except ValueError:
    print("Помилка: введено некоректні дані!")
finally:
    print("Обчислення завершено\n")


print("\n--- Завдання 2: Конвертація доларів в євро ---")
try:
    usd = float(input("Ведіть суму у доларах: "))
    rate = float(input("Ведіть курс обміну USD → EUR: "))
    if rate == 0:
        raise Exception("Курс обміну не може дорівнювати нулю!")
    eur = usd * rate
    print(f"Сума у євро: {eur:.2f}")
except ValueError:
    print("Помилка: введено некоректні дані!")
except Exception as e:
    print(f"Помилка: {e}")
finally:
    print("Операція завершена.\n")


print("\n--- Завдання 3: Середня оцінка студентів ---")
try:
    grades_input = input("Введіть оцінки через пробіл (наприклад: 85 90 78): ")
    grades = [int(x) for x in grades_input.split()]
    if not grades:
        raise ZeroDivisionError("Список оцінок порожній!")
    avg = sum(grades) / len(grades)
    print(f"Середня оцінка: {avg:.2f}")
except ValueError:
    print("Помилка: ведено некоректні оцінки!")
except ZeroDivisionError as e:
    print(f"Помилка: {e}")
finally:
    print("Завершеня обчислень.\n")


print("\n--- Завдання 4: Банкомат ---")
BALANCE = 1000  
try:
    amount = int(input("Ведіть суму для знятя: "))
    if amount % 10 != 0 or amount > BALANCE:
        raise Exception("Некоректна сума для знятя!")
    BALANCE -= amount
    print(f"Зняття успішне! Новий баланс: {BALANCE} грн")
except ValueError:
    print("Помилка: введено некоректні дані!")
except Exception as e:
    print(f"Помилка: {e}")
finally:
    print("Транзакція завершена.\n")
