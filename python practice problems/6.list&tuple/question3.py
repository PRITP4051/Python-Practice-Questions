# WAP that creates a list of 10 random integers. Then create two lists of all 
# odd and even numbers from it.
import random

list = [random.randint(-100000,100000) for _ in range(10)]
print("Random list:", list)
list1=[]
list2=[]
for i in list:
    if i%2==0:
        list1.append(i)
    else:
        list2.append(i)
print("even list:",list1)
print("odd list",list2)