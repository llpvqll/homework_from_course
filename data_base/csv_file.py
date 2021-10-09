import csv


data = {}


def csv_writer():

    headers = ['First name', 'Second name', 'Birthday date', 'City']

    first_name = input("Enter your first name: ")
    second_name = input("Enter your second name: ")
    br_date = int(input("Enter your birthday date: "))
    city = input("Enter your city: ")

    data[headers[0]] = first_name
    data[headers[1]] = second_name
    data[headers[2]] = br_date
    data[headers[3]] = city

    with open("csv_file.csv", 'w', encoding='UTF-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerow((data[headers[0]], data[headers[1]], data[headers[2]], data[headers[3]]))


def csv_editor():
    pass


print("Hi, this program was created to help you write anything to a CSV file!")
print('For writing anything to the new file press "1"')
print('For writing something to an existing file press "2"')
print('For leaving from program press "3"')

while True:

    user_choice = int(input("Your choice: "))

    if user_choice == 1:
        csv_writer()
    elif user_choice == 2:
        csv_editor()
    elif user_choice == 3:
        break
    else:
        print("You entered a wrong character!")



