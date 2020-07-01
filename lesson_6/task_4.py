class Car:
    def __init__(self, speed, color, name, is_police, direction):
        self.speed = int(speed)
        self.color = str(color)
        self.name = str(name)
        self.is_police = bool(is_police)
        self.direction = str(direction)
        print(f"color = {self.color}, name = {self.name}, is_police = {self.is_police}")

    def go(self):
        print("Car go")

    def stop(self):
        print("Car stop")


    def turn(self):
        if self.direction in ["left", "right"]:
            print(f"Car turn {self.direction}")
        else:
            print("error")

    def show_speed(self):
        print(self.speed)



class TownCar(Car):

    "TownCar"

    def show_speed(self):
        print(f"speed = {self.speed}")
        if self.speed > 60:
            print("Сбавьте скорость")

class SportCar(Car):
    "SportCar"


class WorkCar(Car):
    "WorkCar"

    def show_speed(self):
        print(f"speed = {self.speed}")
        if self.speed > 40:
            print("Сбавьте скорость")
class PoliceCar(Car):
    "PoliceCar"


try:
    car = TownCar(40, "red", "BMW", False, "left")
except:
    print("error type")

car.show_speed()

