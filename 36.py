class organism :
    Alive=True

class Animal(organism):
    def eat(self):
        print("This animal is eating")

class Dog(Animal):
    def bark(self):
        print("This daog is barking ")

dog=Dog()

print(Dog.Alive)
dog.bark()
