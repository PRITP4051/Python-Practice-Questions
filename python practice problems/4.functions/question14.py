#WAP to print the sum of the following nth series: 
# a. 1 + ½2 + … + 1/n2 

# n=int(input("enter n:"))
# sum=0
# a=1
# for i in range(1,n+1):
#     sum=sum+ 1/(a**2)
#     a+=1
# print("sum of series is=",sum)

# b. 1 + (1+2) + (1+2+3) + … + (1 + 2+ … + n)     #imp

# n = int(input("enter n: "))
# total = 0
# a = 1
# for i in range(1, n + 1):
#     total = total + sum(range(1, a + 1))
#     a += 1
# print("sum of series is =", total)

# c. sinx = x – x3/3! + x5/5! – x7/7! + x9/9!     #imp

# import math

# def sin(x, n):
#     sine = 0
#     for i in range(n):                   
#         sign = (-1) ** i
#         pi = 22 / 7
#         y = x * (pi / 180)  # Convert degrees to radians
#         sine += ((y ** (2.0 * i + 1)) / math.factorial(2 * i + 1)) * sign
#     return sine

# x = int(input("Enter x value (in degrees): "))
# n = int(input("Enter number of terms: "))
# print("sin", x, "=", round(sin(x, n), 2))

#method 2
#  sinx = x – x3/3! + x5/5! – x7/7! + x9/9!
# import math as m
# n = int(input("enter n: "))
# x=int(input("enter x(in degree):"))
# total = 0
# a = 1
# for i in range(1, n + 1):
#     if i%2==0:
#         total=total- (x**a)/m.factorial(a)
#     else:
#         total=total+ (x**a)/m.factorial(a) 
#     a += 2
# print("sum of series is =", total)

#d.  cos x=1-x^2/2!+x^4/4!-x^6/6!+.............

# import math

# def cosine(x, n):
#     cosx = 1
#     sign = -1
#     pi = 22 / 7
#     y = x * (pi / 180)  # Convert degrees to radians
#     for i in range(2, n, 2):
#         cosx += (sign * (y ** i)) / math.factorial(i)
#         sign = -sign
#     return cosx

# x = int(input("Enter the value of x in degrees: "))
# n = int(input("Enter the number of terms: "))
# print("cos", x, "=", round(cosine(x, n), 2))

#method2
# cos x=1-x^2/2!+x^4/4!-x^6/6!+.............
# import math as m
# n = int(input("enter n: "))
# x=int(input("enter x(in degree):"))
# total = 0
# a = 0
# for i in range(1, n + 1):
#     if i%2==0:
#         total=total- (x**a)/m.factorial(a)
#     else:
#         total=total+ (x**a)/m.factorial(a) 
#     a += 2
# print("sum of series is =", total)

#  e.1-x+x^2/2!x^3/3!+........ x^n/n! in python

# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)

# def calculate_series_sum(x, n):
#     result = 0
#     for i in range(n):
#         term = (-1) ** i * x ** i / factorial(i)
#         result += term
#     return result

# x_value = float(input("Enter the value of x: "))
# n_terms = int(input("Enter the number of terms (n): "))
# sum_series = calculate_series_sum(x_value, n_terms)
# print(f"The sum of the series is: {sum_series}")

#method 2
#  1-x+ x^2/2!- x^3/3!+........ x^n/n!
import math as m
n = int(input("enter n: "))
x=int(input("enter x:"))
total = 0
a = 0
for i in range(1, n + 1):
    if i%2==0:
        total=total- (x**a)/m.factorial(a)
    else:
        total=total+ (x**a)/m.factorial(a) 
    a += 1
print("sum of series is =", total)
