#TypeError
# a=input("enter string: ")
# n=int(input("enter the number: "))
# print(a+n)


#try and except
try:
    a=input("enter string: ")
    n=int(input("enter the number: "))
    print(a+n)
except TypeError:
    print("can not show output.")
print("Hello World")
