#WAP that accepts a string from user and redisplays the same string after 
# removing vowels from it.
vowel="aeiouAEIOU"
n=input("enter the string: ")
ans=""
for i in n:
    if i not in vowel:
        ans+=i
print("string after remove vowels: ",ans)