#WAP to find whether a particular element is present in the list using a loop.
n=int(input("enter element to check:"))
list=[1,2,3,4,5,6,7,8,9,10]
for i in list:
    if n==i:
        print(n,"is present in the list")
        break
else:
    print(n,"is not present in the list")



#note- iif we write if and else both statement in for loop it print not present untill current 
#element did not come
