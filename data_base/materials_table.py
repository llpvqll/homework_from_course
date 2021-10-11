import csv

headers = ['ID', 'weight', 'height', 'add_specification']
with open('materials.csv', 'w', encoding="UTF-8") as file:
    writer = csv.writer(file)
    writer.writeheader