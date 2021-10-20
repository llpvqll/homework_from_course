import numpy as np

# creating matrix
a = np.arange(1, 145).reshape(12, 12)

print('=' * 100)
print("Simple matrix")
print()
print(a)

# transposing matrix
a = a.transpose()

print('=' * 100)
print("Transposed matrix")
print()
print(a)

# erection and multiplication of a matrix
a = (np.linalg.matrix_power(a, 2)) * 2
print('=' * 100)
print("Matrix after exponentiation and multiplication")
print()
print(a)

# subtraction of the identity matrix
b = np.diag([i for i in range(1, 13)])
print('=' * 100)
print(a - b)
