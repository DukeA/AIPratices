import numpy as np

matrix = np.array(
    [
        [1, 2, 3],
        [
            4,
            5,
            6,
        ],
        [7, 8, 9],
    ]
)

max = np.max(matrix)
print(max)

max_row = np.max(matrix, axis=0)
print(max_row)

min = np.min(matrix)
print(min)

min_row = np.min(matrix, axis=1)
print(min_row)
