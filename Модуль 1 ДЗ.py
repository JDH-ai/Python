#Задача 1
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
operation = input("Введите действие(сумма/произведение): ")
if operation == "сумма":
  summ = a + b + c
  print("Сумма:", summ)
elif operation == "произведение":
  proizv = a * b * c
  print("Произведение:", proizv)
else:
  print("Некорректный выбор")

#Задача 2
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))
viv = int(input("максимум = 1: минимум = 2: среднеарифметическое = 3:" ))
if viv == 1:
  print(max(a, b, c))
elif viv == 2:
  print(min(a, b, c))
elif viv == 3:
  average = (a + b + c)/3
  print("Среднее значение", average)
else:
  print("Неправильный выбор")

#Задача 3
meters = float(input("Введите количество метров: "))
viv = int(input("мили = 1: дюймы = 2: ярды = 3: "))
if viv == 1:
 print(meters * 0.00062137)
elif viv == 2:
  print(meters * 39.37)
elif viv == 3:
  print(meters + 1.09361)
else:
  print("Неправильный выбор")


