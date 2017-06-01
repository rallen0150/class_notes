class RectangleMath:
    def __init__(self, x, y):
        self.width = x
        self.length = y

    def parameter(self):
        ans = (self.width*2) + (self.length*2)
        return round(ans, 2)

    def area(self):
        ans = self.width * self.length
        return round(ans, 2)

width = float(input("Enter the width of the rectangle: "))
length = float(input("Enter the length of the rectangle: "))

print(RectangleMath(width, length).parameter())
print(RectangleMath(width, length).area())
