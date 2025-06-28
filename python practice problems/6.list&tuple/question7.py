#WAP using filter() function to filter out only even numbers from a list.
import random as r

def check(i):
    return i % 2 == 0  # Return True for even numbers

lst = [r.randint(-100000, 100000) for i in range(15)]
evens = list(filter(check, lst))
print("Original list:", lst)
print("Even numbers:", evens)

