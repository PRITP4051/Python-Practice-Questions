# WAP to display the grade of student for a given marks.  
# Marks   
# Grade 
# > 90       a  
# >80        b
# >70        c
# >60        d
# >50        e
# <50        fail

# Program to display the grade of a student for given marks

marks = int(input("Enter the marks: "))

if marks > 90:
    grade = 'a'
elif marks > 80:
    grade = 'b'
elif marks > 70:
    grade = 'c'
elif marks > 60:
    grade = 'd'
elif marks > 50:
    grade = 'e'
else:
    grade ="fail"

print("Grade:",grade)
