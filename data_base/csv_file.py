import csv
import xml.dom.xmlbuilder

import pandas as pd
import json

FILENAME = 'users.csv'
# data = {}
headers = ['First name', 'Second name', 'Birthday date', 'City']


def csv_writer():

    with open(FILENAME, 'w', encoding='UTF-8', newline='') as file:
        try:

            rows = int(input("How much rows you need?: "))
            writer = csv.writer(file)
            writer.writerow(headers)
            for i in range(rows):
                first_name = input("Enter your first name: ")
                second_name = input("Enter your second name: ")
                br_date = input("Enter your birthday date: ")
                city = input("Enter your city: ")
                writer.writerow([first_name, second_name, br_date, city])
        except (TypeError, ValueError):
            print("You enter a wrong character!")
            csv_writer()


def csv_editor():
    which_rows = int(input("Which rows you want edit: "))-1
    which_column = input(f'Which column you want edit {headers}: ')
    edited_user = input("Enter correct value: ")
    ed = pd.read_csv(FILENAME)
    ed.loc[which_rows, str(which_column)] = edited_user
    print(ed.loc[which_rows])
    ed.to_csv(FILENAME)


def line_reader():
    which_row_read = int(input("Which row you want to read?: "))-1
    lr = pd.read_csv(FILENAME)
    print(lr.loc[which_row_read])


def json_converting():
    json_file_path = r'Names.json'
    data = {}

    with open(FILENAME, encoding='utf-8') as csvf:
        csv_reader = csv.DictReader(csvf)

        for rows in csv_reader:
            key = rows['First name']
            data[key] = rows

    with open(json_file_path, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


def xml_converting():
    xml_file_path = r'Names.xml'
    xmlf = open(xml_file_path, 'w')
    csv_reader = csv.reader(open(FILENAME))
    xmlf.write('<?xml version="1.0"?>' + "\n")
    xmlf.write('<csv_data>' + "\n")

    row_num = 0
    for row in csv_reader:
        if row_num == 0:
            tags = row
            for i in range(len(tags)):
                tags[i] = tags[i].replace(' ', '_')
        else:
            xmlf.write('<row>' + "\n")
            for i in range(len(tags)):
                xmlf.write('    ' + '<' + tags[i] + '>' \
                      + row[i] + '</' + tags[i] + '>' + "\n")
            xmlf.write('</row>' + "\n")
        row_num +=1
    xmlf.write('</csv_data>' + "\n")
    xmlf.close()


print("Hi, this program was created to help you write anything to a CSV file!")
print('For writing anything to the new file press "1"')
print('For writing something to an existing file press "2"')
print('For reading a specific row press "3"')
print('For converting to JSON format press "4"')
print('For converting to XML format press "5"')
print('For leaving from the program press "6"')

while True:
    try:

        user_choice = int(input("Your choice: "))

        if user_choice == 1:
            csv_writer()
        elif user_choice == 2:
            csv_editor()
        elif user_choice == 3:
            line_reader()
        elif user_choice == 4:
            json_converting()
        elif user_choice == 5:
            xml_converting()
        elif user_choice == 6:
            break
    except (TypeError, ValueError):
        print("You entered a wrong character!")



