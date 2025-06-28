# wap whether the given number is prime or not
# n=int(input("enter the number:"))
# if n>0:
#     for i in range(2,n):
#         if(n%i!=0):
#             print(n,"is the prime number.")
#         else:
#             print(n,"is not the prime number")
# else:
#     print(n,"is not the prime number.")

# #print all divisions

# n=int(input("enter number:"))
# for i in range(1,n+1):
#     if(n%i==0):
#         print(i,end=" ")

#method 2
import math as m
n=int(input("enter number:"))
list=[]
for i in range(1,int(m.sqrt(n)+1)):
    if(n%i==0):
        list.append(i)
        if((n/i)!=i):
            list.append(int(n/i))
list.sort()
print("sorted list",list)



