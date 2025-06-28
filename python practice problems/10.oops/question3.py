# Write a program that has a class Circle. Use a class variable to define the 
# value of constant PI. Use this class variable to calculate area and 
# circumference of a circle with specified radius.

class Circle:
    pi=22/7
    def __init__(self,radius):
        self.radius=radius
    @property
    def area(self):
        are=self.pi*self.radius*self.radius
        return f'area of circle is with radius {self.radius} is {are}'
    @property
    def circumference(self):
        circum=2*self.pi*self.radius
        return f'perimeter of circle with radius {self.radius} is {circum}'
    
c1=Circle(7)
print(c1.area)
print(c1.circumference)

c1.radius=8
print(c1.area)
print(c1.circumference)
