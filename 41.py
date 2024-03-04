
from abc import ABC, abstractmethod
class vehicle(ABC) :
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class car(vehicle):
    def go(self):
        print("You drive the car ")
    def stop(self):
        print("This car is stopeed ")

class motorcycle(vehicle):
    def go(self):
        print("You drive the motorcycle")
    def stop(self):
        print("This motorcycle is stopeed ")


car=car()
motorcycle=motorcycle()


car.go()
motorcycle.go()

car.stop()
motorcycle.stop()