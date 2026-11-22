import math

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = math.pi * self.radius ** 2 #A = pi*r^2
        return area

radius = int(input("Ingrese el radio del círculo: "))
my_circle = Circle(radius)
print(f"El área del círculo es {my_circle.get_area()}")