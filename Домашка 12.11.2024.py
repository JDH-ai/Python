# Задача 5
number = int(input(" Введите число: "))
reverse_number = 0
while number > 0:
    reverse_number = reverse_number * 10 + (number % 10)
    number = number // 10
print(reverse_number)

# Задача 6
number = int(input(" Введите положительное целое число: "))
sum_of_digits = 0
while number > 0:
    sum_of_digits += number % 10
    number = number // 10
print(" Сумма цифр числа: ", sum_of_digits)

# Задача 7
N = int(input(" Введите число N: "))
a, b = 0, 1
while a <= N:
    print(a, end =" ")
    a, b = b, a + b

# Задача 8
number = int(input(" Введите число: "))
reverse_number = 0
while number > 0:
    digit = number % 10
    reverse_number = reverse_number * 10 + digit
    number = number // 10
print(" Перевернутое число: ", reverse_number)
