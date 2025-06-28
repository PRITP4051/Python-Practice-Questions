#Write a program that uses class to store the name and marks of students. Use 
# list to store the marks in three subjects. 

class Student:
    @staticmethod
    def hello():             #static method
        print("hello")
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
Student.hello()
s1=Student("prit",[99,92,93])
print(s1.name,s1.marks)