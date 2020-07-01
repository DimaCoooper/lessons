from time import sleep


class TrafficLight:

    __color = "red"

    def running(self):
        while True:
            print("red")
            sleep(7)
            print("yellow")
            sleep(2)
            print("green")
            sleep(3)

run = TrafficLight()

run.running()