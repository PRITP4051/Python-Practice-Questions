#Write a function that gives numbers of words of a given string. 
def count_words(s):
    words = s.split()  # Split the string into words using whitespace
    return len(words)  # Return the number of words

# Example usage:
text = input("Enter a string: ")
print("Number of words:", count_words(text))