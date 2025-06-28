#Write a Python program to check if a given value is present in a set or not. 
s={1,2,3,4,5,6,7,8,9,10}
n=int(input("enter a number to check: "))
if n in s:
    print(n,"is present in given set.")
else:
    print(n,"is not present in given set.")