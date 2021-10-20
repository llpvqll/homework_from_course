

class Meta(type):
    def __new__(mcs, name, parents, dct):
        dct['x'] = 8
        return super(Meta, mcs).__new__(mcs, name, parents, dct)


class MyClass(metaclass=Meta):
    pass


m = Meta
newMetaClass = m.__new__(mcs=m, name='NewClass', parents=(), dct={'x': 8, 'y': 7})
with open('example.txt', 'w') as file:
    file.writelines(str({'name': MyClass.__name__,
                         'hash': MyClass.__hash__,
                         'type': type(MyClass)}))

    file.write(str({'name': newMetaClass.__name__,
                    'hash': newMetaClass.__hash__,
                    'type': type(newMetaClass)}))





