# Write a program with class Employee that keeps a track of the number of 
# employees in an organization and stores their name, role and salary 
# details.
class Employee:
    count = 0  # Class variable to track number of employees

    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary
        Employee.count += 1  # Increment count when a new employee is created

    def show_details(self):
        print(f"Name: {self.name}, Role: {self.role}, Salary: {self.salary}")

    @classmethod
    def show_count(cls):
        print(f"Total Employees: {cls.count}")

# Example usage:
s1 = Employee("Prit", "Manager", 15000000)
s2 = Employee("Smit", "Assistant", 400000)

s1.show_details()
s2.show_details()
Employee.show_count()
