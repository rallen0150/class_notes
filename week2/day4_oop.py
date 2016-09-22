
class Person:

    def __init__(self, name):
        self.name = name


class Bike:

    def __init__(self, speeds, owner):
        self.speed = speeds
        self.owner = owner
        self.color = "grey"
        self._layers = 1  # Adding the _ before layers means outside peope cannot change the code

    def set_color(self, new_color):
        self.color = new_color
        self._layers += 1  # Adding the _ before layers means outside peope cannot change the code

    def get_layers(self):
        return self._layers  # Adding the _ before layers means outside peope cannot change the code


robbie = Person("Robbie")
joel = Person("Joel")

bike = Bike(18, joel)
robbie_bike = Bike(100, robbie)

print("OWNERS==============")
print(bike.owner.name)
print(robbie_bike.owner.name)

print(bike)
print("Color before we change it")
print(bike.color)
print(bike.get_layers())
print(bike.speed)

print("Color after we change it")
bike.set_color("red")
print(bike.color)
print(bike.get_layers())

print("Color of robbies bike")
print(robbie_bike.color)
print(robbie_bike.speed)

for x in range(100):
    bike.set_color("red")

print(bike.get_layers())
