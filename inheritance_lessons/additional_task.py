

class Vehicle:
    wheel_count = 4
    doors_count = 4
    max_speed = 200
    horse_power = 180
    color = "yellow"
    drive_unit = "front"

    def __str__(self):
        return f"Wheel amount: {self.wheel_count}\nDoors amount: {self.doors_count}\n" \
               f"Maximal speed: {self.max_speed}\nHorse power: {self.horse_power}\n" \
               f"Color of vehicle: {self.color}\nDrive unit: {self.drive_unit} \n"


class Truck(Vehicle):
    wheel_count = 6
    doors_count = 2
    max_speed = 140
    color = "white"
    drive_unit = 'back'


class CUV(Vehicle):
    max_speed = 240
    horse_power = 550
    color = "brown"
    drive_unit = "full"


class CityCar(Vehicle):
    pass


truck_view = Truck()
cuv_view = CUV()
city_car_view = CityCar()
print(truck_view)
print(cuv_view)
print(city_car_view)



