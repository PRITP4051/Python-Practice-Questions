#WAP to find whether a given character is present in a string or not. In case it 
# is present, print the index at which it is present. Do not use built-in find 
# function to search the character.
n=input("enter the string: ")
z=input("enter character: ")
for i in z:
    if i in n:
        print("character present in a string:")
        print("character found at index ",n.index(i))
    else:
        print("character does not present in a string")
