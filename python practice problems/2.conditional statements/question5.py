#WAP to determine whether a person is eligible to vote or not. If he/she is 
# not eligible, display how many years are left to be eligible.

age=int(input("enter age:"))
if age>=18:
    print("person is eligible to vote")
else:
    print("person is not eligible to vote")
years=18-age
print(years,"years left to eligible for vote")