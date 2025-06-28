# WAP to read the values of coefficients and/or variables from the user and 
# print the output for the following expressions: 

#y= ax2 + bx + c 

a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
x=2
y=a*x*x+b*x+c
print(y)

# a = (b + c)*(b – c) 

b=int(input("enter the second number:"))
c=int(input("enter the third number:"))

a=(b+c)*(b-c)
print(a)

# 3. A = -(R1/R2+R3) 

R1=int(input("enter the first number:"))
R2=int(input("enter the second number:"))
R3=int(input("enter the third number:"))
A=-(R1/(R2+R3))
print(A)

# 4. I = (P*R*T)/100 

P=int(input("enter the first number:"))
T=int(input("enter the second number:"))
R=int(input("enter the third number:"))

I=(P*R*T)/100
print(I)


