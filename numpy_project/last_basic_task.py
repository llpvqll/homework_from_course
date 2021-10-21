import numpy as np
from numpy import ndarray

FILENAME = 'weather.txt'


def writer_to_file():
    three_months_matrix = np.random.randint(15, 41, 90).reshape(3, 30)
    np.savetxt(FILENAME, three_months_matrix)
    reader_from_file()


def reader_from_file():
    reader = np.loadtxt(FILENAME, int)
    months_list = ['June', 'July', 'August']
    cycle = (i for i in months_list)
    index = 0
    for item in reader:
        print(f"{months_list[index]}\n{item} \nMaximal temperature {max(item)} \nMinimal temperature {min(item)}")
        print('=' * 100)
        index += 1


# reader_from_file()
writer_to_file()


