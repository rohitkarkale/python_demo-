class prey :
    def flee(self):
        print("This animal flees")

class predator :
    def hunt(self):
        print("This animal hutns")

class Rabbit(prey):
    pass
class Hawk(predator):
    pass
class Fish(prey,predator):
    pass

rabbit=Rabbit()
hawk=Hawk ()
fish=Fish ()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()