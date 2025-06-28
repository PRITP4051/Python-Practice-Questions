#Write a program that has a class Point with attributes as the X and Y co
# ordinates. Make two objects of this class and find the midpoint of both the 
# points.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def find_midpoint(p1, p2):
    mid_x = (p1.x + p2.x) / 2
    mid_y = (p1.y + p2.y) / 2
    return Point(mid_x, mid_y)

# Example usage:
point1 = Point(2, 4)
point2 = Point(6, 8)

mid = find_midpoint(point1, point2)
print(f"Midpoint:({mid.x},{mid.y})")
