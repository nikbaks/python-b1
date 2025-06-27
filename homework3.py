a = int(input("Ведіть перше число: "))
b = int(input("Ведіть друге число: "))

even_sum = 0
odd_sum = 0
div9_sum = 0
even_count = 0
odd_count = 0
div9_count = 0

for i in range(min(a, b), max(a, b) + 1):
    if i % 2 == 0:
        even_sum += i
        even_count += 1
    else:
        odd_sum += i
        odd_count += 1
    if i % 9 == 0:
        div9_sum += i
        div9_count += 1






print("Сума парних:", even_sum, "Середнє:", even_sum / even_count if even_count else 0)
print("Сума непарних:", odd_sum, "Середнє:", odd_sum / odd_count if odd_count else 0)
print("Сума кратних 9:", div9_sum, "Середнє:", div9_sum / div9_count if div9_count else 0)
   

length = int(input("Ведіть довжину лінії: "))
symbol = input("Ведіть символ: ")

for i in range(length):
    print(symbol)




while True:
    num = int(input("Введіть число: "))
    if num > 0:
        print("Number is positive")
    elif num < 0:
        print("Number is negative")
    else:
        print("Number is equal to zero")
    
    if num == 7:
        print("Goodbye!")
        break


total = 0
min_num = None
max_num = None

while True:
    num = int(input("Ведіть число: "))
    if num == 7:
        print("Goodbye!")
        break
    total += num
    if min_num is None or num < min_num:
        min_num = num
    if max_num is None or num > max_num:
        max_num = num

print("Сума:", total)
print("Мінімум:", min_num)
print("Максимум:", max_num)







