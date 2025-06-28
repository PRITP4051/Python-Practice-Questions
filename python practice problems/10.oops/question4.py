#Write a program that illustrates the difference between public and private 
# variables.

#Write a program that illustrates the difference between public and private variables.

class Demo:
    def __init__(self):
        self.public_var = "I am public"
        self.__private_var = "I am private"

    def show(self):
        print("Inside class:")
        print("Public:", self.public_var)
        print("Private:", self.__private_var)

obj = Demo()
obj.show()

print("\nOutside class:")
print("Public:", obj.public_var)          # Accessible

# The following line will cause an AttributeError if uncommented:
# print("Private:", obj.__private_var)    # Not accessible directly

# Accessing private variable using name mangling:
print("Private (using name mangling):", obj._Demo__private_var)
#error for upcoming part
print("Private (using name mangling):", obj.__private_var)