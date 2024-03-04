#super() - Function used to access parent class. returns tempropry object of parent class.
class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class square(rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)
    def area(self):
        return self.length*self.width


class cube(rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height=height
    def volume(self):
        return self.length*self.width*self.height

square=square(3,4)
cube=cube(3,4,5)
print(square.area())
print(cube.volume())



