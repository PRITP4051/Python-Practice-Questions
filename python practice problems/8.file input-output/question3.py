#WAP for considering the following instructions:

# a. Create a text file named “input.txt” and write some text data into it.
# b. Write a Python program that opens the “input.txt” file for reading, 
#    reads the contents of the file, and prints them to the console.
# c. Open another text file named “output.txt” for writing, 
#    and write the contents read from “input.txt” into “output.txt”.
# d. Finally, close both files after reading from and writing to them.

# Step a: Create a file and write some text into it
with open("input.txt", "w") as file:
    file.write("This is a sample input file.\n")
    file.write("We are learning file handling in Python.\n")
    file.write("This is written using write() method.\n")

print("input.txt created and written successfully.")

# Step b: Read from input.txt and print the content
with open("input.txt", "r") as file:
    data = file.read()
    print("\nContents of input.txt:")
    print(data)

# Step c: Write the content into output.txt
with open("output.txt", "w") as file:
    file.write(data)

print("\nContent copied to output.txt successfully.")
