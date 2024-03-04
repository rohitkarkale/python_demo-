class Duck :
    def walk(self):
        print("This duck is walking")
    def talk(self):
        print("This duck is quwking")

class Chicken :
    def walk(self):
        print("This chicken is walking")
    def talk(self):
        print("This chicken is clucking")

class Person :
    def catch(self,duck):

        print("You caught the clitter!")

duck=Duck()
chicken=Chicken()
person=Person()

duck.walk()
duck.talk()
person.catch(duck)