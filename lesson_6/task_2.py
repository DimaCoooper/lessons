class Road:

    def __init__(self, length, width):
        self._width = width
        self._length = length

    def road_area(self):

        area = self._width * self._length * 25 / 1000
        print(f"для ширины {self._width} и длины {self._length} трубется {area} кг асфальта")



length = int(input("length = "))
width = int(input("width = "))
a = Road(length, width)

a.road_area()
