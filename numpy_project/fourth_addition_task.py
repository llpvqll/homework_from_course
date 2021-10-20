import numpy as np

a = np.arange(1, 301)
print(a)
print('=' * 100)

a = a.reshape(3, 100)
print(a)
print('=' * 100)

b = np.arange(1, 301).reshape(6, 50)
print(b)
