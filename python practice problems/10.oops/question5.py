#Write a program that has class Numbers with values stored in a list. Write a 
# class method to find the largest value.

class Numbers:
    def __init__(self, numbers):
        self.numbers = numbers

    def largest(self):
        maxnum = max(self.numbers)
        print("Largest number is:", maxnum)

s1 = Numbers([10, 50,30])
s1.largest()
