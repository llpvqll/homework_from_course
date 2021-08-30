import random


def real_numbers():
    data = []
    for item in range(10000):
        data.append(random.random())

    with open('random', 'w') as file:
        for item in data:
            file.writelines(str(item) + '\n')


real_numbers()


def get_sum_from_database():
    with open('random', 'r') as file:
        database = file.readlines(10000)

    result = 0
    for item in database:
        item = float(item)
        result += item

    print(result)


get_sum_from_database()

