# Cоздать список, состоящий из четных чисел 
'''
# 1) в диапазоне от 1 до 100
list_1 = []
for i in range(1, 101):
    list_1.append(i)
print(list_1)
# Запишем решение сокращенно
list_1 = [i for i in range(1, 101)]
print(list_1)

# 2) только четные числа
list_1 = [i for i in range(1, 101) if i % 2 == 0]
print(list_1)

# Cоздать пару каждому из чисел (кортежи)
list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]
print(list_1)

# Умножить на 2
list_1 = [i * 2 for i in range(10) if i % 2 = 0]
print(list_1)
'''

# Округление в большую сторону
'''
import math
dayDistance = int(input('Введите расстояние за день: '))
overallDistance = int(input('Введите общее расстояние: '))
print(f"{math.ceil(overallDistance / dayDistance)} ")
'''

'''
class_1 = 3
m = class_1//2 + class_1%2
print(m)                       # 2
'''

# Сумма трехзначного числа:
'''
n1 = n // 100 # Нахождение первой цифры числа
n2 = (n % 100) // 10 # Нахождение второй цифры числа
n3 = n % 10 # Нахождение третьей цифры числа
res = n1 + n2 + n3
'''

# Нахождение каждой цифры числа
'''
n = 123456
n1 = n // 100000            # 1
n2 = (n % 100000) // 10000  # 2
n3 = (n % 10000) // 1000    # 3
n4 = (n % 1000) // 100      # 4
n5 = (n % 100) // 10        # 5
n6 = n % 10                 # 6
'''

# Нахождение минимума и максимума
'''
import random

num_N = int(input('Введите кол-во арбузов: '))
watermelon = []

for i in range(num_N):
    watermelon.append(random.randint(1, 10))
print(watermelon)

print(min(watermelon), max(watermelon))
'''

# Нахождения факториала от 1 до N
'''
num_n = int(input('Введите число: '))
factorial_N = 1

while num_n > 0:
    factorial_N = factorial_N * num_n
    num_n -= 1
print(factorial_N)
'''

# Cдвиг налево и направо
"""
## через срезы
'''
k = int(input('Введите число К: '))
num_list = num_list[-k:] + num_list[:-k] # cдвиг справо
num_list = num_list[k:] + num_list[:k]   # сдвиг налево
'''
##через ".pop"
'''
for _ in range(k):
    num_list.insert(0, num_list.pop())
'''
"""


# Убирает пробелы
'''
.strip(" ")
'''
