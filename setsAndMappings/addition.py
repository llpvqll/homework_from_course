

dictionary = {
    'first': 1,
    'second': 2,
    'third': 3,
    'fourth': 4,
    'fifth': 5,
}


def some(**kwargs):
    print(kwargs)


some(one=dictionary['first'], two=dictionary['second'], three=dictionary['third'])
