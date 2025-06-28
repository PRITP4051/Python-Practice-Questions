#zerodivisionerror
# n1=int(input("enter first number: "))
# n2=int(input("enter zero: "))
# div=n1/n2
# print(div)

#try and except
try:
    n1=int(input("enter first number: "))
    n2=int(input("enter zero: "))
    div=n1/n2
    print(div)
except ZeroDivisionError:
    print("can not divide by zero")
print("hello world")
    