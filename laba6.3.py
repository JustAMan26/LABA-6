# -*- coding: utf-8 -*-
import numpy as np

def create_matrix_from_file(filename):
    """Чтение матрицы из файла"""
    with open(filename, "r") as f:
        # Пропуск заголовка
        f.readline()
        # Чтение размера матрицы
        n = int(f.readline().strip())
        # Чтение данных матрицы
        data = []
        for line in f:
            if line.strip():
                row = [float(x) for x in line.split()]
                data.append(row)
        return np.array(data), n

def find_min_max_cols(matrix):
    """Поиск индексов столбцов с максимальным и минимальным элементами"""
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
    """Обмен двух столбцов в матрице"""
    new_matrix = matrix.copy()
    n_rows = new_matrix.shape[0]
    
    for i in range(n_rows):
        temp = new_matrix[i, col1]
        new_matrix[i, col1] = new_matrix[i, col2]
        new_matrix[i, col2] = temp
        
    return new_matrix

def sum_main_diagonal(matrix):
    """Вычисление суммы элементов главной диагонали"""
    n = matrix.shape[0]
    total_sum = 0
    for i in range(n):
        total_sum += matrix[i, i]
    return total_sum

def print_matrix_to_file(matrix, fo, title=""):
    """Запись матрицы в файл"""
    if title:
        fo.write(title + "\n")
    n_rows, n_cols = matrix.shape
    for i in range(n_rows):
        for j in range(n_cols):
            fo.write("{0:8.3f} ".format(matrix[i, j]))
        fo.write("\n")
    fo.write("\n")

# Чтение матрицы из файла
matrix, n = create_matrix_from_file("lab6_5.txt")

# Открытие файла для записи результатов
with open("lab6_5_out.txt", "w") as fo:
    fo.write("Лабораторная работа №5\n")
    fo.write("=" * 60 + "\n\n")
    
    # Вывод исходной матрицы
    print_matrix_to_file(matrix, fo, "Исходная матрица:")
    
    # Поиск столбцов с макс и мин элементами
    max_col, min_col = find_min_max_cols(matrix)
    fo.write("Столбец с максимальным элементом (индекс): {0}\n".format(max_col))
    fo.write("Столбец с минимальным элементом (индекс): {0}\n".format(min_col))
    fo.write("-" * 60 + "\n\n")
    
    # Обмен столбцов
    modified_matrix = swap_columns(matrix, max_col, min_col)
    
    # Вывод измененной матрицы
    print_matrix_to_file(modified_matrix, fo, "Матрица после обмена столбцов:")
    
    # Вычисление суммы главной диагонали
    diag_sum_orig = sum_main_diagonal(matrix)
    diag_sum_mod = sum_main_diagonal(modified_matrix)
    
    fo.write("Сумма элементов главной диагонали исходной матрицы: {0:.4f}\n".format(diag_sum_orig))
    fo.write("Сумма элементов главной диагонали новой матрицы:     {0:.4f}\n".format(diag_sum_mod))

print("Результаты записаны в файл lab6_5_out.txt")