class Sample:
    pass

x=Sample()
print(type(x))

class Dog:
    attr1="mammal"
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("My name is {}".format(self.name))

Rodger=Dog("Rodger")
Tommy=Dog("Rodger")

Rodger.speak()
Tommy.speak()