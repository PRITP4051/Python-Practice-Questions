#WAP to remove nth index character from a non-empty string. 
x="Prit Patel"
n=int(input("enter index to remove:"))
z=x[:n]+x[n+1:]
print("after removing nth index character:",z)