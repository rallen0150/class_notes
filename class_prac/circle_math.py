class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return round(self.radius**2*3.14, 3)

    def perimeter(self):
        return round(2*self.radius*3.14, 3)

x = int(input("Enter the radius of a circle: "))
NewCircle = Circle(x)
print(NewCircle.area())
print(NewCircle.perimeter())
