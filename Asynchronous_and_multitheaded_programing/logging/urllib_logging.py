import urllib.request
import json

FILENAME = 'special_file.json'
URL = ["https://docs.python.org/3/library/urllib.request.html#module-urllib.request",
       "https://www.youtube.com/",
       "https://github.com/"]

DATA = []

for item in URL:
    response = urllib.request.urlopen(item)
    response_code = str(response.getcode())
    response_text = str(response.read(290).decode('utf-8'))
    DATA.append({response_code: response_text})

with open(FILENAME, 'w', encoding='utf-8', newline='') as file:
        json.dump(DATA, file)


# print('-'*20)
# print(f"Response code: {response_code}")
# print('-'*20)
# print(f"Text: \n {response_text}")
