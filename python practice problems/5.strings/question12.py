#Write a function to convert a given string to all uppercase if it contains at 
# least 2 uppercase characters in the first 4 characters.

def conv():
    count=0
    for i in range(0,4):
        if n[i].isupper():
            count+=1
    if(count>=2):
        print(n.upper())
    else:
        print(n)
n=input("enter the string:")
conv()