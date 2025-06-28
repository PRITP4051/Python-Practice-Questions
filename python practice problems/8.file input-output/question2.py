#WAP to demonstrate open, read, write and close .txt and .csv files.
#  In addition, perform the following tasks:

# a. Add a line “Hello World! I am using python” in existing .txt file.
# b. Add following rows and columns in existing .csv file.
# # Roll No.      Name           Department        Course
#     11021       Mahek           CSE               Python
#     11022       Heer            ICT               Mathematics                     
#     11023       Pavan            CIE              Physics                        
#     11024       Moksh            ICT              Data Structure                   

# Part a: Add a line to an existing .txt file
txt_filename = "example.txt"

# Open file in append mode and write the line
with open(txt_filename, 'a') as txt_file:
    txt_file.write("\nHello World! I am using python\n")
print("Text added to example.txt")

# Part b: Add rows and columns to a .csv file
import csv

# Define the fields and rows
fields = ['Rollno', 'Name', 'Department', 'Course']
rows = [
    [11021, "Mahek", "CSE", "Python"],
    [11022, "Heer", "ICT", "Mathematics"],
    [11023, "Pavan", "CIE", "Physics"],
    [11024, "Moksh", "ICT", "Data Structure"]
]

csv_filename = "University_records.csv"

# Open the CSV file in write mode and add data
with open(csv_filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)   # Write header
    csvwriter.writerows(rows)    # Write data rows

print("Data written to University_records.csv")
