import json 

FILENAME = 'sample_file.json'
simple_first_dict = {
    'name': 'Vlad',
    'surname': 'Palamarhuk',
    'height': 95,
    'weight': 181,
    'work': False,
}

simple_second_dict = {
    'name': 'Vladislav',
    'surname': 'Sodolevskiy',
    'height': 70,
    'weight': 181,
    'work': True,
}

with open(FILENAME, 'w', encoding='utf-8', newline='') as file:
    json.dump((simple_first_dict, simple_second_dict), file)

with open(FILENAME, 'r', encoding='utf-8', newline='') as f:
    reader = json.load(f)

print(reader)

