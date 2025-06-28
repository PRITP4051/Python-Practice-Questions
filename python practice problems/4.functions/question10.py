#Write a function that to convert time into minutes. 

def conv(t):
    return t*60

t=int(input("enter the time(in hours):"))
print("minute of given time",t,"hours is:",conv(t))
