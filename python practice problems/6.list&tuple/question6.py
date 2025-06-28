#WAP to combine values in two lists using list comprehension. Combine only 
# those values of a list that are multiples of values in the first list. 

list1=[2,3,4,7,8]
list2=[9,11,13,14,75,22,98]
list3=[[x,y] for x in list1 for y in list2 if (x%y==0) or (y%x==0)]
print(list3)