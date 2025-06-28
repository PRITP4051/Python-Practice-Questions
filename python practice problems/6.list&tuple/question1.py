#WAP to demonstrate the indexing and slicing of a list and tuple. 
list=[1,2,3,4,5,6,7,8,9,10,[1,2,3]]
print(list[5])         #indexing
print(list[0:4])
print(list[0:])
print(list[:len(list)])    #slicing
print(list[-5:-2])
print(list[::-1])
print(list[::2])
print(list[10][2])
tuple=(1,2,3,4,5,6,7,8,9,10,(1,2,3))
print(tuple[5])         #indexing
print(tuple[0:4])
print(tuple[0:])
print(tuple[:len(tuple)])    #slicing
print(tuple[-5:-2])
print(tuple[::-1])
print(tuple[::2])
print(tuple[10][2])
