#Write a function to demonstrate local and global variable
num1 = 10  # global variable
print("Global variable num1 =", num1)

def func(num2):  # num2 is function parameter
    # Global variable num1 can be accessed within and outside the function
    print("In function - Global variable num1 =", num1)
    print("In function - Local variable num2 =", num2)
    num3 = 30
    print("In function - Local variable num3 =", num3)

func(20)
print("num1 again =", num1)

# Error - Local variable can't be used outside the function
# print("num3 outside function =", num3)  # This will cause a NameError