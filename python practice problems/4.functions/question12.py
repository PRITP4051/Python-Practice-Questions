#WAP that prints absolute value, square root and cube of a number. 

import math
def num(n):
    print("number=",n)
    a=math.sqrt(n)
    print("square root of",n,"is:",a)
    z=n**3
    print("cube of",n,"is:",z)
    return n,a,z
n=int(input("enter the number:"))
num(n)