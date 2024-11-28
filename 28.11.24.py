# Задача 6
N = int(input(" Введите число N: "))
a = 0
for i in range(2, N, 2):
    a = a + i
print(f"{a} (", end="")
for i in range(2, N, 2):
    print(f"{i}+", end="")
print("\b)")

# Задание 7
N = int(input(" Введите число N: "))
a = 1
for i in range(1, N + 1):
    a = a * i
print(f"{a} ({N}! =", end=" ")
for i in range(N, 0, -1):
    print(f"{i}*", end="")
print("\b)")

# Задание 8
N = int(input(" Введите число N: "))
a = 0
b = N
c = N
for i in str(N):
    a = a + 1
for i in range(1, a + 1):
    b = c % 10
    c = c // 10
    print(b, end=" ")

# Задание 9
N = int(input(" Введите число N: "))
a = 0
for i in str(N):
    a = a + 1
print(a)

# Задание 10
N = int(input(" Введите число N: "))
a = 0
for i in str(N):
    a = a + int(i)
print(a, "(", end="")
for j in str(N):
    print(f"{j}+", end="")
print("\b)")