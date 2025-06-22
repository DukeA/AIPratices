import numpy as np

matrix = np.array([[1, 1, 1], [1, 1, 10], [1, 1, 15]])

lang_rank = np.linalg.matrix_rank(matrix)
print("Matrix Rank: ", lang_rank)
