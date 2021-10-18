class Meta(type):
    def __new__(cls, name, bases, attrs):
        attrs["custom_field"] = "NewValue"
        with open('example.txt', 'w') as file:
            file.write(str(super().__new__(cls, name, bases, attrs)))


class MyClass(metaclass=Meta):
    def __init__(self):
        print("Constructor")
        super().__init__()





