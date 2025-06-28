#WAP using map() function to create a list of squares of numbers in the range 
# 1 to 10. 
def sqr(x):
    return x**2
a=[1,2,3,4,5,6,7,8,9,10]
print(a)
b=list(map(sqr,a))
print(b)

#WAP using map() function to a list of cubes of numbers from 1 – 10. 
def cube(i):
    return i**3
a=[1,2,3,4,5,6,7,8,9,10]
cubes=list(map(cube,a))
print(cubes)