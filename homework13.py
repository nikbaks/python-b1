import os

def task1():
    with open("data.txt", "w", encoding="utf-8") as file:
        for i in range(3):
            line = input(f"Ведіть рядок {i+1}: ")
            file.write(line + "\n")
    print("Дані записані у файл data.txt")


def task2():
    if os.path.exists("data.txt"):
        print("Файл data.txt існує.")
        with open("data.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            print("Кожен другий рядок файлу:")
            for i in range(1, len(lines), 2):
                print(lines[i].strip())
    else:
        print("Файл data.txt не знайдено")


def task3():
    if os.path.exists("data.txt"):
        with open("data.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        filtered = [line for line in lines if "Python" in line]

        with open("filtered.txt", "w", encoding="utf-8") as out:
            out.writelines(filtered)
        print("Фільтровані рядки збережено у filtered.txt")
    else:
        print("Файл data.txt не знайдено!")


def task4():
    filename = input("Ведіть ім'я файлу: ")
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        cleaned = ''.join(ch for ch in content if not ch.isdigit())

        with open("cleaned.txt", "w", encoding="utf-8") as out:
            out.write(cleaned)
        print("Результат збережено у cleaned.txt")
    else:
        print("Файл не знайдено")
