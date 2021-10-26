from datetime import datetime


# create main class
class User:
    def __init__(self, surname, name, patronymic, birthday):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.year, self.months, self.day = birthday.split(' ')

    def get_short_name(self):
        """ Method created for showing full surname, and for one letter from name and patronymic """
        return f'{self.surname} {self.name[0]}.{self.patronymic[0]}'

    def get_full_name(self):
        """ Method created for showing full user's name """
        return f'{self.surname} {self.name} {self.patronymic}'

    def get_age(self):
        """ Method which showing date when user was born """
        year, months, day = int(self.year), int(self.months), int(self.day)
        birthday = datetime(year, months, day)
        return datetime.date(birthday)

    def get_initials(self):
        """ Method which showing user's initials, first letter from surname, name and patronymic """
        return f'{self.surname[0]}.{self.name[0]}.{self.patronymic[0]}.'

    def set_full_name(self):
        """ Method which showing full name, but after splitting by space from function get_full_name """
        full_name = self.get_full_name().split(' ')
        return full_name

    def __str__(self):
        """ Method which take all information from other function and show them """
        return f'{self.get_short_name()}\n' \
               f'{self.get_full_name()}\n' \
               f'{self.get_initials()}\n' \
               f'{self.set_full_name()}\n' \
               f'{self.get_age()}'


# set variables
my_name = 'Vladislav'
my_surname = 'Palamarchuk'
my_patronymic = 'Olegovich'
my_birthday = '2002 02 26'

# setting instance of class
U = User(my_surname, my_name, my_patronymic, my_birthday)
result = U.__str__()

# call my str method
print(result)
