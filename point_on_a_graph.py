# Practice excercise from Datacamp's Object-Oriented Programming in Python course
import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return math.sqrt((self.x * self.x) + (self.y * self.y))
    
    def reflect(self, axis):
        if axis == 'x':
            self.y = -self.y
        elif axis == 'y':
            self.x = -self.x
        else:
            print("Error!")

pt = Point(x=3.0)
pt.reflect('y')
print((pt.x, pt.y))
pt.y = 4.0
print(pt.distance_to_origin())
