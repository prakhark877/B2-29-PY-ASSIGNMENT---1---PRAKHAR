class Structure:
    def area():
        return 0
        
class Square(Structure):
    def __init__(self,l):
        self.l = l
    def area(self):
        return self.l**2

obj = Structure
print(f"area of struture is : {obj.area()}")
l = int(input("Enter the side of the square : "))
obj = Square(l)
print(f"area of square :{obj.area()}")
