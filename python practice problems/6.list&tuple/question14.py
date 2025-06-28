#WAP that reverse a list using a loop. 
a=[1,2,3,4,5,6,7,8,9,10]
first=0
last=len(a)-1
for i in range(first,last+1):
    if first<=last:
            (a[first],a[last])=(a[last],a[first])
            first+=1
            last-=1
print(a)

#metho2 
a=[1,2,3,4,5]
ra=[]
for value in a:
   ra=[value]+ra
print(ra)


#metho direct
a=[1,2,3,4,5,6,7,8,9,10]
a.reverse()
print(a)