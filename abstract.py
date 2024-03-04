from abc import ABC, abstractmethod
class car(ABC):
    def mileage(self):
        pass

class tesla(car):
    def mileage(self):
        print("The mileage is 30kph")
class suzuki(car):
    def mileage(self):
        print("The mileage is 25kph")
class duster(car):
    def mileage(self):
        print("The mileage is 24kph")

class renault(car):
    def mileage(self):
        print("The mileage is 30kph")

obj1=tesla()
