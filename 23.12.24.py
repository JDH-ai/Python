# Задача 1
from itertools import combinations

numbers = [1,3,5,7,2,4,6,8]
max_sum = 10
groups = []
current_group = []
current_sum = 0
for num in numbers:
    if current_sum + num <= max_sum:
        current_group.append(num)
        current_sum += num
    else:
        groups.append(current_group)
        current_group = [num]
        current_sum = num
if current_group:
    groups.append(current_group)
print(groups)

# Задача 2
items = [1,2,3,4]
k = 2
combinations_list = [
    (items[i], items[j])
    for i in range(len(items))
    for j in range(i + 1, len(items))
]
print(combinations_list)
