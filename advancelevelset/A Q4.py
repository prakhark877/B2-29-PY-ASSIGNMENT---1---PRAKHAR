class Shape:
    def area():
        return 0

class Square(Shape):
    def __init__(self,length):
        self.length = length
    def area(self):
        return self.length**2

obj_superclass = Shape
print(f"area of shape: {obj_superclass.area()}")
length = int(input("side of the square: "))
obj_subclass = Square(length)
print(f"area of square :{obj_subclass.area()}")
