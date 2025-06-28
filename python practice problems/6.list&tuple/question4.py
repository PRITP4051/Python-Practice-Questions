#WAP that creates a list of words by combining the words in two individual 
# lists. 
list1=["Hello","Prit","Narendra","Virat"]
list2=["World","Patel","Modi","Kohli"]
list3=[]
for i in range(0,len(list1)):
    for j in range(0,len(list2)):
        if i==j:
            name=list1[i]+" "+list2[j]
            list3.append(name)
print("combining word list: ",list3)
