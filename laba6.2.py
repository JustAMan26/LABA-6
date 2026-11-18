# -*- coding: utf-8 -*-

# Чтение массива из файла
fi = open("lab6_4.txt", "rt")

# Пропуск заголовка
fi.readline()  # # Одномерный массив
fi.readline()  # #-------------------

# Чтение данных
line = fi.readline()
mas = [float(x) for x in line.split()]
fi.close()

n = len(mas)

# 1. Произведение положительных элементов
prod_pos = 1.0
for i in range(n):
    if mas[i] > 0:
        prod_pos *= mas[i]

# 2. Сумма элементов до минимального
min_val = mas[0]
min_idx = 0
for i in range(1, n):
    if mas[i] < min_val:
        min_val = mas[i]
        min_idx = i

sum_before_min = 0.0
for i in range(min_idx):
    sum_before_min += mas[i]

# 3. Сортировка отдельно четных и нечетных индексов
even_elements = []  # индексы 0, 2, 4, ...
odd_elements = []   # индексы 1, 3, 5, ...

for i in range(n):
    if i % 2 == 0:
        even_elements.append(mas[i])
    else:
        odd_elements.append(mas[i])

# Сортировка по возрастанию
even_elements.sort()
odd_elements.sort()

# Восстановление массива
result = []
even_idx = 0
odd_idx = 0
for i in range(n):
    if i % 2 == 0:
        result.append(even_elements[even_idx])
        even_idx += 1
    else:
        result.append(odd_elements[odd_idx])
        odd_idx += 1

# Запись результатов в файл
fo = open("lab6_4_out.txt", "wt")

fo.write("Исходный массив:\n")
for i in range(n):
    fo.write("{0:7.2f}".format(mas[i]))
fo.write("\n\n")

fo.write("1. Произведение положительных элементов: {0:.4f}\n".format(prod_pos))
fo.write("2. Минимальный элемент: {0:.2f} (индекс {1})\n".format(min_val, min_idx))
fo.write("3. Сумма элементов до минимального: {0:.4f}\n\n".format(sum_before_min))

fo.write("Массив после сортировки:\n")
fo.write("Четные индексы (отсортированы): ")
for val in even_elements:
    fo.write("{0:.2f} ".format(val))
fo.write("\n")

fo.write("Нечетные индексы (отсортированы): ")
for val in odd_elements:
    fo.write("{0:.2f} ".format(val))
fo.write("\n\n")

fo.write("Итоговый массив:\n")
for i in range(n):
    fo.write("{0:7.2f}".format(result[i]))
fo.write("\n")

fo.close()

print("Результаты записаны в файл lab6_4_out.txt")