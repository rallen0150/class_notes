# from math import pi #DOESN'T WORK, NO PI ATTRIBUTE

pi = 3.14159265358979323846

def simple_paramater(side):
    param = side*4
    return param

def circle_area(radius):
    area = (radius**2)*pi
    return area

def cylinder_volume(radius, height):
    volume = height*pi*(radius**2)
    return volume

radius = input("What is the radius of the circle? ")
radius = float(radius)
print(circle_area(radius))

new_radius = input("What is the radius of the cylinder? ")
height = input("What is the height of the cylinder? ")
new_radius = float(new_radius)
height = float(height)
print(cylinder_volume(new_radius, height))

side = input("Enter a side of the square: ")
side = float(side)
print(simple_paramater(side))
