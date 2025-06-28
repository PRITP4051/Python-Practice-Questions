#WAP to check whether a string is a palindrome or not. 
n=input("enter the string:")
z=n[::-1]
print("original string: ",n)
print("reverse string: ",z)
if n==z:
    print("string is a palindrome.")
else:
    print("string is not a palindrome.")



