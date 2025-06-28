#mix error question
try:
    n1=int(input("enter string or number: "))
    n2=int(input("enter zero: "))
    div=n1/n2
    print(div)
except ValueError:
    print("your input is wrong.")
except ZeroDivisionError:
    print("can not divide by zero")