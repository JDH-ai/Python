# Задача 1
numbers = []
for i in range(5):
    number = int(input(f"Введите целое число {i + 1}: "))
    numbers.append(number)
print("Список чисел: ", numbers)

# Задача 2
numbers = []
for i in range(5):
    number = int(input(f"Введите целое число {i + 1}: "))
    numbers.append(number)
total_sum = sum(numbers)
print("Сумма всех элементов списка: ", total_sum)

# Задание 3
numbers = []
for i in range(5):
    number = int(input(f"Введите целое число {i + 1}: "))
    numbers.append(number)
max_number = max(numbers)
print("Максимальный элемент в списке: ", max_number)

# Задача 4
numbers = [6,8,3,5,9,4,6,8]
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
print("Список с уникальными элементами: ", unique_numbers)

# Задача 5
list1 = [6,7,8]
list2 = [4,5,2]
merged_list = list1 + list2
print("Обьедененный список: ", merged_list)

# Задача 6
my_list = [5,6,7,8,9]
my_list.reverse()
print(my_list)

# Задача 7
my_list = [8,4,1,6,3,9,0,3]
my_list.sort()
print(my_list)

# Задача 8
list1 = [1,5,0]
list2 = [2,8,4]
merged_list = []
i,j = 0,0
while i < len(list1) and j < len(list2):
    if list1[i] == list2[j]:
        merged_list.append(list1[i])
        i += 1
    else:
        merged_list.append(list2[j])
        j += 1
while i < len(list1):
    merged_list.append(list1[i])
    i += 1
while j < len(list2):
    merged_list.append(list2[j])
    j += 1
print(merged_list)

# Задание 9
numbers = [9,5,3,2,7,6,0,1]
min_num = min(numbers)
max_num = max(numbers)
print("Минимальный элемент: ", min_num)
print("Максимальный элемент: ", max_num)

# Задание 10
numbers = [8,9,1,0,6,5]
for i in range(0,len(numbers) -1,2):
    numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
print("Список после перестановки: ", numbers)