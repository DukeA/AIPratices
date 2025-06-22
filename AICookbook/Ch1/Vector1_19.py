import numpy as np

matrix = np.matrix([[1, 4], [2, 5]])

invert_matrix = np.linalg.inv(matrix)

print("The inverse of the matrix is:")
print(invert_matrix)
