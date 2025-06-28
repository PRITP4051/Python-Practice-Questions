# function defination and calling
# def calc_diff(a,b):
#     diff=a-b
#     print(f"Difference:",diff)
#     return diff

# calc_diff(99999,12054)

# def sum(a,b):
#     return a+b

# sum_result = sum(10, 20)
# print(sum_result)

# def print_hello():
#     print("Hello, World!")
# print_hello()
# print_hello()

# def average(a,b,c):
#     avg=(a+b+c)/3
#     print(f"Average of {a}, {b}, and {c} is: {avg}")

# qverage(10, 20, 30)

# #defult parameters in function

# def cal_prod(a=2,b=5):
#     print(a*b)
#     return a*b
# cal_prod()

#print length of list using functions

# list= [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# list1=[1,2,3,4,5,4,3]
# def cal_len(list):
#     print(len(list))
# cal_len(list)
# cal_len(list1)

#print all element of list in single line

# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# def print_list(list):
#     for i in list:
#         print(i, end=' ')

# print_list(list)

# #find factorial using functions
# def calc_fact(n):
#     factorial = 1
#     for i in range(1,n+1):
#         factorial*=i
#     print(factorial)
#     return factorial

# calc_fact(5)

# #convert us dollars to pak rupees using functions
# def conv(n):
#     inr = n * 86
#     print(n,"USD =",inr,"INR")
#     return inr
# conv(100)

# n=int(input("Enter a number: "))
# def is_even(n):
#     if n%2==0:
#         print("EVEN")
#     else:
#         print("ODD")

# is_even(n)


# def show(n):
#     if n==0:
#         return
#     print(n)
#     show(n-2)
# n=int(input("enter n"))
# show(n)
count=0
def ex(count):
    if count==101:
        return
    print(count)
    ex(count+1)
ex(count)


# show(10)
# sum of fisrt n numbers using recursion
# n = int(input("Enter a number: "))
# def sum(n):
#     if n==0:
#         return 0
#     return n+sum(n-1)
# print(sum(n))

# print element of list using recursion
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# def print_list(list,index=0):
#     if index == len(list):
#         return
#     print(list[index])
#     print_list(list, index + 1)
# print_list(list)





     








