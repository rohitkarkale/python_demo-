class Animal :

    Alive=True


    def eat(self):
        print("This animal is eating.")

    def sleep(self):
        print("This animal is sleeping.")

class Rabbit(Animal) :
    def run(self):
        print("This rabbit is running")
    pass
class Fish(Animal):
    def swim(self):
        print("This fish is swimming")
    pass
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")
    pass
rabbit=Rabbit()
fish=Fish()
hawk=Hawk

rabbit.run()
fish.swim()
