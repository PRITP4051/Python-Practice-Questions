#WAP to find the roots of a quadratic equation ax2 + bx + c. (using math 
# module) 
import math
def sol(a,b,c):
    d=b**2-4*a*c
    D=math.sqrt(d)
    s1=(-b+D)/(2*a)
    s2=(-b-D)/(2*a)
    print("solution of quadratic equation ",a,"x2 + ",b,"x + ",c," is ",s1,"and",s2)
    return s1,s2

sol(9,12,4)