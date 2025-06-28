#WAP to demonstrate the use of various built-in functions such as count, find, 
# isalnum, isalpha, isdigit, islower, isupper, upper, lower,enumerate, replace, 
# swapcase, join etc. 

n="Adani University"
print(n.count("i"))
print(n.find("i"))
print(n.isalnum())
print(n.isalpha())
print(n.isdigit())
print(n.islower())
print(n.isupper())
print(n.upper())
print(n.lower())
print(n.replace("ni","uk"))
print(n.swapcase())
z="-".join(n)
print(z)
print(list(enumerate(n)))
