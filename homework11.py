numbers = list(map(int, input("Ведіть елементи списку через пробіл: ").split()))
total_sum = sum(numbers)
average = total_sum / len(numbers) if numbers else 0
print(f"Сума елементів: {total_sum}")
print(f"Середнє арифметичне: {average}")


numbers = list(map(int, input("Ведіть елементи списку через пробіл: ").split()))
num = int(input("Ведіть число для пошуку: "))
count = numbers.count(num)
print(f"Число {num} зустрічається {count} раз(и)")




numbers = list(map(int, input("Ведіть елементи списку через пробіл: ").split()))
positive_sum = sum([x for x in numbers if x > 0])
print(f"Сума додатних чисел: {positive_sum}")




numbers = list(map(int, input("Ведіть елементи списку через пробіл: ").split()))
even_indices = [i for i, x in enumerate(numbers) if x % 2 == 0]
print(f"Індекси парних чисел: {even_indices}")
