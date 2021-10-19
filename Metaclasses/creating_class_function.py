def creating_class_function():
    car = type('Car', (), {'color': "green", 'doors_count': 4, 'horse_power': 150})

    print(type(car))
    print(car.__class__)
    print(car)


if __name__ == "__main__":
    creating_class_function()

