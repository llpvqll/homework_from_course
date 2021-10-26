import smtplib
import sqlite3
import ssl
from datetime import datetime

PORT = 465
PASS = 'kerfdswz'
db = sqlite3.connect('user.db')
sql = db.cursor()
sql.execute('''CREATE TABLE IF NOT EXISTS users (
        name TEXT, 
        surname TEXT,
        patronymic TEXT, 
        birthday DATE, 
        email TEXT
    )''')
db.commit()


class User:
    def __init__(self, full_name, birthday, email):
        self.full_name = full_name
        self.year, self.months, self.day = birthday.split(' ')
        self.birthday = birthday
        self.email = email

    def get_full_name(self):
        return str(self.full_name)

    def get_short_name(self):
        last, name, patronymic = str(self.full_name).split(' ')
        return str(f"{last} {name[0]}.{patronymic[0]}.")

    def get_age(self):
        year, months, day = int(self.year), int(self.months), int(self.day)
        birthday = datetime(day, months, year)
        return datetime.date(birthday)

    def __str__(self):
        return self.get_full_name(), self.get_age(), self.email


def registry_new_user(full_name, birthday, email):
    name, surname, patronymic = full_name.split(' ')
    sql.execute("SELECT email FROM users")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?, ?, ?, ?, ?)", (name, surname, patronymic, birthday, email))
        db.commit()
    else:
        print("This email already was registry!")
    sending_message_to_mail(email)


def sending_message_to_mail(receiver_email):
    context = ssl.create_default_context()
    sender_email = 'testmailfortaskfromcourse@gmail.com'
    message = '''Thanks for registry in our database!'''
    with smtplib.SMTP_SSL('smtp.gmail.com', PORT, context=context) as server:
        server.login(sender_email, PASS)
        server.sendmail(sender_email, receiver_email, message)


def finding_user():
    for item in sql.execute("SELECT name, surname, email FROM users"):
        return item


name_input = input("Enter your full name, split by space: ").split(' ')
b_day = input('Enter you birthday (day, months, year), split by space: ')
email_input = input("Enter your Gmail (for example: petrov@gmail.com): ")
u = User(name_input, b_day, email_input)
print(u.__str__())
registry_new_user(u.get_full_name(), u.get_age(), u.email)
finding_user()

