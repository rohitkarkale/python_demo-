#method chaining = calling multiple methods subsequently
class car:

    def turn_on(self):
        print("You turned on the engine")
        return(self)
    def drive(self):
        print("You drive the car")
        return(self)

    def brake(self):
        print("You step on the brake ")
        return(self)

    def turn_off(self):
        print("You turned off the engine ")
        return(self)

car=car()

car.turn_on().drive().brake().turn_off()