import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Diagonal of the matrix:", matrix.diagonal())
print("Diagonal of the matrix with offset 1:", matrix.diagonal(offset=1))
print("Diagonal of the matrix with offset -1:", matrix.diagonal(offset=-1))
