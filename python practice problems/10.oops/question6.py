#Write a class that stores a string and all its status details such as number of 
# uppercase characters, vowels, consonants, spaces etc.

#Write a class that stores a string and all its status details such as number of 
# uppercase characters, vowels, consonants, spaces etc.

class Str:
    def __init__(self, string):
        self.string = string

    def show_details(self):
        vowels = "aeiouAEIOU"
        num_vowels = 0
        num_consonants = 0
        num_upper = 0
        num_spaces = 0

        for ch in self.string:
            if ch.isupper():
                num_upper += 1
            if ch in vowels:
                num_vowels += 1
            elif ch.isalpha():
                num_consonants += 1
            if ch == " ":
                num_spaces += 1

        print("String:", self.string)
        print("Uppercase characters:", num_upper)
        print("Vowels:", num_vowels)
        print("Consonants:", num_consonants)
        print("Spaces:", num_spaces)

# Example usage:
s = Str("Hello World")
s.show_details()
        