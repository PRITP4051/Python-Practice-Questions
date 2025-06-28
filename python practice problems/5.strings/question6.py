#WAP to return a string in title case. Do not use built in function title( ). (If 
# string is “The world is beautiful”, program should return the string in title 
# case as “The World Is Beautiful”.) 

a="the world is beautiful"
a=a[0].upper() + a[1:]
print(a)
for i in range(len(a)):
    if a[i]==" ":
        a=a[0:i+1]+a[i+1].upper()+a[i+2:]
print(a)