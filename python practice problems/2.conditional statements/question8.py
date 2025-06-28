#WAP to enter any character. If entered character is in lowercase then convert it 
# into uppercase and if it is an uppercase, then convert it into lowercase. 
a=input("enter the character:")
if a>="a" and a<="z":
    print("lowercase")
    print(a.upper())
if a>="A" and a<="Z":
    print("uppercase")
    print(a.lower())