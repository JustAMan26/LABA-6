# -*- coding: utf-8 -*-
import numpy as np

def find_min_max_cols(matrix):
    """Поиск столбцов с минимальным и максимальным элементами"""
    n_rows, n_cols = matrix.shape
    
    max_val = matrix[0, 0]
    min_val = matrix[0, 0]
    max_col = 0
    min_col = 0
    
    for i in range(n_rows):
        for j in range(n_cols):
            if matrix[i, j] > max_val:
                max_val = matrix[i, j]
                max_col = j
            if matrix[i, j] < min_val:
                min_val = matrix[i, j]
                min_col = j
                
    return max_col, min_col

def swap_columns(matrix, col1, col2):
    """Обмен двух столбцов"""
    new_matrix = matrix.copy()
    n_rows = new_matrix.shape[0]
    
    for i in range(n_rows):
        temp = new_matrix[i, col1]
        new_matrix[i, col1] = new_matrix[i, col2]
        new_matrix[i, col2] = temp
        
    return new_matrix

def sum_main_diagonal(matrix):
    """Сумма элементов главной диагонали"""
    n = matrix.shape[0]
    total = 0
    for i in range(n):
        total += matrix[i, i]
    return total

# Чтение матрицы из файла
fi = open("lab6_5.txt", "rt")

# Пропуск заголовка
fi.readline()  # # Квадратная матрица 4x4
fi.readline()  # #------------------------

# Чтение матрицы
matrix_data = []
for line in fi:
    if line.strip():
        row = [float(x) for x in line.split()]
        matrix_data.append(row)
fi.close()

# Преобразование в numpy массив
matrix = np.array(matrix_data)

# Запись результатов в файл
fo = open("laba6_5_out.txt", "wt")

# Запись исходной матрицы
fo.write("Исходная матрица:\n")
n_rows, n_cols = matrix.shape
for i in range(n_rows):
    for j in range(n_cols):
        fo.write("{0:7.2f}".format(matrix[i, j]))
    fo.write("\n")
fo.write("\n")

# Поиск столбцов с экстремумами
max_col, min_col = find_min_max_cols(matrix)
fo.write("Столбец с максимальным элементом: {0}\n".format(max_col))
fo.write("Столбец с минимальным элементом: {0}\n".format(min_col))
fo.write("\n")

# Обмен столбцов
modified_matrix = swap_columns(matrix, max_col, min_col)

# Запись измененной матрицы
fo.write("Матрица после обмена столбцов:\n")
for i in range(n_rows):
    for j in range(n_cols):
        fo.write("{0:7.2f}".format(modified_matrix[i, j]))
    fo.write("\n")
fo.write("\n")

# Вычисление сумм диагоналей
diag_sum_orig = sum_main_diagonal(matrix)
diag_sum_mod = sum_main_diagonal(modified_matrix)

fo.write("Сумма элементов главной диагонали исходной матрицы: {0:.4f}\n".format(diag_sum_orig))
fo.write("Сумма элементов главной диагонали новой матрицы: {0:.4f}\n".format(diag_sum_mod))

fo.close()

print("Результаты записаны в файл lab6_5_out.txt")
