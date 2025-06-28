#Write a Python script to print a dictionary where the keys are numbers 
# between 1 and 15 (both included) and the values are the square of the keys. 

list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
list2=[i**2 for i in list1]
dict=dict(zip(list1,list2))
print("Dictionary: ",dict)
