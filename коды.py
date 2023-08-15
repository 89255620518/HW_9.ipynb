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


