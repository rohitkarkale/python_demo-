class car:

    def __init__(self,make,model,year,colour):
        self.make=make
        self.model=model
        self.year=year
        self.colour=colour

    def drive(self):
        print("This car is driving ")

    def stop(self):
        print("This car is stopped ")