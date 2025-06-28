#WAP to count the occurrence of each word in a given sentence.

n=input("enter the string: ")
word=input("enter word to check: ")
words=n.split()
count=0
for i in words:
    if i==word:
        count+=1
print(word,"word is occurrence ",count," times in the string.")