#basic class and objects
# class Students:
#     name="Prit"
#     branch="CSE"
# s1=Students()
# print(s1.name)
# s2=Students()
# print(s2.branch)

#constructor and __init__ function
# class Students:
#     college="adani university"
#     name="xyz"    #class attribute
#     #parameterise constructor
#     def __init__(self,name,marks):
#         print("Adding student information")
#         self.name=name    #obj attribute > class attribute
#         self.marks=marks
# s1=Students("Prit",97)
# print(s1.name,s1.marks)
# s2=Students("smit",95)
# print(s2.name,s2.marks)
# print(Students.college)

#methos in class

# class Students:

#     def __init__(self,name,marks):
#         print("Adding student information")
#         self.name=name    #obj attribute > class attribute
#         self.marks=marks
#     def hello(self):
#         print("hello",self.name)
#     def get_marks(self):
#         return self.marks
# s1=Students("prit",97)
# s1.hello()
# print(s1.get_marks())


#question1
#create student class that take name and marks of 3 subjects as arguments in constructor
#then create a methos to print the average

# class Student:
#     @staticmethod
#     def hello():             #static method
#         print("hello")
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def ave(self):
#         sum=0
#         for value in self.marks:
#             sum+=value
#         average=sum/3
#         print("Hy",self.name,"Your Average marks is ",average)
# Student.hello()
# s1=Student("prit",[99,92,93])
# s1.ave()
# s1.name="smit"
# s1.ave()

#1.abstration

# class Car:
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.clutch=False
#     def start(self):
#         self.acc=True
#         self.clutch=True      #in this it doesn't show this unnecessary implimentation details to user
#         print("car started.......")
# c1=Car()
# c1.start()

#question2
#create account class with 2 attributes-balance and account number
# create methos for debit,credit,printing the balance

class Account:
    def __init__(self,balance,accountno):
        self.balance=balance
        self.accountno=accountno
    def debit(self):
        a=int(input("enter money to debit :"))
        self.balance-=a
        print("money after debit",a,"from account is ",self.get_balance())
    def credit(self):
        b=int(input("enter money to credit :"))
        self.balance+=b
        print("money after credit",b,"to account is ",self.get_balance())
    def get_balance(self):
        return self.balance

    
p1=Account(100000,101)
p1.debit()
p1.credit()




