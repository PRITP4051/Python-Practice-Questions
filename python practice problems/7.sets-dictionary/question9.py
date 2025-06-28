#WAP that creates a dictionary of radius of a circle and its circumference.
print("enter -1 to exit.....")
circumference={}
while True:
    r=float(input("enter the radius: "))
    if int(r)==-1:
        break
    else:
        Dict={r:2*3.14*r}
        circumference.update(Dict)
print(circumference)