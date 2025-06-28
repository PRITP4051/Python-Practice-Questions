#del keyword
# class Student:
#     def __init__(self,name):
#         self.name=name
# s1=Student("Prit")
# print(s1.name)
# del s1.name
# print(s1.name)


#private attributes and methods
# class Person:
#     __name="prit"   #__ make attribute private
#     def __hello(self):
#         print("hello")
#     def welcome(self):
#         return self.__hello()
# s1=Person()
# # print(s1.__name)
# # print(s1.__hello())
# s1.welcome()


#inheritence
#multi level

# class Car:
#     @staticmethod
#     def start():
#         print("car started....")
# class Toyotacar(Car):
#     def __init__(self,brand):
#         self.brand=brand
#     colour="black"

# class Fortuner(Toyotacar):
#     def __init__(self,type):
#         self.type=type

# c1=Fortuner("petrol")
# print(c1.type)
# c1.start()
# print(c1.colour)


#multiple inheritence

# class A:
#     a="hello"
# class B:                #multitask inheritence=multilevel+multiple inheritence
#     b="world"
# class C(A,B):
#     c="how are you?"
# c1=C()
# print(c1.a,c1.b,c1.c)

#super() keyword
# class Car:
#     def __init__(self,type):
#         self.type=type

#     @staticmethod
#     def start():
#         print("car started....")
# class Toyotacar(Car):
#     def __init__(self,name,type):
#         super().__init__(type)
#         self.name=name
#         super().start()

# s1=Toyotacar("fortuner","petrol")
# print(s1.type)


#class method
# class Person:
#     name="prit"
#     # def changename(self,name):   #it create new name varibale and store it value
#     #     self.name=name            #it does not change prit
#     # def changename(self,name):   
#     #     Person.name=name         #method 1
#     # def changename(self,name):   
#     #     self.__class__.name=name   #method 2
#     @classmethod
#     def changename(cls,name):     #method 3
#         cls.name=name

# s1=Person()
# s1.changename("rahul")
# print(s1.name)
# print(Person.name)


#property decorator
# class Student:
#     def __init__(self,phy,maths,che):
#         self.phy=phy
#         self.maths=maths
#         self.che=che
#     @property
#     def percentage(self):
#         return str((self.phy+self.maths+self.che)/3)+"%"
# s1=Student(98,95.5,96)
# print(s1.percentage)
# s1.phy=97.3
# print(s1.percentage)

#polymorphism 
#built in operator overloading
# print(1+2)   #addition
# print("hello"+"world") #concatination         #different meaning of + operator
# print([1,2]+[3,4])  #merge

#self mad operator overloading
# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
#     def shownumber(self):
#         print(self.real,"i +",self.img,"j")
#     def __add__(self,num2):
#         newreal=self.real+num2.real       #dunder function with denote by __ 
#         newimg=self.img+num2.img
#         return Complex(newreal,newimg) 
#     def __sub__(self,num2):
#         newreal=self.real-num2.real
#         newimg=self.img-num2.img
#         return Complex(newreal,newimg)

# num1=Complex(7,11)
# num1.shownumber()

# num2=Complex(5,8)
# num2.shownumber()

# num3=num1+num2
# num3.shownumber()

# num4=num1-num2
# num4.shownumber()

#question1
#define a circle class to create a circle with radius r using the constructor
#define the area() method of class which calculates the area of the circle
#define the perimeter() method which calculates the perimeter of the circle 

# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     @property
#     def area(self):
#         are=3.14*self.radius*self.radius
#         return f'area of circle is with radius {self.radius} is {are}'
#     @property
#     def parimeter(self):
#         perim=2*3.14*self.radius
#         return f'perimeter of circle with radius {self.radius} is {perim}'
    
# c1=Circle(7)
# print(c1.area)
# print(c1.parimeter)

# c1.radius=8
# print(c1.area)
# print(c1.parimeter)

#question2
#define a employee class with attributes role,department and salary this class also has
#showdetails() method
#create an engineer class that inherits properties from employee and has additional attribute
#name and age

# class Employee:
#     def __init__(self,role,department,salary):
#         self.role=role
#         self.department=department
#         self.salary=salary
#     def showdetails(self):
#         print([self.role,self.department,self.salary])
# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         super().__init__("seniour manager","technical",1500000)
    
    
# p1=Engineer("Prit",22)
# print(p1.name)
# print(p1.role)

#question3
#create a class order which stores item and its price
#use dunder function __gt__() to convey that:
#order1>order2 if price of order1>price of order 2


class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    # def __gt__(self,od2):
    #     if self.price>od2.price:                         #long ans
    #         print(self.item,"is bigger than",od2.item)
    #     else:
    #         print(od2.item,"is bigger than",self.item)
    def __gt__(self,od2):
        return self.price>od2.price

od1=Order("iphone 16 pro max","134000")
print(od1.item)
od2=Order("samsung s24 ultra","155000")
print(od2.item)
print(od1>od2)