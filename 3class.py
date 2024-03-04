class Base:
    def __init__(self):
        self.a="Rohit"
        self.__c="pune"

class Derieved(Base):
    def __init__(self):

# calling constructor of base class

        Base.__init__(self)
        print("calling private member of base class :")
        print(self.__c)

obj1=Base()
print(obj1.a)
