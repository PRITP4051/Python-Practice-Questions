#WAP to read two numbers. Then find out whether the first number is a multiple of 
# the second number.

a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
if a%b==0:
    print(a,"is multiple of",b)
else:
    print(a,"is not multiple of",b)