# -*- coding: utf-8 -*-
from math import *

def f1(m, n):
    """Вычисление первого выражения"""
    z1 = (m - 1) * sqrt(m) - (n - 1) * sqrt(n) / sqrt((m**3 * n) + n * m + m**2 - m)
    return z1

def f2(m, n):
    """Вычисление второго выражения"""
    z2 = sqrt(m) - sqrt(n) / m
    return z2

# Открытие файлов
fi = open("lab6_1.txt", "rt")  # читать
fo = open("lab6_1_out.txt", "wt")  # писать

# Пропуск заголовка
line = fi.readline()  # # m    n
line = fi.readline()  # #-----------

# Запись шапки таблицы результатов
fo.write("+======+======+=========+========+\n")
fo.write("|  m   |  n   |   z1    |   z2   |\n")
fo.write("+======+======+=========+========+\n")

# Обработка данных
for line in fi:
    if line == "\n":
        continue
    
    # Разделение строки
    parts = line.split()
    m = float(parts[0])
    n = float(parts[1])
    
    # Вычисления
    z1 = f1(m, n)
    z2 = f2(m, n)
    
    # Запись результата
    fo.write("|{0:6.2f}|{1:6.2f}|{2:9.4f}|{3:8.4f}|\n".format(m, n, z1, z2))
    fo.write("+------+------+---------+--------+\n")

# Закрытие файлов
fi.close()
fo.close()

print("Результаты записаны в файл lab6_1_out.txt")