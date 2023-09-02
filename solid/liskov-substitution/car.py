"""
Another example for LSP. RacingCar cannot inherit Car because it doesnt
have a cabin width. Instead it has a cockpit. To adhere to LSP rule, a
vehicle class is created as a base class for both car and racingcar.
"""


class Vehicle():
    def __init__(self) -> None:
        pass

    def get_interior(self):
        pass


class Car(Vehicle):
    def __init__(self) -> None:
        self._cabin_width = 2

    def get_interior(self):
        return self.get_cabin_width()

    def get_cabin_width(self):
        print("Car get cabin width")
        return self._cabin_width


class RacingCar(Vehicle):
    def __init__(self) -> None:
        self._cockpit_width = 1

    def get_interior(self):
        return self.get_cockpit_width()

    def get_cockpit_width(self):
        print("RacingCar get cockpit width")
        return self._cockpit_width


class VehicleUtils():
    def print_ls_car_width(ls_cars: 'list'):
        for car in ls_cars:
            print(car.get_interior())


a = Car()
b = RacingCar()
VehicleUtils.print_ls_car_width([a, b])
