#wap to print multiplication table 
n=int(input("enter the number:"))
i=1
while i<=10:
    print(n,"x",i,"=",n*i)
    i+=1


#for loop and range
n=int(input("enter the number:"))
for i in range(1,n+1):
    print(n,"x",i,"=",n*i)