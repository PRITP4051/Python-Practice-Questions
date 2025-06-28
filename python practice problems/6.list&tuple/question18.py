#WAP to insert a value in the list at the specified location using while loop. 

nlist=input("Enter a list of numbers separated by space : ").split()
print(f"{nlist=}")
ele,index=int(input("Enter the element to be inserted : ")),int(input("Enter the index: "))
while index>len(nlist):
 print("Index out of range")
 index=int(input("Enter the index : "))
nlist.insert(index,ele)
print(f"{nlist=}")