#numbers = list(map(int, input("Введіть список чисел через пробіл: ").split()))

#count = 0
#result = []

#for i in range(1, len(numbers)):
    #if numbers[i] > numbers[i - 1]:
   #    count += 1
    #    result.append(numbers[i])

#print("Кількість елементів:", count)
#print("Послідовність:", result)


#numbers = list(map(int, input("Ведіть список чисел через пробіл: ").split()))

#unique = []
#for num in numbers:
    #if numbers.count(num) == 1:
       # unique.append(num)

#print("Результат:", unique)


numbers = list(map(int, input("Ведіть список чисел через пробіл: ").split()))

max_seq = []
current_seq = [numbers[0]]

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        current_seq.append(numbers[i])
    else:
        if len(current_seq) > len(max_seq):
            max_seq = current_seq
        current_seq = [numbers[i]]

if len(current_seq) > len(max_seq):
    max_seq = current_seq

print("Довжина послідовності:", len(max_seq))
print("Послідовність:", max_seq)

