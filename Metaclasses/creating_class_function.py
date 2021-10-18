def creating_class_function():
    MyShinyClass = type('Car', (), {'color': "green", 'doors_count': 4, 'horse_power': 150})

    print(type(MyShinyClass))
    print(MyShinyClass.__class__)
    print(MyShinyClass)


if __name__ == "__main__":
    creating_class_function()

