#WAP to check whether a given number is divisible by three, five and both three 
# and five.

n=int(input("enter the number:"))
if n%3==0 or n%5==0:
    if n%3==0 and n%5==0:
        print(n,"is divisible by 3 and 5")
    else:
        print(n,"is divisible by 3 or 5")