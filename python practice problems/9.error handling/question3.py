#ValueError
# a=int(input("enter string or number: "))
# n=int(input("enter the number: "))
# print(a+n)

try:
    a=int(input("enter string or number: "))
    n=int(input("enter the number: "))
    print(a+n)
except ValueError:
    print("can not show output")
    

