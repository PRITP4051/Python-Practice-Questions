#WAP to iterate an element of list and tuple using for and while loops.

list=[1,2,3,4,5,6,7,8,9,10,[1,2,3]]
tuple=(1,2,3,4,5,6,7,8,9,10,(1,2,3))
for i in range(0,len(list)):
    print(list[i],end=" ")
for i in range(0,len(tuple)):
    print(tuple[i],end=" ")
j=0
while j<len(list):
    print(list[j])
    j+=1
k=0
while k<len(tuple):
    print(tuple[k])
    k+=1
