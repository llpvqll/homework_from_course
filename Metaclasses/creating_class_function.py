
def creating_class_function(class_name, base_class, attrs):
    new_attrs = {}
    for attr, value in attrs.items():
        new_attrs[attr.lower()] = value

    return type(class_name, base_class, new_attrs)


attr = {
    'speed': 120,
    'Mark': 'Audi',
    'Color': 'Green'}

if __name__ == "__main__":
    Car = creating_class_function('Car', (), attr)

print(Car)
print(type(Car))
print(Car.__class__)
print(Car.speed.__class__)




