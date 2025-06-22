import numpy as np

matrix = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

mean = np.mean(matrix)

print(mean)

variance = np.var(matrix)
print(variance)

standard_deviation = np.std(matrix)
print(standard_deviation)

mean_column = np.mean(matrix, axis=0)
print(mean_column)
