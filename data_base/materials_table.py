import csv
import pandas as pd

quoting = csv.QUOTE_ALL
FILENAME = 'materials.csv'

headers = ['ID', 'weight', 'height', 'add specification']
with open(FILENAME, 'w', encoding="UTF-8") as file:
    # create headers in file
    writer = csv.DictWriter(file, fieldnames=headers, quoting=quoting)
    writer.writeheader()
    # add users
    # add first user
    writer.writerow({
        'ID': 1,
        'weight': 95.3,
        'height': 181,
        'add specification': ['Vladislav', 'administrator']
    })
    # add second user
    writer.writerow({
        'ID': 2,
        'weight': 70.6,
        'height': 181,
        'add specification': ['Vlad', 'deputy administrator']
    })
    # add third user
    writer.writerow({
        'ID': 3,
        'weight': 50,
        'height': 163,
        'add specification': ['Alexandra', 'administrator assistant']
    })


def weight_counter():
    data = []
    df = pd.read_csv(FILENAME)
    weight = df.get('weight')
    for item in weight:
        data.append(float(item))
    print(f"The sum of all weight: {round(sum(data))}")


def concatenation():
    with open(FILENAME, 'r', encoding='utf-8', newline='') as f:
        data = []
        reader = csv.reader(f)
        for item in reader:
            data.append(item)
        print(data)


concatenation()
print('-' * 20)
weight_counter()
