#wap to calculate factorial of the number

n=int(input("enter the number:"))
count=1
factorial=1
while count<=n:
    factorial*=count
    count+=1
    if n==0 or n==1:
        print(1)
print("factorial of",n,"is:",factorial)
