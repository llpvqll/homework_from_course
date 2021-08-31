import random
import pickle


def real_numbers():
    # creating random float num, and write to file
    data = []
    for item in range(10000):
        data.append(random.random())
        pickle.dump(data, open('binary_data', 'wb'))


real_numbers()


def get_sum_from_database():
    with open('binary_data', 'rb') as file:
        some_result = pickle.load(file)
    result = 0
    for item in some_result:
        item = float(item)
        result += item
    print(result)


get_sum_from_database()
