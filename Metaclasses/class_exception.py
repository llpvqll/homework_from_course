class Except(type):

    def __new__(mcs, class_name, base_class, attrs):
        new_attrs = {}

        for attr, value in attrs.items():
            for item in attr:
                if item != item.lower():
                    raise NameError('Invalid character in the attribute/method name!')

                try:
                    int(item)
                    raise NameError('Invalid character in the attribute/method name!')
                except ValueError:

                    continue
            new_attrs[attr.lower()] = value
        return type(class_name, base_class, new_attrs)


attributes = {
    'speed': 120,
    'mark': 'Audi',
    'color': 'Green'}


Car = Except.__new__(Except, 'Car', (), attributes)

print(Car)
print(type(Car))
print(Car.__class__)
print(Car.color)
