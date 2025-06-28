#WAP to find a random decimal number between 1 and 10 with two places of 
# accuracy for example 1.23, 3.45. 
import random

# Generate a random decimal number between 1 and 10 with two decimal places
num = round(random.uniform(1, 10), 2)
print("Random decimal number between 1 and 10 is:",num)