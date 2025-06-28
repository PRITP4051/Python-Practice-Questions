# #WAP to read the numbers until -1 is encountered. Also count the negative, positives 
# and zeroes entered by the user. 
i=0
j=0
k=0
while True:
    a=int(input("enter the number:"))
    if a==-1:
        break
    elif a>0:
        i=i+1
    elif a<0:
        j=j+1
    elif a==0:
        k=k+1
print("number of positive:",i)
print("number of negative:",j)
print("number of zeroes:",k)