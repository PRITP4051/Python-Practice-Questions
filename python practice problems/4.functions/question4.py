#Write a function that returns the area and perimeter of a rectangle. Print the 
# area and perimeter of the rectangle. 
def rectangle(a,b):
    area=a*b
    perimeter=2*(a+b)
    print("area of rectangle is:",area)
    print("perimeter of rectangle is:",perimeter)
    return area,perimeter
a=float(input("enter the length:"))
b=float(input("enter the width:"))
rectangle(a,b)
