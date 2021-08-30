import json
import pickle

data = {
    'one': 'milk',
    'two': 'bread',
    'three': 'chocolate',
    "four": 'tomatoes',
    'five': 'water',
}

# pickle.dump(data, open('data.pkl', 'wb', pickle.HIGHEST_PROTOCOL))

with open('data.pkl', 'rb') as f:
    ready_to_write = f.read()

with open('data.json', 'w') as file:
    file.write(str(ready_to_write))




