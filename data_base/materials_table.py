import csv

quoting = csv.QUOTE_ALL

headers = ['ID', 'weight', 'height', 'add specification']
with open('materials.csv', 'w', encoding="UTF-8") as file:
    # create headers in file
    writer = csv.DictWriter(file, fieldnames=headers, quoting=quoting)
    writer.writeheader()
    # add users
    # add first user
    writer.writerow({
        'ID': 1,
        'weight': 90,
        'height': 181,
        'add specification': ['Vladislav', 'administrator']
    })
    # add second user
    writer.writerow({
        'ID': 2,
        'weight': 70,
        'height': 181,
        'add specification': ['Vlad', 'deputy administrator']
    })

