a = int(input("Ведіть перше число: "))
b = int(input("Ведіть друге число: "))

for i in range(min(a, b), max(a, b) + 1):
    print(i)


a = int(input("Ведіть перше число: "))
b = int(input("Ведіть друге число: "))

for i in range(min(a, b), max(a, b) + 1):
    if i % 2 != 0:
        print(i)


a = int(input("Ведіть перше число: "))
b = int(input("Ведіть друге число: "))

for i in range(max(a, b), min(a, b) - 1, -1):
    if i % 2 == 0:
        print(i)
