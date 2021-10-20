import numpy as np

print('=' * 100)
a = np.arange(625).reshape(25, 25)
print(a)
print('=' * 100)
b = np.diag([i for i in range(25)])
print(b)
print('=' * 100)
print(a * b)

