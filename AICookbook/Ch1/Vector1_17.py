import numpy as np

matrix_a = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 2]])
matrix_b = np.array([[1, 3, 1], [1, 3, 1], [1, 3, 8]])

matrix_add = np.add(matrix_a, matrix_b)
print("Matrix add:\n", matrix_add)

matrix_subtract = np.subtract(matrix_a, matrix_b)
print("Matrix subtract:\n", matrix_subtract)
