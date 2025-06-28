# WAP that prints all consonants in a string using list comprehension.
n=input("enter the string:")
str="aeiouAEIOU"
consonants=[char for char in n if char not in str]
print(consonants)
