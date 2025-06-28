#1.print number from 1 to 100
# i=1
# while i<=100:
#     print(i)
#     i += 1

#2.print number from 100 to 1
# i=100
# while i>=1:
#     print(i)
#     i -= 1

#3.print multiplication table of number n 

# n=int(input("Enter a number: "))
# i=1
# while i<=10:
#     print(n, "x", i, "=", n*i)
#     i += 1

#4.print elements of list
# list=[1,4,9,16,25,36,49,64,81,100]
# index=0
# while index<len(list):
#     print(list[index])
#     index += 1

#5.print element x from any tuple     {this called linear search}
# nums= (1,4,9,16,25,36,49,64,81,100)
# x=36
# i=0
# while i<len(nums):
#     if(nums[i]==x):
#         print("found at index",i)
#     i+=1

# # question 4 using for loop
# list=[1,4,9,16,25,36,49,64,81,100]
# for i in list:
#     print(i)

# quetion 5 using for loop

# nums= (1,4,9,16,25,36,49,64,81,100,36)
# x=36
# index=0
# for i in nums:
#     if(i==x):
#         print("found at index",index)
#         # break
#     index+=1

#question 1 using for and range
# for i in range(1,101):
#     print(i)

# #question 2 using for and range
# for i in range(100,0,-1):
#     print(i)

# quetion 3 using for and range
# n=int(input("enter a number:"))
# for i in range(1,11):
#     print(n,"x",i,"=",n*i)

#find the sum of first n numbers using while loop and for loop

# num=int(input("enter the number:"))
# i=1
# sum=0
# while i<=num:
#     sum=sum+i                       #while loop
#     i=i+1
# print("The sum of first", num, "numbers is:", sum)


# n=int(input("Enter the number: "))
# sum=0
# for i in range(1, n + 1):  # for loop
#     sum += i
# print("The sum of first", n, "numbers is:", sum)

#find the factiorial of a number using for loop

#for loop
# n = int(input("Enter a number: "))
# factiorial=1
# for i in range(1, n + 1):
#     factiorial *= i
# print("The factorial of", n, "is:", factiorial)

#while loop
# n=int(input("Enter a number: "))
# factiorial=1
# i=1
# while i <= n:
#     factiorial *= i
#     i += 1
# print("The factorial of", n, "is:", factiorial)

