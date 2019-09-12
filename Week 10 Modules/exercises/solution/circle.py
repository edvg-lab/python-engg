import math

PI = math.pi

def calculate_diameter(radius):
    diameter = radius*2
    return diameter

def calculate_radius(diameter):
    radius = diameter/2
    return radius

def calculate_circumference(diameter):
    circumference = PI * diameter
    return circumference

def calculate_area(radius):
    area = PI * (radius ** 2)
    return area

