#WAP that creates a dictionary of cubes of odd numbers in the range 1 to 10 
# using dictionary comprehensions.
cube={i:i**3 for i in range(1,11) if i%2!=0}
print("cubes of odd numbers:",cube)
