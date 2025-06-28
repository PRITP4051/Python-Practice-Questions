#WAP to remove all duplicates from a list.
# WAP to remove all duplicates from a list.
lst = [1, 2, 3, 4, 5, 1, 4, 3, 7, 8, 9]

# Using set to remove duplicates and then converting back to list
lst_no_duplicates = list(set(lst))

print("List after removing duplicates:", lst_no_duplicates)


#methos 2
li = ["apple","banana","mango","apple","banana","orange"]
dup_li = list()
for item in li:
 if item not in dup_li:
  
  dup_li.append(item)
print(dup_li)