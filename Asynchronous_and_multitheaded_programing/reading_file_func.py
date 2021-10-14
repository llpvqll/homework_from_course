import time
import os


FILENAME = 'example.txt'


def finding_wow():
    need_word = 'Wow'
    with open(FILENAME, 'r', encoding='utf-8') as file:
        try:
            for item in file:
                if need_word in item:
                    print('yes')
                    print(f'"WOW" is found, file will be delete!')
                    file.close()
                    delete_file()
            else:
                print(f'"WOW" cannot be found, try again!')
                time.sleep(5)
                finding_wow()
        except (ValueError, TypeError):
            pass


def delete_file():

    os.remove(FILENAME)
    print(f'File was deleted!')


if __name__ == "__main__":
    finding_wow()