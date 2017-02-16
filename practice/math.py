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

def triangle_area(base, height):
    area = (base*height)/2
    return area

def square_a_sum(x, y):
    ans = (x+y)**2
    return ans

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

base = input("What is the base of the triangle? ")
base = float(base)
height = input("What is the height of the triangle? ")
height = float(height)
print(triangle_area(base, height))

x = input("Enter the first number: ")
x = float(x)
y = input("Enter the second number: ")
y = float(y)
print(square_a_sum(x, y))
