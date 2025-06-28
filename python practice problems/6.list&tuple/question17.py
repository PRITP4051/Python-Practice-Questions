#WAP that counts the number of times a value appears in the list. Use a loop 
# to do the same. 
a=[1,2,3,4,7,1,5,4,8,9,1]
print(a.count(1))

#by loops
count=0
n=int(input("enter element to check: "))
for i in a:
    if i==n:
        count+=1
print(count)