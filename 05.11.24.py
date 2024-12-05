# Незакрашенный квадрат
a = 5
for i in range(a):
    for j in range(a):
        if i == 0 or i == a - 1 or j == 0 or j == a - 1:
           print("*", end="")
        else:
            print(" ", end="")
    print()
print()

# Закрашенный квадрат
a = 5
for i in range(a):
    for j in range(a):
        print("*", end="")
    print()

# Равносторонний незакрашенный треугольник
a = 5
for i in range(1, a + 1):
    for j in range(a - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2 or i == a:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Равносторонний закрашенный треугольник
a = 5
for i in range(1, a + 1):
    for j in range(a - i):
        print(" ", end="")
    for i in range(2 * i - 1):
        print("*", end="")
    print()

# Незакрашенный прямоугольный треугольник
a = 5
for i in range(1, a + 1):
    if i == 1 or i == a:
        print('*' * i)
    else:
        print('*' + ' ' * (i - 2) + '*')

# Закрашенный прямоугольный треугольник
a = 5
for i in range(1, a + 1):
    for j in range(i):
        print("*", end="")
    print()
print()

# Развернутый вниз и незакрашенный равнобедренный треугольник
a = 5
for i in range(a, 0, -1):
    for j in range(a - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2 or i == a:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Развернутый вниз и закрашенный равнобедренный треугольник
a = 5
for i in range(a, 0, -1):
    for j in range(a - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()