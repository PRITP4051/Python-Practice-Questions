#wap to print reverse of the number using while loop
n=int(input("enter the number:"))
num=n
rev=""
count=0
while n>0:                   #we do this in string format
    rem=n%10
    rev=rev+str(rem)
    n=n//10
    count=count+1
print("reverse of number",num,"is:",rev)
print(count)

#method 2
num =int(input("Enter The Number: "))
reversed_num = 0
while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit         #in number format
        num //= 10

print("Reversed Number: ", reversed_num)
